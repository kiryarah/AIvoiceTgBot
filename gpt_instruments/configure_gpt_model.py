import openai

MODEL = 'gpt-3.5-turbo'


def get_gpt_model(content):
    model = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{'role': 'user', 'content': content}]
    )
    return model
