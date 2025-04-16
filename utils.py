def salvar_post_em_txt(conteudo, nome_arquivo="post_tiktok.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"✅ Post salvo em {nome_arquivo}")
