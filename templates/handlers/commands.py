from typing import Any

from aiogram import types, Router
from aiogram.filters import Command

from templates.types import texts

router = Router()

@router.message(Command("start"))
async def start(message: types.Message) -> Any:
    await message.answer(texts["start"], parse_mode="HTML")