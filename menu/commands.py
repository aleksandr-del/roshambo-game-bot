#!/usr/bin/env python3

from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot) -> None:
    main_menu_commands = [
        BotCommand(command="/start", description="Запуск бота"),
        BotCommand(command="/help", description="Инструкция по использованию бота"),
    ]
    await bot.set_my_commands(main_menu_commands)
