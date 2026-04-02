import json
from ai_service import analisar_texto

if __name__ == "__main__":
    texto = input("Digite o texto da consulta: ")

    resultado = analisar_texto(texto)

    print("\nResultado estruturado:")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))