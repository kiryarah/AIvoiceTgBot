from .configure_speechkit_model import get_recognition_model, get_synthesis_model


def recognize(audio):
    result = get_recognition_model().transcribe(audio)
    return result[0].normalized_text


def synthesize(text):
    raw_voice = get_synthesis_model().synthesize(text, raw_format=True)
    return raw_voice
