# 🐍 Calculadora em Python: Interativa & Educativa

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/Imersão-Alura%20com%20IA-0070f3?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Alura" />
  <img src="https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

> Uma calculadora completa, modular e didática desenvolvida para ensinar conceitos fundamentais de programação, contando com **Calculadora Real (Visor LCD e Botões)**, **Anatomia do Código**, **Simulador de Terminal**, **Histórico de Cálculos** e tratamento rigoroso de erros.
---
https://1-projeto-alura-calculadora-python.vercel.app/ <-- [Abra para testar a calculadora]

<img width="1258" height="970" alt="Captura de tela 2026-10-28 183731" src="https://github.com/user-attachments/assets/b367a91f-087e-4915-afc2-f9731719f655" />


## 🎓 Como Foi Feito & Imersão Alura

Este projeto foi concebido e desenvolvido durante a **Imersão de Engenharia de Software com IA da Alura**.

O objetivo da imersão foi vivenciar na prática o fluxo de trabalho da nova geração de engenharia de software: utilizar **Inteligência Artificial como parceira de desenvolvimento (Pair Programming)** para acelerar a arquitetura, refatoração de código, tratamento de exceções e criação de interfaces modernas.


## 🛠️ Processo de Criação e Metodologia:
1. **Engenharia de Prompt & Requisitos:** Definição clara dos requisitos de código limpo (funções separadas para operações, menu com loop `while`, validação com `try/except` para não quebrar com letras e proteção contra divisão por zero).
2. **Modularização de Código:** Separação anatômica do script Python em funções puras com `return` e ponto de entrada seguro com `if __name__ == '__main__':`.
3. **Evolução da Interface do Usuário (UI/UX):**
   - Criação da versão **CLI (Terminal)** tradicional;
   - Construção da versão **Desktop Nativa (`Tkinter`)** com janela, visor e botões reais;
   - Desenvolvimento do **Laboratório Web Interativo** com simulador de tomada de decisão (`if / elif`) e histórico reativo na memória.
4. **Deploy & Publicação:** Versionamento com Git, publicação em repositório público no GitHub com licença MIT e deploy gratuito contínuo na Vercel.


## 🌟 Funcionalidades do Projeto

- 🖥️ **Calculadora Desktop com Janela Real (`Tkinter`)**: Abre uma janela no Windows, Mac ou Linux com botões clicáveis, visor digital e histórico. Não requer instalação de pacotes externos!
- ⌨️ **Modo Terminal de Comando (`CLI`)**: Versão pura e robusta para terminal com menu de opções (`1` a `4`, `0` para sair), validação de decimais (`float`) e captura de `ValueError`.
- 🧠 **Anatomia do Código & Lógica de Decisão**: Visualizador passo a passo de como o Python toma decisões com `if / elif` e como as 4 funções (`somar`, `subtrair`, `multiplicar`, `dividir`) processam os dados.
- 📜 **Histórico de Cálculos Recentes**: Armazenamento cronológico de todas as operações concluídas na sessão.
- 🛡️ **Tratamento de Exceções**: Proteção nativa contra divisão por zero (`ZeroDivisionError`) e digitação de letras em vez de números.


## 🚀 Como Executar no seu Computador

### 1. Calculadora com Janela e Botões (Recomendado):
python python/calculadora_visual.py

### 2. Calculadora no Terminal de Texto:
python python/calculadora.py

### 3. Aplicação Web no Terminal do VS Code (com Node.js & package.json):  <-- [Metodo 1]
1. Abra o terminal com Ctrl + `
2. npm install
3. npm run dev
4. Clique no link http://localhost:3000/

### 4. Abrir Direto pelo index.html (Super Rápido, sem Terminal):          <-- [Metodo 2]
- Opção A: Dois cliques no arquivo index.html no Windows
- Opção B: Botão direito no index.html > Open with Live Server no VS Code

 
## 📁 Estrutura Organizada dos Arquivos

```text
├── python/                      # 🐍 Scripts Python prontos para rodar no seu computador
│   ├── calculadora_visual.py    # Versão desktop com janela, visor e botões (Tkinter)
│   ├── calculadora.py           # Versão clássica de terminal com menu e input()
│   └── calculadora_turbo.py     # Versão terminal com cores ANSI e histórico
│
├── index.html                   # 🌐 Aplicação Web completa (Vercel / GitHub Pages)
├── README.md                    # 📖 Documentação do projeto
├── .gitignore                   # 🚫 Arquivos ignorados pelo Git
└── LICENSE                      # 📜 Licença de código aberto MIT
