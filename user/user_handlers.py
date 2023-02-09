from aiogram import Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text, Command
import user.user_keyboards as KB
import user.user_DataBase as DB

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message):
    con = DB.Connect()
    try:
        con.register(message.from_user.id, message.from_user.username)
    except:
        con.db.close()
    await message.answer(
        'Hello!',
        reply_markup=KB.main()
    )