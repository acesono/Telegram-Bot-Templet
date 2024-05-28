from aiogram.filters import Filter
from aiogram import types


class custom_filter(Filter):
    async def __call__(self,message: types.message) -> bool:
        return 
        
