import settings
import asyncio
from aiogram import Bot, Dispatcher

import user.user_handlers as user_handlers

bot = Bot(token=settings.Bot)
dp = Dispatcher()


async def main():
    #add router
    dp.include_router(user_handlers.router)

    #disables the event handler when the bot is turned off
    await bot.delete_webhook(drop_pending_updates=True)

    #turning on the endless work of the bot
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
