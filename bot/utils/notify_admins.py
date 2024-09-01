import logging
from aiogram import Bot
from bot.config.data_config import ADMINS


async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "✅ Произошёл запуск бота")
        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "⛔ Произошла остановка бота")
        except Exception as err:
            logging.exception(err)
