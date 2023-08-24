from speechkit import model_repository
from speechkit.stt import AudioProcessingType


def get_recognition_model():
    model = model_repository.recognition_model()
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Full
    return model


def get_synthesis_model():
    model = model_repository.synthesis_model()
    model.voice = 'alena'
    model.role = 'good'
    return model
