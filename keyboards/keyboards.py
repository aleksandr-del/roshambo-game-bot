#!/usr/bin/env python3

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

yes_button = KeyboardButton(text=LEXICON_RU["yes_button"])
no_button = KeyboardButton(text=LEXICON_RU["no_button"])
yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(yes_button, no_button, width=2)
yes_no_keyboard: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    resize_keyboard=True, one_time_keyboard=True
)

stone_button = KeyboardButton(text=LEXICON_RU["stone"])
scissors_button = KeyboardButton(text=LEXICON_RU["scissors"])
paper_button = KeyboardButton(text=LEXICON_RU["paper"])
game_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [stone_button],
        [scissors_button],
        [paper_button],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
