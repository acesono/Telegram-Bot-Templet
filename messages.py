from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from aiogram.enums.parse_mode import ParseMode
from texts import *


async def main_message(message):
    button = ReplyKeyboardBuilder()
    button.add(KeyboardButton(text='button 1'))
    button.add(KeyboardButton(text='button 2'))
    button.adjust(2)
    await message.answer('Choose a language / ቋንቋ ምረጥ',reply_markup=button.as_markup(resize_keyboard=True))
