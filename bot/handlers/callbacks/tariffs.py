from aiogram import types
from bot import dp, bot
from data import text
from ...keyboards import inlineKeyboards as inKey
from aiogram.types import InputMediaPhoto

@dp.callback_query_handler(text=['learnMore'])
async def learnMore(call: types.CallbackQuery):
    photo_1 = "AgACAgIAAxkBAAM2ZL7c8E5_ONTRN7WcGNk0-F1RS7kAAm3KMRvrnflJmgcx-nLGyyABAAMCAAN5AAMvBA"
    photo_2 = "AgACAgIAAxkBAAM3ZL7c8OJNCecFQlO_O9hnaw3HO4gAAm7KMRvrnflJiDzaxYLe3d4BAAMCAAN5AAMvBA"
    photo_3 = "AgACAgIAAxkBAAM4ZL7c8HaW5ZzZW-58Gk-iOfbSJtsAAm_KMRvrnflJ4LCU1byqZjMBAAMCAAN5AAMvBA"

    media = [
        InputMediaPhoto(media=photo_1),
        InputMediaPhoto(media=photo_2),
        InputMediaPhoto(media=photo_3)
    ]

    await bot.send_media_group(call.from_user.id, media=media)
    await bot.send_message(call.from_user.id, f'{text.tariffs(call)}', reply_markup=inKey.tariffs(call))
