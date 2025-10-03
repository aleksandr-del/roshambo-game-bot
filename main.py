#!/usr/bin/env python3

import asyncio
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import user_router, other_router
from config.config import Config, load_config
from filters.filters import UserFilter


async def main():
    config: Config = load_config(".env")
    bot = Bot(
        token=config.bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    dp.message.filter(UserFilter(config.bot.user_ids))
    dp.include_routers(user_router, other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
