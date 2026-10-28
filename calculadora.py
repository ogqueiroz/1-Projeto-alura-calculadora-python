"""
Calculadora Básica em Python (Terminal)
Autor: Projeto Educativo
Objetivo: Ensinar conceitos fundamentais (funções, loops, validação de dados e tratamento de erros).
Executar: python python/calculadora.py
"""

# =====================================================================
# 1. FUNÇÕES DAS 4 OPERAÇÕES MATEMÁTICAS BÁSICAS
# =====================================================================

def somar(primeiro_valor, segundo_valor):
    """Retorna a soma de dois números."""
    return primeiro_valor + segundo_valor


def subtrair(primeiro_valor, segundo_valor):
    """Retorna a subtração do primeiro número pelo segundo."""
    return primeiro_valor - segundo_valor


def multiplicar(primeiro_valor, segundo_valor):
    """Retorna a multiplicação de dois números."""
    return primeiro_valor * segundo_valor


def dividir(primeiro_valor, segundo_valor):
    """
    Retorna a divisão do primeiro número pelo segundo.
    Se o divisor for zero, gera um erro matemático específico.
    """
    if segundo_valor == 0:
        raise ZeroDivisionError("Não é possível realizar divisão por zero.")
    return primeiro_valor / segundo_valor


# =====================================================================
# 2. FUNÇÃO AUXILIAR PARA LEITURA SEGURA DE NÚMEROS
# =====================================================================

def pedir_numero(mensagem):
    """
    Pede um número ao usuário e repete a pergunta até que um valor
    numérico válido (inteiro ou decimal) seja digitado.
    Aceita tanto ponto quanto vírgula como separador decimal.
    """
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print("⚠️  Entrada inválida! Por favor, digite apenas números.")


# =====================================================================
# 3. FUNÇÃO DO MENU DE OPÇÕES
# =====================================================================

def exibir_menu():
    """Exibe na tela o cabeçalho e as opções disponíveis da calculadora."""
    print("\n" + "=" * 40)
    print("         CALCULADORA EM PYTHON")
    print("=" * 40)
    print("1 - Somar (+)")
    print("2 - Subtrair (-)")
    print("3 - Multiplicar (*)")
    print("4 - Dividir (/)")
    print("0 - Sair do programa")
    print("-" * 40)


# =====================================================================
# 4. FUNÇÃO PRINCIPAL (ORQUESTRADORA DO PROGRAMA)
# =====================================================================

def main():
    """Função principal que gerencia o fluxo da calculadora."""
    print("Olá! Seja bem-vindo à Calculadora em Python!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 4): ").strip()

        # Condição de saída: opção 0
        if opcao == "0":
            print("\nObrigado por usar a calculadora! Bons estudos e até a próxima! 👋")
            break

        # Validação: verifica se a opção digitada existe no menu
        if opcao not in ("1", "2", "3", "4"):
            print("⚠️  Opção inválida! Escolha um número entre 0 e 4.")
            continue

        print("\n--- Digite os valores para o cálculo ---")
        num1 = pedir_numero("Digite o primeiro número: ")
        num2 = pedir_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(num1, num2)
                simbolo = "+"
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                simbolo = "-"
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                simbolo = "*"
            elif opcao == "4":
                resultado = dividir(num1, num2)
                simbolo = "/"

            print("\n" + "✓" * 40)
            print(f"Resultado: {num1} {simbolo} {num2} = {resultado}")
            print("✓" * 40)

        except ZeroDivisionError as erro:
            print(f"\n⚠️  Erro matemático: {erro}")


if __name__ == "__main__":
    main()