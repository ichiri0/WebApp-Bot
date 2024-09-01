from typing import List, Optional
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types
from aiogram.filters.callback_data import CallbackData

from bot.utils.web_client.web_apps import WebAppsService
from bot.config.data_config import WEBAPP_URL 

class MyCallback(CallbackData, prefix="my_callback"):
    action: str
    message_id: int


async def get_start_keyboard_inline():

    web_app_service = WebAppsService()

    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(text="Открыть",
                                    web_app=types.web_app_info.WebAppInfo(url=WEBAPP_URL)),
    )
    markup = types.InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


async def get_keyboard(kb_text: str) -> Optional[types.ReplyKeyboardMarkup]:
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(
            text=kb_text
        )
    )
    return types.ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True, row_width=3)


