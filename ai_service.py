import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analisar_texto(texto: str):
    prompt = f"""
Você é um assistente de extração de informações clínicas.

Sua tarefa é analisar o texto médico abaixo e retornar SOMENTE um JSON válido.

IMPORTANTE:
- Use APENAS informações explícitas do texto
- NÃO invente dados
- Se não houver informação, retorne lista vazia []
- NÃO inclua explicações, comentários ou markdown

Formato obrigatório da resposta:

{{
  "resumo_clinico": "string curta resumindo o caso",
  "diagnosticos": ["possíveis diagnósticos citados no texto"],
  "condutas": ["tratamentos ou condutas mencionadas"]
}}

Texto do paciente:
\"\"\"{texto}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você retorna apenas JSON válido."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        resposta = response.choices[0].message.content.strip()

        # Remove possíveis blocos de código
        if "```" in resposta:
            resposta = resposta.replace("```json", "").replace("```", "").strip()

        return json.loads(resposta)

    except Exception:
        return gerar_resposta_local(texto)


def gerar_resposta_local(texto: str):
    return {
        "resumo_clinico": "Falha na análise automática. Resumo parcial gerado.",
        "diagnosticos": [],
        "condutas": []
    }