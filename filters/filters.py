#!/usr/bin/env python3

from aiogram.types import Message
from aiogram.filters import BaseFilter


class UserFilter(BaseFilter):
    def __init__(self, user_ids: list[int], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_ids = user_ids

    async def __call__(self, message: Message):
        return message.from_user.id in self.user_ids
