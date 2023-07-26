from aiogram import types
from bot import dp
from ...keyboards import inlineKeyboards as inKey
from ...keyboards import replyKeyboards as repKey
from data import text, db

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if not db.getUsersExist(message.from_user.id):
        db.addUser(message.from_user.id, message.from_user.full_name)

    await message.reply(f'{text.start(message)}', reply_markup=inKey.menu(message))
