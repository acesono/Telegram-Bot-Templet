from aiogram import Bot, Dispatcher, types, F
import logging
import asyncio
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from messages import *
from filters import custom_filter


TOKEN=''
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
    STATES = State()

@dp.message(Command("start"))
async def command_handler(message: types.Message):
    pass

@dp.message()
async def message_handler(message: types.Message):
    pass
    
@dp.callback_query()
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    pass

@dp.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery):
    pass

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
