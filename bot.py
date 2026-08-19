import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)


BOT_TOKEN = os.environ["BOT_TOKEN"]

WEB_APP_URL = os.environ["WEB_APP_URL"]


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):

    telegram_id = message.from_user.id

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 Открыть сайт",
                    web_app=WebAppInfo(
                        url=f"{WEB_APP_URL}/?telegram_id={telegram_id}"
                    )
                )
            ]
        ]
    )

    await message.answer(
        "Откройте сайт. При посещении фиксируется IP-адрес подключения.",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
