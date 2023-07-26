from aiogram import types
from bot import dp, bot
from ..keyboards import inlineKeyboards as inKey
import os
from data import db

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query.id,
        ok=True,
        error_message='Payment error message (if needed)'
    )

@dp.shipping_query_handler()
async def process_shipping_query(shipping_query: types.ShippingQuery):
    await bot.answer_shipping_query(
        shipping_query_id=shipping_query.id,
        ok=True,
        shipping_options=[],
        error_message='Shipping error message (if needed)'
    )

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    plus = message.successful_payment.invoice_payload.split('-')[1]
    adminId = os.getenv('adminId')
    await bot.send_message(message.from_user.id, f'''
Спасибо за оплату и доверие! 
Внизу ссылка на канал, где будет вся организационная информация об экспресс-курсе. 
До встречи !)

P.S: ссылка действует только для одного входа (!)
''', reply_markup=await inKey.urlChannel(message))
    
    await bot.send_message(adminId, f'''
Имя: {message.from_user.full_name}
Тариф: {plus}
''', reply_markup=inKey.chatUser(message))
    db.addPaymentSuccess(message.from_user.id, plus)