# Simulador de Propagação de Erros Numéricos

![Status](https://img.shields.io/badge/status-concluído-green)

Projeto desenvolvido para a disciplina de Cálculo Numérico da Universidade Federal do Vale do São Francisco (UNIVASF), sob orientação do Prof. Jorge Luis Cavalcanti Ramos.

## Descrição do Projeto

Este projeto é uma ferramenta computacional, desenvolvida em Python com a biblioteca Streamlit, criada para demonstrar na prática os conceitos de **erros de truncamento e arredondamento**.

O objetivo principal é permitir que o usuário visualize como erros numéricos surgem a partir da precisão finita dos computadores, como eles se propagam em operações sequenciais e como podem levar a fenômenos como o **cancelamento subtrativo**, onde a subtração de números muito próximos resulta em uma perda catastrófica de precisão.

## Equipe

* Caio Vinícius Soares Rosa de Souza
* Lucas Gomes de Lucena
* Wendell Moura Leite

## Funcionalidades Principais

* **Entrada de Dados Interativa:** O usuário fornece dois números, a operação aritmética (+, -, *, /), o número de dígitos significativos e o método de ajuste (truncamento ou arredondamento).
* **Cálculo Duplo:** O programa realiza a operação de duas formas:
    1.  **Cálculo Exato:** Utiliza a precisão máxima do Python como valor de referência.
    2.  **Cálculo Aproximado:** Simula uma máquina de precisão finita, ajustando os números de entrada antes de realizar a operação.
* **Análise de Erros:** Exibe o **Erro Absoluto** e o **Erro Relativo** para comparar o resultado exato com o aproximado.
* **Demonstração de Cenários:** Inclui 3 exemplos práticos para ilustrar:
    1.  Operação Simples (comparando truncamento e arredondamento).
    2.  Cancelamento Subtrativo.
    3.  Propagação de Erro em Operações Sequenciais.

## Como Executar o Projeto

Para rodar este simulador em sua máquina local, siga os passos abaixo.

**Pré-requisitos:**
* Ter o [Python 3](https://www.python.org/downloads/) instalado.
* Ter o [Git](https://git-scm.com/downloads) instalado.

**Passo a passo:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd nome-do-repositorio
    ```

3.  **Instale as dependências (principalmente o Streamlit):**
    ```bash
    pip install streamlit
    ```

4.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```
Após executar o comando acima, a aplicação será aberta automaticamente no seu navegador.

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica:** Streamlit
* **Cálculos de Precisão:** Biblioteca `decimal`
