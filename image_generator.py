from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling
from config import IMG_WIDTH, IMG_HEIGHT, FONT_PATH, FONT_SIZE
import os

def criar_imagem_slide(texto, nome_arquivo, caminho_fundo):
    img = Image.open(caminho_fundo).convert("RGB").resize((IMG_WIDTH, IMG_HEIGHT), Resampling.LANCZOS)

    overlay = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), (0, 0, 0))
    blended = Image.blend(img, overlay, alpha=0.4)

    draw = ImageDraw.Draw(blended)
    fonte = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    linhas = []
    palavras = texto.split()
    linha = ""
    for palavra in palavras:
        if draw.textlength(linha + " " + palavra, font=fonte) < IMG_WIDTH - 100:
            linha += " " + palavra
        else:
            linhas.append(linha.strip())
            linha = palavra
    linhas.append(linha.strip())

    y_text = (IMG_HEIGHT - (len(linhas) * FONT_SIZE)) // 2
    for linha in linhas:
        largura_texto = draw.textlength(linha, font=fonte)
        x_text = (IMG_WIDTH - largura_texto) // 2
        draw.text((x_text, y_text), linha, font=fonte, fill=(255, 255, 255))
        y_text += FONT_SIZE + 10

    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    blended.save(nome_arquivo)
    print(f"✅ Slide salvo: {nome_arquivo}")
