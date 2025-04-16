from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip
import os

def criar_video(slide_path, audio_narracao, nome_saida="video.mp4", trilha_fundo="audio_base/musica_fundo.mp3", duracao_padrao=6):
    try:
        imagem = ImageClip(slide_path).set_duration(duracao_padrao)
        imagem = imagem.resize(height=1920).resize(width=1080)

        narracao = AudioFileClip(audio_narracao)

        if os.path.exists(trilha_fundo):
            musica = AudioFileClip(trilha_fundo).subclip(0, narracao.duration).volumex(0.1)
            audio_final = CompositeAudioClip([musica, narracao])
        else:
            audio_final = narracao

        imagem = imagem.set_audio(audio_final).set_duration(narracao.duration)
        video = CompositeVideoClip([imagem])
        os.makedirs("videos", exist_ok=True)
        caminho = os.path.join("videos", nome_saida)
        video.write_videofile(caminho, fps=24, codec='libx264', audio_codec='aac')

        print(f"🎬 Vídeo gerado: {caminho}")
    except Exception as e:
        print(f"Erro ao criar vídeo: {e}")
