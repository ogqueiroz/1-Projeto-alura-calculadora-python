# 🐍 Calculadora em Python: Interativa & Educativa

> Uma calculadora completa e didática para quem está aprendendo programação, com **Calculadora Real (Visor LCD e Botões)**, **Anatomia do Código**, **Terminal Interativo**, **Histórico de Cálculos** e tratamento rigoroso de erros.
---
https://1-projeto-alura-calculadora-python.vercel.app/

<img width="1258" height="970" alt="Captura de tela 2026-10-28 183731" src="https://github.com/user-attachments/assets/b367a91f-087e-4915-afc2-f9731719f655" />


## 🌟 Funcionalidades do Projeto

- 🖥️ **Calculadora Desktop com Janela Real (`Tkinter`)**: Abre uma janela no Windows, Mac ou Linux com botões clicáveis, visor digital e histórico. Não requer instalação de pacotes externos!
- ⌨️ **Modo Terminal de Comando (`CLI`)**: Versão pura e robusta para terminal com menu de opções (`1` a `4`, `0` para sair), validação de decimais (`float`) e captura de `ValueError`.
- 🧠 **Anatomia do Código & Lógica de Decisão**: Visualizador passo a passo de como o Python toma decisões com `if / elif` e como as 4 funções (`somar`, `subtrair`, `multiplicar`, `dividir`) processam os dados.
- 📜 **Histórico de Cálculos Recentes**: Armazenamento cronológico de todas as operações concluídas na sessão.
- 🛡️ **Tratamento de Exceções**: Proteção nativa contra divisão por zero (`ZeroDivisionError`) e digitação de letras em vez de números.

---

## 📁 Estrutura Organizada dos Arquivos

```text
├── python/                      # 🐍 Scripts Python prontos para rodar no seu computador
│   ├── calculadora_visual.py    # Versão desktop com janela, visor e botões (Tkinter)
│   ├── calculadora.py           # Versão clássica de terminal com menu e input()
│   └── calculadora_turbo.py     # Versão terminal com cores ANSI e histórico
│
├── README.md                    # Documentação do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
└── LICENSE                      # Licença de código aberto
