# ai-medical-form

🧠 AI Medical Form Processor
📌 Descrição

Este projeto recebe um texto clínico (como anotações médicas ou relatos de pacientes) e utiliza um modelo de inteligência artificial (OpenAI GPT) para transformar esse texto em informações estruturadas no formato JSON.

O sistema extrai automaticamente:

Um resumo clínico do caso
Possíveis diagnósticos citados no texto
Condutas ou tratamentos mencionados

O objetivo é demonstrar como a IA pode ser usada para organizar informações não estruturadas e facilitar o uso em sistemas reais.

⚙️ Funcionalidades
Entrada de texto via terminal
Processamento usando modelo de linguagem (LLM)
Extração de informações médicas estruturadas
Retorno em formato JSON consistente
Sistema de fallback em caso de erro na API
Tratamento básico de exceções
🧠 Tecnologias utilizadas
Python 3
OpenAI API (GPT-4o-mini)
JSON
Variáveis de ambiente
📂 Estrutura do projeto

O projeto é dividido em dois arquivos principais:

app.py → responsável pela entrada de dados e exibição do resultado
ai_service.py → responsável pela integração com a IA e processamento do texto
🚀 Como executar o projeto

Primeiro, clone o repositório para sua máquina.
Depois instale a dependência da OpenAI com pip install openai.

Em seguida, configure sua chave da OpenAI em uma variável de ambiente chamada OPENAI_API_KEY.

No Windows, use setx OPENAI_API_KEY "sua_chave_aqui".
No Linux ou Mac, use export OPENAI_API_KEY="sua_chave_aqui".

Por fim, execute o projeto com python app.py.

🧪 Exemplo de uso

Entrada:
Paciente relata dor de cabeça intensa há três dias, associada à sensibilidade à luz. Nega febre. Possui histórico de enxaqueca. Foi orientado repouso, hidratação e prescrito analgésico.

Saída esperada:
{
"resumo_clinico": "Paciente com cefaleia intensa associada à fotofobia e histórico de enxaqueca.",
"diagnosticos": ["Enxaqueca"],
"condutas": ["Repouso", "Hidratação", "Analgésico"]
}

🏗️ Arquitetura

O sistema funciona de forma simples:

O app.py recebe o texto do usuário.
O ai_service.py envia esse texto para a OpenAI e processa a resposta.
A API retorna um JSON estruturado com as informações extraídas.

🎯 Objetivo do projeto

Este projeto tem como objetivo demonstrar habilidades em:

Uso de inteligência artificial (LLMs)
Engenharia de prompts
Transformação de texto em dados estruturados
Organização de código backend
Aplicação prática de IA em sistemas reais
⚠️ Observação importante

Este sistema não substitui análise médica profissional.
Ele é apenas uma demonstração técnica de uso de IA aplicada à organização de dados clínicos.

👨‍💻 Autor

Projeto desenvolvido para fins de estudo e demonstração de integração de IA em sistemas reais.
