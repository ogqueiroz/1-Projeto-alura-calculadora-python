"""
Calculadora Visual em Python (Interface Gráfica Desktop com Tkinter)
Autor: Projeto Educativo
Objetivo: Calculadora com Janela, Visor Digital, Botões Clicáveis e Histórico.
Requisitos: Nenhum! Usa a biblioteca nativa tkinter que já vem instalada com o Python.
Executar: python python/calculadora_visual.py
"""

import tkinter as tk
from tkinter import messagebox


# =====================================================================
# 1. FUNÇÕES DAS 4 OPERAÇÕES MATEMÁTICAS BÁSICAS
# =====================================================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero!")
    return a / b


# =====================================================================
# 2. INTERFACE GRÁFICA (VISOR + TECLADO + HISTÓRICO)
# =====================================================================

class CalculadoraVisualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python Interativa")
        self.root.geometry("350x540")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        self.primeiro_numero = None
        self.operador_atual = None
        self.novo_numero = True
        self.historico = []

        self.criar_componentes()

    def criar_componentes(self):
        # 1. VISOR SECUNDÁRIO (Mostra a expressão anterior)
        self.lbl_expressao = tk.Label(
            self.root, 
            text="Python 3 • Pronto", 
            font=("Consolas", 10), 
            bg="#0f172a", 
            fg="#94a3b8", 
            anchor="e"
        )
        self.lbl_expressao.pack(fill="x", padx=16, pady=(16, 4))

        # 2. VISOR PRINCIPAL (Mostra o número grande digitado)
        self.visor = tk.Entry(
            self.root, 
            font=("Consolas", 28, "bold"), 
            bg="#020617", 
            fg="#f59e0b", 
            justify="right", 
            bd=0, 
            highlightthickness=2, 
            highlightbackground="#1e293b",
            highlightcolor="#f59e0b"
        )
        self.visor.insert(0, "0")
        self.visor.pack(fill="x", padx=16, pady=(0, 14), ipady=8)

        # 3. CONTAINER DOS BOTÕES
        frame_botoes = tk.Frame(self.root, bg="#0f172a")
        frame_botoes.pack(fill="both", expand=True, padx=16)

        # Layout do teclado: (texto, linha, coluna, cor_fundo, cor_texto)
        botoes = [
            ("C", 0, 0, "#450a0a", "#fca5a5"), 
            ("⌫", 0, 1, "#1e293b", "#cbd5e1"), 
            ("Hist", 0, 2, "#1e293b", "#c084fc"), 
            ("÷", 0, 3, "#78350f", "#fef3c7"),

            ("7", 1, 0, "#1e293b", "#ffffff"), 
            ("8", 1, 1, "#1e293b", "#ffffff"), 
            ("9", 1, 2, "#1e293b", "#ffffff"), 
            ("×", 1, 3, "#78350f", "#fef3c7"),

            ("4", 2, 0, "#1e293b", "#ffffff"), 
            ("5", 2, 1, "#1e293b", "#ffffff"), 
            ("6", 2, 2, "#1e293b", "#ffffff"), 
            ("-", 2, 3, "#78350f", "#fef3c7"),

            ("1", 3, 0, "#1e293b", "#ffffff"), 
            ("2", 3, 1, "#1e293b", "#ffffff"), 
            ("3", 3, 2, "#1e293b", "#ffffff"), 
            ("+", 3, 3, "#78350f", "#fef3c7"),

            ("±", 4, 0, "#1e293b", "#cbd5e1"), 
            ("0", 4, 1, "#1e293b", "#ffffff"), 
            (".", 4, 2, "#1e293b", "#ffffff"), 
            ("=", 4, 3, "#f59e0b", "#020617"),
        ]

        # Configura colunas e linhas flexíveis
        for col in range(4):
            frame_botoes.columnconfigure(col, weight=1)
        for lin in range(5):
            frame_botoes.rowconfigure(lin, weight=1)

        # Cria os botões na tela
        for (texto, linha, coluna, bg, fg) in botoes:
            btn = tk.Button(
                frame_botoes, 
                text=texto, 
                font=("Segoe UI", 13, "bold"),
                bg=bg, 
                fg=fg, 
                activebackground="#f59e0b", 
                activeforeground="#020617",
                bd=0, 
                relief="flat", 
                cursor="hand2",
                command=lambda t=texto: self.clicar_botao(t)
            )
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)

        # 4. RODAPÉ COM ATALHO DE TECLADO
        lbl_info = tk.Label(
            self.root, 
            text="Use o mouse ou as teclas do seu teclado físico", 
            font=("Segoe UI", 8), 
            bg="#0f172a", 
            fg="#64748b"
        )
        lbl_info.pack(pady=10)

        # Conectar teclado físico do computador
        self.root.bind("<Key>", self.evento_teclado)

    def evento_teclado(self, event):
        tecla = event.char
        if tecla in "0123456789":
            self.adicionar_digito(tecla)
        elif tecla in (".", ","):
            self.adicionar_ponto()
        elif tecla == "+":
            self.definir_operador("+")
        elif tecla == "-":
            self.definir_operador("-")
        elif tecla == "*":
            self.definir_operador("×")
        elif tecla == "/":
            self.definir_operador("÷")
        elif event.keysym in ("Return", "KP_Enter") or tecla == "=":
            self.calcular_resultado()
        elif event.keysym == "BackSpace":
            self.apagar_digito()
        elif event.keysym == "Escape":
            self.limpar_tudo()

    def clicar_botao(self, tecla):
        if tecla in "0123456789":
            self.adicionar_digito(tecla)
        elif tecla == ".":
            self.adicionar_ponto()
        elif tecla in ("+", "-", "×", "÷"):
            self.definir_operador(tecla)
        elif tecla == "=":
            self.calcular_resultado()
        elif tecla == "C":
            self.limpar_tudo()
        elif tecla == "⌫":
            self.apagar_digito()
        elif tecla == "±":
            self.inverter_sinal()
        elif tecla == "Hist":
            self.mostrar_historico()

    def adicionar_digito(self, digito):
        if self.novo_numero:
            self.visor.delete(0, tk.END)
            self.visor.insert(0, digito)
            self.novo_numero = False
        else:
            if self.visor.get() == "0":
                self.visor.delete(0, tk.END)
            self.visor.insert(tk.END, digito)

    def adicionar_ponto(self):
        if self.novo_numero:
            self.visor.delete(0, tk.END)
            self.visor.insert(0, "0.")
            self.novo_numero = False
        elif "." not in self.visor.get():
            self.visor.insert(tk.END, ".")

    def definir_operador(self, op):
        try:
            self.primeiro_numero = float(self.visor.get())
            self.operador_atual = op
            self.novo_numero = True
            self.lbl_expressao.config(text=f"{self.primeiro_numero} {op}")
        except ValueError:
            pass

    def calcular_resultado(self):
        if self.primeiro_numero is None or self.operador_atual is None:
            return

        try:
            segundo_numero = float(self.visor.get())
            a = self.primeiro_numero
            b = segundo_numero
            op = self.operador_atual

            if op == "+":
                res = somar(a, b)
            elif op == "-":
                res = subtrair(a, b)
            elif op == "×":
                res = multiplicar(a, b)
            elif op == "÷":
                res = dividir(a, b)

            texto_res = str(int(res)) if res.is_integer() else f"{res:.4f}".rstrip("0").rstrip(".")

            # Guarda no histórico recente
            registro = f"{a} {op} {b} = {texto_res}"
            self.historico.append(registro)

            self.lbl_expressao.config(text=f"{a} {op} {b} =")
            self.visor.delete(0, tk.END)
            self.visor.insert(0, texto_res)

            self.primeiro_numero = None
            self.operador_atual = None
            self.novo_numero = True

        except ZeroDivisionError as erro:
            messagebox.showerror("Erro Matemático", str(erro))
            self.limpar_tudo()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido no visor!")

    def limpar_tudo(self):
        self.visor.delete(0, tk.END)
        self.visor.insert(0, "0")
        self.primeiro_numero = None
        self.operador_atual = None
        self.novo_numero = True
        self.lbl_expressao.config(text="Pronto para calcular")

    def apagar_digito(self):
        texto = self.visor.get()
        if len(texto) > 1:
            self.visor.delete(len(texto) - 1, tk.END)
        else:
            self.visor.delete(0, tk.END)
            self.visor.insert(0, "0")
            self.novo_numero = True

    def inverter_sinal(self):
        try:
            val = float(self.visor.get()) * -1
            texto = str(int(val)) if val.is_integer() else str(val)
            self.visor.delete(0, tk.END)
            self.visor.insert(0, texto)
        except ValueError:
            pass

    def mostrar_historico(self):
        if not self.historico:
            messagebox.showinfo("Histórico", "Nenhum cálculo recente foi realizado ainda.")
            return

        janela_hist = tk.Toplevel(self.root)
        janela_hist.title("Histórico de Cálculos")
        janela_hist.geometry("300x380")
        janela_hist.configure(bg="#0f172a")

        lbl = tk.Label(janela_hist, text="Cálculos Recentes:", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="#f59e0b")
        lbl.pack(padx=12, pady=10)

        lista = tk.Listbox(janela_hist, font=("Consolas", 10), bg="#020617", fg="#e2e8f0", bd=0, selectbackground="#f59e0b", selectforeground="#020617")
        lista.pack(fill="both", expand=True, padx=12, pady=4)

        for item in reversed(self.historico):
            lista.insert(tk.END, f"• {item}")


if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = CalculadoraVisualApp(janela_principal)
    janela_principal.mainloop()