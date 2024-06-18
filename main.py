import asyncio
import templates.bot
import logging, sys

async def main():    
    
    if "--log-file" in sys.argv:
        logging.basicConfig(filename="main.log", encoding="utf-8", level=logging.INFO)
    else: logging.basicConfig(level=logging.INFO)

    await templates.bot.run()

if __name__ == "__main__":

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.critical("Bye!")