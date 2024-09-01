from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="start",
                   description="Запуск/Перезапуск бота"),
    ]

    await bot.set_my_commands(commands)
