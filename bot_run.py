from aiogram.utils import executor
from settings import DISPATCHER
from bot_instruments.handlers import register_handlers


register_handlers(DISPATCHER)

executor.start_polling(DISPATCHER, skip_updates=True)
