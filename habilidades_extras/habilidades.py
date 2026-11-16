# habilidades_extras/habilidades.py
import random
import webbrowser
import os
import re

def contar_piada(falar_func):
    """Seleciona uma piada e usa a função 'falar' fornecida para comunicá-la."""
    piadas = [
        "O que o pato falou para a pata? Vem quá!",
        "Por que a velhinha não usa relógio? Porque ela é uma senhora.",
        "Você conhece a piada do pônei? Pô nei eu...",
        "O que um cromossomo disse para o outro? Cromossomos felizes!"
    ]
    piada_escolhida = random.choice(piadas)
    falar_func(piada_escolhida)

def abrir_sites_e_programas(comando, falar_func):
    """Abre YouTube ou Calculadora e usa a função 'falar' para confirmar."""
    if "youtube" in comando:
        falar_func("Abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "calculadora" in comando:
        falar_func("Abrindo a calculadora.")
        os.system("start calc") # Comando para Windows
    else:
        falar_func("Desculpe, não sei como abrir isso.")

def calcular(comando, falar_func):
    """Resolve uma expressão matemática simples e usa a função 'falar' para dar o resultado."""
    try:
        # Padroniza a entrada: substitui palavras por operadores
        comando = comando.replace("mais", "+").replace("menos", "-").replace("vezes", "*").replace("dividido por", "/")
        
        # Regex aprimorado: procura por uma sequência que DEVE conter números,
        # junto com operadores e espaços.
        match = re.search(r'(\d[\s\d\.\+\-\*\/]+)', comando)
        
        if match:
            # Pega a expressão encontrada
            expressao = match.group(0)
            
            # Limpa espaços extras no início ou fim
            expressao_limpa = expressao.strip()
            
            print(f"[DEBUG] Expressão matemática encontrada: '{expressao_limpa}'")
            
            # Usa eval() para calcular o resultado da string
            # ATENÇÃO: eval() pode ser inseguro se a entrada não for controlada.
            # Aqui, é seguro pois nosso regex só permite números, operadores e espaços.
            resultado = eval(expressao_limpa)
            
            falar_func(f"O resultado é {resultado}")
        else:
            # Se o regex não encontrar nenhuma correspondência
            falar_func("Não encontrei uma expressão matemática clara no seu comando.")
            
    except Exception as e:
        # Captura erros de cálculo (ex: 5 / 0) ou outros problemas
        print(f"[DEBUG] Erro na função calcular: {e}")
        falar_func("Desculpe, não consegui calcular isso.")