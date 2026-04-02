import json
from openai import OpenAI

# Estrutura preparada para integração com LLMs e validação de saída estruturada
client = OpenAI(api_key="SUA_API_KEY_AQUI")


def analisar_texto(texto):
    prompt = f"""
Você é um assistente médico.

Analise o texto abaixo e retorne um JSON com exatamente esta estrutura:

{{
  "resumo_clinico": "string",
  "diagnosticos": ["string"],
  "condutas": ["string"]
}}

Regras:
- Responda APENAS com JSON válido
- Não adicione explicações
- Não use markdown
- Seja objetivo
- Não invente informações

Texto:
{texto}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        resposta = response.choices[0].message.content.strip()

        # Remove possíveis blocos ```json
        if resposta.startswith("```"):
            resposta = resposta.replace("```json", "").replace("```", "").strip()

        return json.loads(resposta)

    except Exception:
        return gerar_resposta_local(texto)


def gerar_resposta_local(texto):
    return {
        "resumo_clinico": f"Resumo baseado no texto: {texto[:80]}...",
        "diagnosticos": ["Possível condição identificada no texto"],
        "condutas": ["Análise clínica recomendada"]
    }