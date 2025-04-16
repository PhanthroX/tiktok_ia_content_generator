import os

HISTORICO_PATH = "carrossel/historico.txt"

def salvar_conteudo(texto_slide2):
    with open(HISTORICO_PATH, "a", encoding="utf-8") as f:
        f.write(texto_slide2.strip() + "\n")

def ja_foi_usado(texto_slide2):
    if not os.path.exists(HISTORICO_PATH):
        return False
    with open(HISTORICO_PATH, "r", encoding="utf-8") as f:
        return texto_slide2.strip() in [linha.strip() for linha in f.readlines()]
