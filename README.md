🚀 TikTok Tech Content Automation
    Projeto completo de automação para geração de vídeos curtos com curiosidades, dicas e novidades de tecnologia, ideal para plataformas como TikTok, Reels e Shorts.

🧠 Visão geral
    Este projeto utiliza Python + IA (OpenAI) para gerar roteiros dinâmicos, criar imagens temáticas, sintetizar narrações com voz e montar vídeos prontos para publicação — tudo de forma autônoma, modular e escalável.

✨ Funcionalidades
    🔁 Geração automatizada de conteúdo com roteiros em 3 blocos: Gancho, Explicação e Call to Action

    🎨 Criação de imagens com IA ou templates fixos

    🎙️ Narração por voz com gTTS (Text-to-Speech)

    🎬 Composição de vídeos com MoviePy

    📥 Organização de mídia em pastas dedicadas

    ✅ Geração de vídeo final otimizado para TikTok (1080x1920)


🧩  Estrutura modular

    Módulo	Responsabilidade
    main.py	Orquestra a execução total do processo
    content_generator.py	Gera roteiros com inteligência artificial
    image_generator.py	Cria slides baseados no texto
    voice_generator.py	Gera narração em áudio usando gTTS
    video_generator.py	Compõe vídeos slide+áudio
    video_merger.py	Junta os vídeos temporários em um único arquivo final
    history_manager.py	Evita repetições de conteúdo previamente gerado

⚙️ Como rodar o projeto
Observação: A lib moviepy não estava rodando corretamente com o .editor. Desta forma, instalei a versão mais antiga para rodar e descobri que a pillow também deveria ser uma versão antiga. Entretanto, ambas não rodavam com o python 3.13.x. Então, o projeto foi desenvolvido com python 3.10.x.

Instale as dependências:
    pip install -r requirements.txt

Configure sua chave de API no ambiente:
    export OPENAI_API_KEY=your_key_here

Rode o projeto:
    python main.py