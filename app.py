import streamlit as st
from erros_prompt2 import (
    truncar,
    arredondar_para_n_significante_digitos,
    normalizar_notacao_cientifica,
    calcular_erro_abs,
    calcular_erro_relat,
)

#streamlit run app.py

def operacao_aritmetica(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ValueError("Divisão por zero streamlit run app.pynão é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida. Use +, -, *, ou /.")

def exibir_resultados_streamlit(x, y, operacao, digitos, metodo, resultado_exato):
    st.subheader("Resultados da Simulação")
    st.write(f"**Dados de entrada:**")
    st.write(f"- x = {x}")
    st.write(f"- y = {y}")
    st.write(f"- Operação = {operacao}")
    st.write(f"- Dígitos significativos (n) = {digitos}")
    st.write(f"- Método de ajuste = {metodo}")

    st.write(f"**Valor Exato:** {x} {operacao} {y} = {resultado_exato:.7f} ou {normalizar_notacao_cientifica(resultado_exato)}.")

    st.write(f"**Análise com o Simulador (k={digitos}, com {metodo}):**")
    st.write(f"Primeiro, os números são representados na máquina:")

    x_representado = arredondar_para_n_significante_digitos(x, digitos) if metodo == 'arredondamento' else truncar(x, digitos)
    y_representado = arredondar_para_n_significante_digitos(y, digitos) if metodo == 'arredondamento' else truncar(y, digitos)

    st.write(f"- x_aprox = {x_representado} (ajustado para {digitos} dígitos)")
    st.write(f"- y_aprox = {y_representado} (ajustado para {digitos} dígitos)")

    st.write(f"**A operação é realizada com os valores aproximados:**")

    resultado_aproximado_calculado = operacao_aritmetica(x_representado, y_representado, operacao)

    st.write(f"Resultado Aprox = {x_representado} {operacao} {y_representado} = {resultado_aproximado_calculado:.7f} ou {normalizar_notacao_cientifica(resultado_aproximado_calculado)}.")

    st.write(f"**Comparação e Erros:**")

    erro_abs = calcular_erro_abs(resultado_exato, resultado_aproximado_calculado)
    erro_relat = calcular_erro_relat(resultado_exato, resultado_aproximado_calculado)

    st.write(f"- Erro Absoluto: |{resultado_exato:.7f} - {resultado_aproximado_calculado:.7f}| = {erro_abs:.7f}")
    st.write(f"- Erro Relativo: |{erro_abs:.7f} / {resultado_aproximado_calculado:.7f}| = {erro_relat:.4f} (ou {erro_relat * 100:.2f}%).")

def exibir_comparacao_trunc_arred_streamlit(x, y, operacao, digitos):
    try:
        resultado_exato_base = operacao_aritmetica(x, y, operacao)

        st.write(f"**Valor Exato da Operação:** {x} {operacao} {y} = {resultado_exato_base:.7f} ou {normalizar_notacao_cientifica(resultado_exato_base)}.")

        st.subheader("Resultados para Truncamento")
        x_trunc = truncar(x, digitos)
        y_trunc = truncar(y, digitos)
        resultado_aproximado_trunc = operacao_aritmetica(x_trunc, y_trunc, operacao)

        erro_abs_trunc = calcular_erro_abs(resultado_exato_base, resultado_aproximado_trunc)
        erro_relat_trunc = calcular_erro_relat(resultado_exato_base, resultado_aproximado_trunc)

        st.write(f"- Resultado Aproximado (Truncamento): {resultado_aproximado_trunc:.7f} ou {normalizar_notacao_cientifica(resultado_aproximado_trunc)}.")
        st.write(f"- Erro Absoluto (Truncamento): {erro_abs_trunc:.7f}")
        st.write(f"- Erro Relativo (Truncamento): {erro_relat_trunc:.4f} (ou {erro_relat_trunc * 100:.2f}%).")

        st.subheader("Resultados para Arredondamento")
        x_arred = arredondar_para_n_significante_digitos(x, digitos)
        y_arred = arredondar_para_n_significante_digitos(y, digitos)
        resultado_aproximado_arred = operacao_aritmetica(x_arred, y_arred, operacao)

        erro_abs_arred = calcular_erro_abs(resultado_exato_base, resultado_aproximado_arred)
        erro_relat_arred = calcular_erro_relat(resultado_exato_base, resultado_aproximado_arred)

        st.write(f"- Resultado Aproximado (Arredondamento): {resultado_aproximado_arred:.7f} ou {normalizar_notacao_cientifica(resultado_aproximado_arred)}.")
        st.write(f"- Erro Absoluto (Arredondamento): {erro_abs_arred:.7f}")
        st.write(f"- Erro Relativo (Arredondamento): {erro_relat_arred:.4f} (ou {erro_relat_arred * 100:.2f}%).")

    except ValueError as e:
        st.error(f"Erro: {e}")

def exemplo1_operacao_simples_streamlit():
    st.header("Exemplo 1: Operação Simples")
    st.write("Realiza uma operação entre dois números, mostrando resultados por truncamento e arredondamento.")

    x = st.number_input("Digite o primeiro número (x)", value=0.12345, format="%.5f", key="x1")
    y = st.number_input("Digite o segundo número (y)", value=0.67890, format="%.5f", key="y1")
    operacao = st.selectbox("Escolha a operação", ["+", "-", "*", "/"], key="op1")
    digitos = st.slider("Escolha o número de dígitos significativos (n)", 1, 15, 5, key="dig1")

    if st.button("Calcular Exemplo 1", key="btn1"):
        exibir_comparacao_trunc_arred_streamlit(x, y, operacao, digitos)

def exemplo2_cancelamento_subtrativo_streamlit():
    st.header("Exemplo 2: Propagação de Erro e Cancelamento Subtrativo")
    st.write("Demonstra como a subtração de números muito próximos pode levar a uma perda de dígitos significativos.")

    x_input = st.number_input("Digite o primeiro número (x)", value=0.76545, format="%.5f", key="x2")
    y_input = st.number_input("Digite o segundo número (y)", value=0.76541, format="%.5f", key="y2")
    operacao_input = st.selectbox("Escolha a operação", ["-", "+", "*", "/"], key="op2")
    digitos_input = st.slider("Escolha o número de dígitos significativos (n)", 1, 15, 4, key="dig2")
    metodo_input = st.selectbox("Escolha o método de ajuste", ["arredondamento", "truncamento"], key="met2")

    if st.button("Calcular Exemplo 2", key="btn2"):
        try:
            resultado_exato = operacao_aritmetica(x_input, y_input, operacao_input)
            exibir_resultados_streamlit(x_input, y_input, operacao_input, digitos_input, metodo_input, resultado_exato)
            st.info("Este exemplo demonstra drasticamente como a subtração de dois números muito próximos pode levar a uma perda total de dígitos significativos, resultando em um erro relativo muito alto ou mesmo tornando nula uma operação de subtração (demonstrar).")
        except ValueError as e:
            st.error(f"Erro: {e}")

def exemplo3_sequencia_operacoes_streamlit():
    st.header("Exemplo 3: Propagação de Erro em uma Sequência de Operações")
    st.write("Este exemplo mostra como pequenos erros se acumulam em operações repetidas.")

    numero_base = st.number_input("Digite o número base", value=0.56786, format="%.5f", key="num3")
    operacao_repetida = st.selectbox("Escolha a operação a ser repetida", ["+", "-", "*", "/"], key="op3")
    vezes_repetir = st.slider("Quantas vezes repetir a operação", 1, 20, 10, key="vezes3")
    digitos = st.slider("Escolha o número de dígitos significativos (n)", 1, 15, 4, key="dig3")
    metodo = st.selectbox("Escolha o método de ajuste", ["truncamento", "arredondamento"], key="met3")

    if st.button("Calcular Exemplo 3", key="btn3"):
        try:
            valor_exato_total = numero_base
            if operacao_repetida == '+':
                valor_exato_total = numero_base * vezes_repetir
            elif operacao_repetida == '-':
                if vezes_repetir > 1:
                    valor_exato_total = numero_base - (numero_base * (vezes_repetir - 1))
                else:
                    valor_exato_total = numero_base
            elif operacao_repetida == '*':
                valor_exato_total = numero_base ** vezes_repetir
            elif operacao_repetida == '/':
                if vezes_repetir > 1:
                    valor_exato_total = numero_base / (numero_base ** (vezes_repetir - 1))
                else:
                    valor_exato_total = numero_base

            valor_aproximado_acumulado = numero_base

            st.write(f"**Valor Exato Total ({numero_base} {operacao_repetida} ... {operacao_repetida} {numero_base} {vezes_repetir} vezes):** {valor_exato_total:.7f}")
            st.write(f"**Análise com o Simulador (k={digitos}, com {metodo}):**")

            st.subheader("Passos da Operação Sequencial")
            for i in range(1, vezes_repetir):
                resultado_intermediario_exato = operacao_aritmetica(valor_aproximado_acumulado, numero_base, operacao_repetida)

                if metodo == 'truncamento':
                    valor_aproximado_acumulado = truncar(resultado_intermediario_exato, digitos+1) # Digitos+1 para corrigir o 0 como n1 padrão 
                elif metodo == 'arredondamento':
                    valor_aproximado_acumulado = arredondar_para_n_significante_digitos(resultado_intermediario_exato, digitos=1)

                st.write(f"- Passo {i+1}: Resultado parcial aproximado = {valor_aproximado_acumulado:.7f}")

            st.write(f"**Resultado Final Aproximado (após {vezes_repetir} operações):** {valor_aproximado_acumulado:.7f}")

            erro_abs_total = calcular_erro_abs(valor_exato_total, valor_aproximado_acumulado)
            erro_relat_total = calcular_erro_relat(valor_exato_total, valor_aproximado_acumulado)

            st.write(f"- Erro Absoluto Total: |{valor_exato_total:.7f} - {valor_aproximado_acumulado:.7f}| = {erro_abs_total:.7f}")
            st.write(f"- Erro Relativo Total: |{erro_abs_total:.7f} / {valor_aproximado_acumulado:.7f}| = {erro_relat_total:.4f} (ou {erro_relat_total * 100:.2f}%).")
            st.info("Este exemplo mostra como pequenos erros podem se acumular ao longo de várias operações, levando a um resultado final significativamente diferente do valor exato.")
        except ValueError as e:
            st.error(f"Erro: {e}")

def main(): 
    st.set_page_config(layout="wide", page_title="Simulador de Erros Numéricos", page_icon="🔢") 
    st.title("🔢 Simulador de Propagação de Erros Numéricos") 

    tab1, tab2, tab3 = st.tabs(["Exemplo 1: Operação Simples", 
                                "Exemplo 2: Cancelamento Subtrativo", 
                                "Exemplo 3: Sequência de Operações"]) 

    with tab1:
        exemplo1_operacao_simples_streamlit() 

    with tab2:
        exemplo2_cancelamento_subtrativo_streamlit() 

    with tab3:
        exemplo3_sequencia_operacoes_streamlit() 

if __name__ == "__main__": 
    main() 

#streamlit run app.py