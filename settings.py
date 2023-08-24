from speechkit import configure_credentials, creds
from aiogram import Bot, Dispatcher
import openai
import os


# yandex speechkit settings
def configure_speechkit() -> None:
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key=os.getenv('YA_API_KEY')
        )
    )


# openAI settings
def configure_openai() -> None:
    openai.api_key = os.getenv('GPT_API_KEY')


# TGBot settings
BOT = Bot(token=os.getenv('BOT_API_KEY'))
DISPATCHER = Dispatcher(BOT)
