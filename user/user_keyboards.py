from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def main():
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="User button", callback_data='#'))
    return kb.as_markup()
