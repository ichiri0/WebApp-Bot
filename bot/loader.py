import contextlib
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from bot.config.data_config import BOT_TOKEN
from bot.utils.notify_admins import on_startup_notify, on_shutdown_notify
from bot.utils.set_bot_commands import set_default_commands
from bot import handlers



async def on_startup(bot: Bot):
    await set_default_commands(bot)
    await on_startup_notify(bot)


async def on_shutdown(bot: Bot):
    await on_shutdown_notify(bot)


async def start():

    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(
        handlers.router
    )
    try:
        with contextlib.suppress(KeyboardInterrupt, SystemExit):
            await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        await bot.session.close()
