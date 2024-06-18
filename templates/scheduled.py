from os import getenv

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from templates.const import EVERY

async def build_scheduler(bot: Bot):

    async def scheduled():
        await bot.send_message(
            chat_id=int(getenv("CHAT_ID")),
            text=f"<a href=\"tg://user?id={getenv('ID')}\">Шо ти?))</a>",
            parse_mode="HTML")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(scheduled, "interval", minutes=EVERY)
    scheduler.start()