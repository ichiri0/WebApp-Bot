from aiogram import Router
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio

from bot.keyboards import start as start_keyboards
from bot.keyboards.start import MyCallback

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):

    inline_markup = await start_keyboards.get_start_keyboard_inline()
    await message.answer("Привет! По кнопке ниже ты сможешь открыть приложени!", reply_markup=inline_markup)

