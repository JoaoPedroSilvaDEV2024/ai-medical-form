# ai-medical-form

# 🧠 AI Medical Text Processor

## 📌 Descrição

Este projeto transforma textos clínicos não estruturados em informações organizadas, simulando o uso de um modelo de linguagem (LLM).

A aplicação recebe um relato médico e retorna um JSON contendo:

* Resumo clínico
* Possíveis diagnósticos
* Condutas/tratamentos

---

## 🚀 Tecnologias

* Python
* Estrutura preparada para integração com LLM (OpenAI, Anthropic, etc)

---

## ⚙️ Como executar

1. Clone o repositório:

```
git clone https://github.com/JoaoPedroSilvaDEV2024/ai-medical-form.git
```

2. Instale as dependências:

```
pip install openai
```

3. Execute:

```
python app.py
```

---

## 🧠 Uso de IA

A solução foi projetada para utilizar um modelo de linguagem (LLM) na análise de textos clínicos.

O prompt foi estruturado para:

* Garantir saída em JSON válido
* Evitar informações fora do contexto
* Manter objetividade

A arquitetura permite integração direta com APIs como OpenAI.

---

## ⚠️ Observação importante

A integração com LLM está implementada na estrutura do código, porém foi utilizado um fallback local para simulação das respostas, evitando dependência de quota de API.

Em um ambiente real, a função pode ser facilmente conectada a um modelo de linguagem externo.

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
2. O serviço processa os dados
3. Retorna JSON estruturado
4. O sistema consome para exibição ou armazenamento

---

## 🚀 Melhorias futuras

* Integração real com LLM
* Uso de RAG com histórico do paciente
* Integração com banco de dados
* Interface web
* Monitoramento de respostas

---

## 📌 Observações finais

A arquitetura foi pensada para ser simples, modular e facilmente adaptável para uso em sistemas reais, com foco em confiabilidade e escalabilidade.
