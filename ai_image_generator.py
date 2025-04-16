# 
from openai import OpenAI
import requests
from config import OPENAI_API_KEY
import os
import uuid

client = OpenAI(api_key=OPENAI_API_KEY)

def gerar_imagem_fundo(prompt="futuristic technology background, neon circuits, dark tones"):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = response.data[0].url
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho_pasta = "backgrounds"
    os.makedirs(caminho_pasta, exist_ok=True)
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

    imagem = requests.get(image_url)
    with open(caminho_arquivo, "wb") as f:
        f.write(imagem.content)

    print(f"🧠 Imagem de fundo gerada: {caminho_arquivo}")
    return caminho_arquivo
