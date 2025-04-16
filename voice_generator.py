from gtts import gTTS
import os

def gerar_audio(texto, nome_arquivo):
    try:
        tts = gTTS(text=texto, lang='pt', slow=False)
        tts.save(nome_arquivo)
        print(f"🔊 Áudio salvo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
