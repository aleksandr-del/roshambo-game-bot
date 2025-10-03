#!/usr/bin/env python3

import random
from lexicon.lexicon import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(("stone", "paper", "scissors"))


def _normalize_user_answer(user_answer: str) -> str:
    reverse_dict = {v: k for k, v in LEXICON_RU.items()}
    return reverse_dict[user_answer]


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {"stone": "scissors", "scissors": "paper", "paper": "stone"}
    if user_choice == bot_choice:
        return "nobody_won"
    return "user_won" if rules[user_choice] == bot_choice else "bot_won"
