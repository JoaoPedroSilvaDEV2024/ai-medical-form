# ai-medical-form

# 🧠 AI Medical Text Processor

## 📌 Descrição

Este projeto transforma textos clínicos não estruturados em informações organizadas utilizando um modelo de linguagem (LLM).

A aplicação recebe um relato médico e retorna um JSON contendo:

* Resumo clínico
* Possíveis diagnósticos
* Condutas/tratamentos

---

## 🚀 Tecnologias

* Python
* OpenAI API

---

## ⚙️ Como executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/ai-medical-form.git
```

2. Instale as dependências:

```
pip install openai
```

3. Configure sua API Key no arquivo `ai_service.py`:

```python
client = OpenAI(api_key="SUA_API_KEY_AQUI")
```

4. Execute:

```
python app.py
```

---

## 🧠 Uso de IA

A solução utiliza um modelo de linguagem para interpretar o texto clínico e gerar uma saída estruturada em JSON.

O prompt foi projetado para:

* Garantir formato consistente
* Evitar respostas fora do contexto
* Manter objetividade

Também foi implementado tratamento de erro e fallback local, garantindo funcionamento mesmo sem acesso à API.

---

## 🛡️ Redução de riscos

Para reduzir o risco de informações incorretas:

* Uso de prompts restritivos
* Limitação ao conteúdo do texto
* Validação do formato da resposta
* Possibilidade de revisão humana

Como evolução, pode-se aplicar RAG com fontes confiáveis.

---

## 🔗 Integração

A solução pode ser integrada como um serviço backend:

1. O sistema envia o texto da consulta
2. A API processa via LLM
3. Retorna JSON estruturado
4. O sistema consome para exibição ou armazenamento

---

## 🚀 Melhorias futuras

* Integração com banco de dados
* Uso de RAG com histórico do paciente
* Interface web
* Monitoramento de respostas

---

## 📌 Observações

A arquitetura foi pensada para ser simples, modular e facilmente integrável a sistemas reais.
