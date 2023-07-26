from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import dp, bot
import os

channelId = os.getenv('channelId')

def menu(message):
    main = InlineKeyboardMarkup()
    learnMore = InlineKeyboardButton("Узнать подробнее", callback_data="learnMore")
    main.add(learnMore)
    return main

def tariffs(call):
    main = InlineKeyboardMarkup()
    buy1 = InlineKeyboardButton("Приобрести Тариф 1", callback_data="buy-1")
    buy2 = InlineKeyboardButton("Приобрести Тариф 2", callback_data="buy-2")
    help = InlineKeyboardButton("Связаться с поддержкой", url='https://t.me/vitaecom_support')
    main.add(buy1)
    main.add(buy2)
    main.add(help)
    return main

async def urlChannel(message):
    invite_link = await bot.create_chat_invite_link(
        chat_id=channelId,
        member_limit=1
    )

    main = InlineKeyboardMarkup()
    url = InlineKeyboardButton("Ссылка", url=f'{invite_link.invite_link}')
    main.add(url)
    return main

def chatUser(message):
	main = InlineKeyboardMarkup()

	link_button = InlineKeyboardButton("Написать", url=f"tg://user?id={message.from_user.id}")

	main.add(link_button)
	return main
