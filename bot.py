import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Welcome to Show Kali!\n\n"
        "Choose your subscription:\n\n"
        "💎 1 Week - KES 199\n"
        "💎 2 Weeks - KES 399\n"
        "💎 1 Month - KES 499\n"
        "💎 6 Months - KES 1,599\n"
        "💎 1 Year - KES 3,999\n\n"
        "Reply with the plan you want."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
