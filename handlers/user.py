#!/usr/bin/env python3


from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import yes_no_keyboard, game_keyboard
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner

user_router = Router(name=__name__)


@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=yes_no_keyboard)


@user_router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=yes_no_keyboard)


@user_router.message(F.text == LEXICON_RU["yes_button"])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"], reply_markup=game_keyboard)


@user_router.message(F.text == LEXICON_RU["no_button"])
async def process_no_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["no"],
    )


@user_router.message(
    F.text.in_((LEXICON_RU["stone"], LEXICON_RU["paper"], LEXICON_RU["scissors"]))
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} - {LEXICON_RU[bot_choice]}")
    winner = get_winner(message.text, bot_choice)
    message_effect_id = "5046509860389126442" if winner == "user_won" else None
    await message.answer(
        text=LEXICON_RU[winner],
        reply_markup=yes_no_keyboard,
        message_effect_id=message_effect_id,
    )
