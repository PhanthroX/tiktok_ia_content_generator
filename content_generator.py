# content_generator.py
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def gerar_roteiro_carrossel():
    prompt = """
Você é um criador de conteúdo para TikTok focado em dicas e curiosidades de tecnologia que realmente agreguem para o usuário.
Então pesquise sempre as maiores tendências, novidades e dicas de tecnologia que possam ser úteis para o público jovem.
Você vai criar um roteiro para um vídeo curto de TikTok, com o objetivo de gerar engajamento e curiosidade. O vídeo deve ser dividido em 3 partes: gancho, explicação e chamada para ação.

Crie um roteiro dividido em 3 blocos, com linguagem leve, clara e que funcione bem em narração por voz. O objetivo é gerar vídeos curtos e envolventes.
Escolha um tema de tecnologia atual e interessante, como inteligência artificial, gadgets, aplicativos ou segurança digital. O conteúdo deve ser relevante e atrativo para o público jovem.
O vídeo deve ter entre 30 e 60 segundos de duração, com uma introdução que prenda a atenção, uma explicação clara e uma chamada para ação no final. O tom deve ser amigável e acessível, como se você estivesse conversando com um amigo.

Estrutura do conteúdo:

Slide 1 (Gancho):
- Comece com uma pergunta intrigante, um fato surpreendente ou uma frase impactante.
- A função desse slide é prender a atenção nos 2 primeiros segundos.
- Aqui você pode usar uma pergunta retórica ou uma afirmação que faça a pessoa querer saber mais.
- Evite clichês ou frases genéricas. Foque em algo que realmente chame a atenção.

Slide 2 (Explicação):
- Apresente o tema escolhido de forma clara e direta.
- Evite conteúdo bobo ou clichê. Foque em algo que realmente chame a atenção.
- Use uma linguagem simples e acessível, como se estivesse explicando para um amigo.
- Se for algo histórico, traga o “uau” do passado. Se for uma novidade, destaque por que isso importa, se for dica deve ser uma dica que realmente importe.
- Evite termos técnicos ou frases genéricas.
- Se fizer uma pergunta no Slide 1, responda aqui.

Slide 3 (Chamada para ação):
- Convide a pessoa a seguir para ver mais conteúdos como esse.
- Pode ser divertido, criativo ou até misterioso — mas natural.

Importante:
- Use frases curtas e com ritmo de fala natural.
- Não inclua emojis, hashtags ou frases escritas como se fosse legenda de post.
- A ideia é que esse roteiro seja lido em voz alta por uma IA de narração.
- Evite clichês, publi disfarçada ou frases genéricas.. Seja direto, interessante e original.

Formato de saída:
Slide 1: ...
Slide 2: ...
Slide 3: ...
"""



    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.85,
        max_tokens=300
    )

    return response.choices[0].message.content
