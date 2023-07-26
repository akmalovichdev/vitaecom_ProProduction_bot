from aiogram import types
from bot import dp, bot
from data.config import yoomoneyToken

async def sendinvoice(userId, plus):
    if plus == '1':
        plus1 = 'Тариф 1'
        price = 790000
    elif plus == '2':
        plus1 = 'Тариф 2'
        price = 1990000


    title = 'Покупка'
    desc = f'Вы покупаете подписку: "{plus1}"'

    product = types.LabeledPrice(f'Подписка "{plus1}"', price)

    await bot.send_invoice(
        chat_id=userId,
        title=f'{title}',
        description=f'{desc}',
        payload=f'buysuccess-{plus}',
        provider_token=yoomoneyToken,
        start_parameter='invoice',
        currency='RUB',
        prices=[product],
        need_name=False,
        need_phone_number=False,
        need_email=False,
        is_flexible=False
    )

@dp.callback_query_handler(lambda c: c.data.startswith('buy'))
async def buy(call: types.CallbackQuery):
    id = call.data.split('-')[1]
    await sendinvoice(call.from_user.id, id)