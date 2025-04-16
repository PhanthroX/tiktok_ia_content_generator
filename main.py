from content_generator import gerar_roteiro_carrossel
from image_generator import criar_imagem_slide
from history_manager import salvar_conteudo, ja_foi_usado
from voice_generator import gerar_audio
from video_generator import criar_video
from video_merger import juntar_videos
import os

def parsear_roteiro(roteiro):
    slides = {}
    for linha in roteiro.strip().split("\n"):
        if linha.startswith("Slide"):
            chave, texto = linha.split(":", 1)
            slides[chave.strip()] = texto.strip()
    return slides

def gerar_conteudo_unico(max_tentativas=5):
    for tentativa in range(max_tentativas):
        print(f"🌀 Tentativa {tentativa + 1} de {max_tentativas}")
        roteiro = gerar_roteiro_carrossel()
        slides = parsear_roteiro(roteiro)
        slide2 = slides.get("Slide 2", "")
        if not ja_foi_usado(slide2):
            salvar_conteudo(slide2)
            return slides
        else:
            print("⚠️ Conteúdo repetido. Tentando outro...")
    raise Exception("❌ Não foi possível gerar conteúdo novo após várias tentativas.")

def main():
    slides = gerar_conteudo_unico()

    imagens_fixas = [
        "backgrounds/imagem_1.png",
        "backgrounds/imagem_2.png",
        "backgrounds/imagem_3.png"
    ]

    os.makedirs("videos", exist_ok=True)
    os.makedirs("audio", exist_ok=True)

    clipes_temp = []

    for i, slide in enumerate(["Slide 1", "Slide 2", "Slide 3"]):
        texto = slides[slide]
        nome_imagem = f"carrossel/slide{i+1}.png"
        nome_audio = os.path.join("audio", f"audio{i+1}.mp3")
        nome_video = f"temp_video{i+1}.mp4"

        criar_imagem_slide(texto, nome_imagem, imagens_fixas[i])
        gerar_audio(texto, nome_audio)
        criar_video(nome_imagem, nome_audio, nome_video)

        clipes_temp.append(os.path.join("videos", nome_video))

    juntar_videos(clipes_temp, output_path="videos/final_video.mp4")

if __name__ == "__main__":
    main()
