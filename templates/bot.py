import os

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

from templates import Exceptions, throttling, handlers, scheduled
from templates.types import texts

from templates.run import Environment
Environment().load_env()

async def run() -> None:

    # configuring aiogram bot

    TOKEN = os.getenv("BOT_TOKEN")

    if TOKEN == None:
        raise Exceptions.TokenDoesNotDefined()

    bot = Bot(TOKEN)

    # configuring storage

    dp = Dispatcher(storage=MemoryStorage(), name="main")
    
    dp["dp"] = dp
    dp["texts"] = texts
    dp["bot"] = bot
    dp["bot_info"] = await bot.me()
        
    # Filters and middlewares only work for text messages
    # Setting up middleware for every message type:
    # inline, photo, sticker, etc. breaks middleware
    # because text message provides Message event type
    # but Sticker provides Update event type
    # https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html
    dp.message.middleware(throttling.AntiFloodMiddleware())
    
    for handler in handlers.handlers:
        dp.include_router(handler.router)
    
    await scheduled.build_scheduler(bot)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()