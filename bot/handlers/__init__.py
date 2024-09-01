from . import users

from aiogram import Router

router = Router()

router.include_router(
    users.router
)