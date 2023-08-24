from aiogram import types
from aiogram.utils import executor
from settings import BOT, DISPATCHER
from client_message_service import get_gpt_voice_response, convert_voice_to_text
from io import BytesIO


GREETING = '''
Привет. Я твой новый голосовой ИИ друг.
Я умею принимать твои голосовые сообщения,
а также умею отвечать голосовыми сообщениями.
Единственное, я пока не умею вести диалог.
Давай попробуем. Задавай вопрос.
'''


@DISPATCHER.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    await message.answer(GREETING)


@DISPATCHER.message_handler()
async def echo_send(message: types.Message):
    '''
    Обработчик текстового запроса клиента.
    Бот отвечет голосовым сообщением
    '''
    await message.answer('Еще учусь. Дай подумаю...')
    await BOT.send_voice(
        chat_id=message.from_user.id,
        voice=get_gpt_voice_response(text=message.text)
    )


@DISPATCHER.message_handler(content_types=[types.ContentType.VOICE])
async def voice_message_handler(message: types.Message):
    '''
    Обработчик голосового запроса клиента.
    Бот отвечет голосовым сообщением
    '''
    voice = await _save_voice_to_bytes(message.voice)

    await message.answer('Еще учусь. Дай подумаю...')
    await BOT.send_voice(
        chat_id=message.from_user.id,
        voice=get_gpt_voice_response(text=convert_voice_to_text(voice))
    )


async def _save_voice_to_bytes(voice: types.Voice) -> bytes:
    '''
    Записывает голос в поток и возвращает набор байт
    '''
    bytestream = BytesIO()
    voice_file = await voice.get_file()
    await voice_file.download(destination_file=bytestream)
    return bytestream.getvalue()

executor.start_polling(DISPATCHER, skip_updates=True)
