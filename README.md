# ai-medical-form

# 🧠 AI Medical Form Processor

Sistema de processamento de textos clínicos utilizando Inteligência Artificial (LLM) para extração estruturada de informações médicas.

---

## 📌 Descrição

Este projeto recebe um texto clínico (como anotações médicas ou relatos de pacientes) e utiliza um modelo de linguagem (OpenAI GPT) para gerar uma saída estruturada em JSON.

A saída contém:

- Resumo clínico do caso
- Possíveis diagnósticos citados
- Condutas ou tratamentos mencionados

O objetivo é demonstrar como IA pode ser aplicada para organização e estruturação de informações em sistemas reais de saúde.

---

## ⚙️ Funcionalidades

- Entrada de texto clínico via terminal
- Processamento com LLM (OpenAI GPT-4o-mini)
- Extração estruturada de informações médicas
- Retorno em formato JSON consistente
- Fallback local em caso de falha da API
- Tratamento básico de erros e resposta inválida

---

## 🧠 Tecnologias utilizadas

- Python 3
- OpenAI API (GPT-4o-mini)
- JSON
- Variáveis de ambiente (.env recomendado)

---

## 📂 Estrutura do projeto
.
├── app.py # Interface principal (input/output)
├── ai_service.py # Integração com LLM e lógica de IA
└── README.md

---

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto

2. Instale as dependências
