#!/usr/bin/env python3

from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon import LEXICON_RU

other_router = Router(name=__name__)


@other_router.message()
async def process_other(message: Message):
    await message.answer(text=LEXICON_RU["other_answer"])
