"""
Calculadora Turbo em Python (Terminal Colorido com ANSI + Histórico)
Autor: Projeto Educativo
Objetivo: Ensinar códigos ANSI de cores, estrutura de listas em Python e novas operações (potência e raiz).
Executar: python python/calculadora_turbo.py
"""

import math

# Códigos de cores ANSI (funcionam em qualquer terminal moderno)
COR_RESET = "\033[0m"
COR_TITULO = "\033[1;36m"
COR_MENU = "\033[0;33m"
COR_SUCESSO = "\033[1;32m"
COR_ERRO = "\033[1;31m"
COR_DESTAQUE = "\033[1;35m"


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(a)


def pedir_numero(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print(f"{COR_ERRO}⚠️  Entrada inválida! Digite apenas números.{COR_RESET}")


def exibir_menu():
    print(f"\n{COR_TITULO}========================================{COR_RESET}")
    print(f"{COR_TITULO}      CALCULADORA TURBO EM PYTHON       {COR_RESET}")
    print(f"{COR_TITULO}========================================{COR_RESET}")
    print(f"{COR_MENU}1 - Somar (+)")
    print(f"2 - Subtrair (-)")
    print(f"3 - Multiplicar (*)")
    print(f"4 - Dividir (/)")
    print(f"5 - Potência (a ** b)")
    print(f"6 - Raiz Quadrada (√)")
    print(f"7 - Ver Histórico de Cálculos")
    print(f"0 - Sair{COR_RESET}")
    print(f"{COR_TITULO}----------------------------------------{COR_RESET}")


def main():
    historico = []
    print(f"{COR_SUCESSO}Calculadora iniciada com sucesso!{COR_RESET}")

    while True:
        exibir_menu()
        opcao = input(f"{COR_DESTAQUE}Escolha uma opção (0 a 7): {COR_RESET}").strip()

        if opcao == "0":
            print(f"\n{COR_SUCESSO}Obrigado por usar a calculadora! Até logo! 👋{COR_RESET}")
            break

        if opcao == "7":
            print(f"\n{COR_DESTAQUE}=== HISTÓRICO DE CÁLCULOS ==={COR_RESET}")
            if not historico:
                print("Nenhum cálculo recente ainda nesta sessão.")
            else:
                for idx, item in enumerate(historico, 1):
                    print(f"[{idx}] {item}")
            continue

        if opcao not in ("1", "2", "3", "4", "5", "6"):
            print(f"{COR_ERRO}⚠️  Opção inválida! Escolha um número de 0 a 7.{COR_RESET}")
            continue

        if opcao == "6":
            try:
                num = pedir_numero("Digite o número para extrair a raiz quadrada: ")
                resultado = raiz_quadrada(num)
                registro = f"√{num} = {resultado:.2f}"
                historico.append(registro)
                print(f"\n{COR_SUCESSO}✓ Resultado: {registro}{COR_RESET}")
            except ValueError as erro:
                print(f"{COR_ERRO}⚠️  Erro: {erro}{COR_RESET}")
            continue

        num1 = pedir_numero("Digite o 1º número: ")
        num2 = pedir_numero("Digite o 2º número: ")

        try:
            if opcao == "1":
                resultado = somar(num1, num2)
                operacao_str = f"{num1} + {num2} = {resultado:.2f}"
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                operacao_str = f"{num1} - {num2} = {resultado:.2f}"
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                operacao_str = f"{num1} * {num2} = {resultado:.2f}"
            elif opcao == "4":
                resultado = dividir(num1, num2)
                operacao_str = f"{num1} / {num2} = {resultado:.2f}"
            elif opcao == "5":
                resultado = potencia(num1, num2)
                operacao_str = f"{num1} ** {num2} = {resultado:.2f}"

            historico.append(operacao_str)
            print(f"\n{COR_SUCESSO}✓ Resultado: {operacao_str}{COR_RESET}")

        except ZeroDivisionError as erro:
            print(f"{COR_ERRO}⚠️  Erro: {erro}{COR_RESET}")


if __name__ == "__main__":
    main()