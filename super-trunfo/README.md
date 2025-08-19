# Desafio Cartas Super Trunfo (Python)

Projeto simples em Python para cumprir o trabalho **Desafio Cartas Super Trunfo** da disciplina *Introdução à Programação de Computadores*.

> **Observação:** Os números do dataset são *didáticos* (aproximados/simplificados). Você pode editar `super_trunfo/data/cards.json` e colocar outras cartas/atributos.

## Como rodar

1) Tenha o Python 3.10+ instalado.
2) (Opcional) Crie um ambiente virtual:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```
3) Rode o jogo:
```bash
python main.py
```

## Como jogar
- O programa sorteia 2 cartas (uma para você e outra para o computador).
- Você escolhe **um atributo** para disputar.
- Quem tiver o **maior valor** naquele atributo vence a rodada.
- Digite `s` para continuar jogando ou `n` para sair.

## Como enviar para o GitHub
1. Crie um repositório novo no GitHub (nome sugerido: `desafio-super-trunfo`).
2. No seu computador, abra a pasta do projeto e rode:
```bash
git init
git add .
git commit -m "Desafio Cartas Super Trunfo"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/desafio-super-trunfo.git
git push -u origin main
```
3. Copie a **URL do repositório** e cole no campo do trabalho na Estácio.

## Estrutura
```
super-trunfo/
  main.py
  super_trunfo/
    __init__.py
    game.py
    data/cards.json
  README.md
```

## Personalizações possíveis
- Trocar as cartas (ex.: animais, planetas, carros).
- Adicionar novos atributos.
- Implementar placar por várias rodadas.
- Implementar regra onde **menor é melhor** para algum atributo específico.
