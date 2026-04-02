# ai-medical-form

🧠 AI Medical Text Processor
📌 Descrição

Este projeto transforma textos médicos não estruturados em informações organizadas usando Inteligência Artificial (LLM).

A aplicação recebe um texto clínico e retorna uma estrutura em formato JSON contendo:

Resumo clínico
Possíveis diagnósticos citados no texto
Condutas ou tratamentos mencionados
🚀 Tecnologias
Python
OpenAI API (GPT-4o-mini)
JSON
📂 Estrutura do projeto
app.py → arquivo principal (entrada do usuário)
ai_service.py → integração com o modelo de IA e processamento do texto
⚙️ Como executar
Instalar dependência:
pip install openai
Definir a chave da OpenAI:

Windows (PowerShell):
setx OPENAI_API_KEY "sua_chave_aqui"

Linux/Mac:
export OPENAI_API_KEY="sua_chave_aqui"

Rodar o projeto:
python app.py
🧪 Exemplo

Entrada:
Paciente relata dor de cabeça intensa há três dias, com sensibilidade à luz...

Saída:
{
"resumo_clinico": "Paciente com cefaleia intensa há 3 dias associada à fotossensibilidade",
"diagnosticos": ["enxaqueca"],
"condutas": ["repouso", "hidratação", "analgésico"]
}

🧠 Como funciona
Usuário digita um texto clínico
O sistema envia o texto para um modelo de linguagem (LLM)
O modelo retorna uma resposta estruturada em JSON
O sistema trata e exibe o resultado
Caso falhe, retorna uma resposta padrão
🔒 Regras do sistema
Não inventa informações
Usa apenas o que está no texto
Sempre retorna JSON válido
Estrutura fixa para consistência
🎯 Objetivo

Demonstrar capacidade de:

Uso de LLMs na prática
Extração de informação de texto não estruturado
Engenharia de prompt
Criação de soluções integráveis em sistemas reais
