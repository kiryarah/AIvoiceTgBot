# AIvoiceTgBot
### Телеграмм Бот - Голосовой ИИ помощник.
Бот понимает как головые, так и текстовые сообщения клиента и отвечает голосовыми сообщениями.<br>
За распознавание и синтез речи отвечает Yandex Speechkit.<br>
Ответы на вопросы клиента выполняет чат модель GPT "gpt-3.5-turbo".<br>
GPT модель можно поменять в файле "gpt_instruments/configure_gpt_model.py".<br>
Также можете задать настройки голоса и языка в speechkit_instruments/configure_speechkit_model.py.<br>
Документация тут (https://cloud.yandex.ru/docs/speechkit/stt/models) и тут (https://cloud.yandex.ru/docs/speechkit/tts/voices).

# Чтобы работало:
1. Вам нужен аккаунт в Yandex.Cloud, продукт Speechkit (https://cloud.yandex.ru/services/speechkit).<br>
   Далее читайте документацию, там последовательно все изложено. Создадите API-KEY и добавьте в переменные окружения.
2. Вам нужен аккаунт на сайте open.ai и также API-KEY.
3. Нужен API-KEY телеграмм бота, попросите у https://t.me/BotFather, при создании бота
Если не хотите добавлять в переменные окружения, можете напрямую указать в settings.py
