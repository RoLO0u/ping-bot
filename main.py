import asyncio
import templates.bot
import logging

async def main():    
    
    logging.basicConfig(level=logging.INFO)

    await templates.bot.run()

if __name__ == "__main__":

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.critical("Bye!")