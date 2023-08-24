from gpt_instruments.generate_gpt_response import gen_gpt_response
from speechkit_instruments.generate_speech import synthesize, recognize


def get_gpt_voice_response(text: str) -> bytes:
    gpt_response = gen_gpt_response(text)
    return convert_text_to_voice(text=gpt_response)


def convert_voice_to_text(voice: bytes) -> str:
    return recognize(voice)


def convert_text_to_voice(text: str) -> bytes:
    return synthesize(text=text)
