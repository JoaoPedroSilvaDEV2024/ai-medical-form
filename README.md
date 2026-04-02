# ai-medical-form

# 🧠 AI Medical Text Processor

## 📌 Visão Geral

Este projeto implementa um sistema de processamento de linguagem natural aplicado ao contexto médico, utilizando um modelo de linguagem (LLM) para estruturar informações clínicas a partir de texto livre.

O objetivo é transformar relatos médicos não estruturados em dados organizados, facilitando análise, registro e integração com sistemas de saúde.

---

## 🚀 Funcionalidades

A aplicação recebe um texto clínico e retorna uma estrutura em JSON contendo:

- Resumo clínico do caso
- Possíveis diagnósticos citados no texto
- Condutas e tratamentos mencionados

---

## 🧠 Abordagem Técnica

O sistema utiliza engenharia de prompt para orientar o modelo de linguagem a:

- Extrair apenas informações explícitas do texto
- Evitar alucinações (não inventar dados)
- Retornar resposta exclusivamente em JSON válido
- Manter estrutura consistente de saída

Em caso de falha na geração da resposta, o sistema utiliza um fallback local para garantir robustez.

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- OpenAI API (GPT-4o-mini)
- JSON para estruturação de dados
- Variáveis de ambiente para segurança da API Key

---

## 📂 Estrutura do Projeto

- app.py → ponto de entrada da aplicação (input do usuário e exibição da resposta)
- ai_service.py → camada de integração com LLM e processamento do texto clínico

---

## 🔁 Fluxo da Aplicação

1. Usuário insere texto clínico
2. O sistema monta um prompt estruturado
3. O texto é enviado ao modelo de linguagem
4. O modelo retorna um JSON estruturado
5. O sistema valida e converte a resposta
6. Resultado é exibido ao usuário

---

## 🧪 Exemplo

### Entrada:
Paciente relata dor de cabeça intensa há três dias, associada à sensibilidade à luz. Nega febre. Possui histórico de enxaqueca. Foi orientado repouso, hidratação e prescrito analgésico.

### Saída:
```json
{
  "resumo_clinico": "Paciente com cefaleia intensa há 3 dias associada à fotossensibilidade, sem febre, com histórico de enxaqueca.",
  "diagnosticos": ["enxaqueca"],
  "condutas": ["repouso", "hidratação", "analgésico"]
}

## 🔒 Garantias do Sistema
- Uso exclusivo de informações presentes no texto
- Saída sempre estruturada em JSON válido
- Controle de aleatoriedade (temperature = 0)
- Redução de respostas inconsistentes via prompt engineering

## 🧩 Possíveis Evoluções
- Integração com bancos de dados médicos
- Uso de RAG (Retrieval Augmented Generation)
- Versionamento de prompts
- Interface web para profissionais da saúde
- Logs e monitoramento de respostas do modelo

## 🎯 Objetivo do Projeto
Demonstrar capacidade em:
- Integração com LLMs em aplicações reais
- Engenharia de prompt aplicada
- Estruturação de dados a partir de texto não estruturado
- Construção de pipelines simples de IA
- Boas práticas de software (organização, fallback, modularização)

## 👨‍💻 Observação
Este projeto foi desenvolvido com foco em clareza de arquitetura, aplicação prática de IA generativa e simulação de uso em sistemas reais de saúde.
