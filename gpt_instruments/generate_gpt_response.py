from .configure_gpt_model import get_gpt_model


def gen_gpt_response(content: str) -> str:
    response = get_gpt_model(content)
    return response['choices'][0]['message']['content']
