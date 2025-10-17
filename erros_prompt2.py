# Códigos para cores no terminal (ANSI)
COLOR_RESET = "\033[0m" # Reset para a cor padrão 
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_BOLD = "\033[1m" # Reset para negrito

import decimal
# Módulo decimal do python para uso de float 

# Função 1, para converter o número digitado para notação científica  
def normalizar_notacao_cientifica(numero): 
    if numero == 0: 
        return "0.0 x 10^0" 
    str_cientifica = f"{numero:.10e}" # Começar a formatar como string, a notação científica 
    str_mantissa, str_expoente = str_cientifica.split("e") # Separar o número digitado em dois, pela letra e
    exponente = int(str_expoente) # Pega a parte inteira do expoente, convertendo-a
    mantissa = decimal.Decimal(str_mantissa) # Converte a string mantissa para o decimal da notação 
    mantissa = mantissa.normalize() # Normaliza tirando os 0s a direita 
    return f"{mantissa} x 10^{exponente}" # Retorna a  string final com o número convertido para notação cientifica 

# Função 2, para truncar o número digitado de acordo com os dígitos significantes para o usuário 
def truncar(numero, n_significante_digitos): 
    if numero == 0: 
        return 0.0 
    d = decimal.Decimal(str(numero)) # Recebe a string digitada e converte para numerico, decimal 
    digitos = d.as_tuple().digits # Extrai os dígitos do numero digitado para uma lista tupla, ex. se o número for 1.234 sai uma tupla (1, 2, 3, 4)
    if n_significante_digitos >= len(digitos): # N digitos for maior que o digitado, n precisa truncar 
        return float(d) 
    truncar_digitos = digitos[:n_significante_digitos] # Pega apenas os primeiros n digitos para truncar
    exp = d.as_tuple().exponent + (len(digitos) - n_significante_digitos) # Ajuste no expoente para manter a grandeza, de acordo com
                                                                          # a quantidade dos dígitos e o n significante solicitado 
    truncado = decimal.Decimal((d.as_tuple().sign, truncar_digitos, exp)) # Soma os digitos truncados com o novo expoente 
                                                                          # Sign é 0 ou 1 (positivo e negativo)
    return float(truncado) # Retorna o numero truncado e em float 

# Função 3, para arredondar o número digitado de acordo com os dígitos significantes para o usuário 
def arredondar_para_n_significante_digitos(numero, n_significante_digitos): 
    if numero == 0: 
        return 0.0 
    d = decimal.Decimal(str(numero)) # Converter o numero para decimal
    contexto = decimal.Context(prec=n_significante_digitos, rounding=decimal.ROUND_HALF_UP) 
    # Arrendondamento da parte inteira do decimal com precisão, prec = precisão  e rouding é a regra. 
    # HALF_UP se for 5, pra cima
    # DOWN, HALF_EVEN 
    with decimal.localcontext(contexto): # Contexto temporário
        arredondado = +d # Soma do inteiro o numero digitado com o arredondado
    return float(arredondado) 

# Função 4, para calcular o erro absoluto (exato - aproximado) 
def calcular_erro_abs(valor_exato, valor_aproximado): 
    return abs(valor_exato - valor_aproximado) 
# Recebe os valores já digitados e retorna o absoluto vide fórmula

# Função 5, para calcular o erro relativo ((exato - aproximado) / aproximado) 
def calcular_erro_relat(valor_exato, valor_aproximado): 
    if valor_aproximado == 0: 
        return float("inf") 
    return abs((valor_exato - valor_aproximado) / valor_aproximado) 
# Recebe os valores já digitados e retorna o relativo vide fórmula (aprox sendo denominador)

# Função 6, no exemplo I é pedido para que ocorra uma operação e haja um comparativo entre 
# o resultado trucando VS o resultado arredondado. Usando as funções 1, 2, 3, 4, 5. 
def exibir_comparacao_trunc_arred(x, y, operacao, digitos): 
    try: 
       # Start var
        resultado_exato_base = 0.0 
       
        # O resultado exato da operação é calculado 
        if operacao == '+': 
            resultado_exato_base = x + y 
        elif operacao == '-': 
            resultado_exato_base = x - y 
        elif operacao == '*': 
            resultado_exato_base = x * y 
        elif operacao == '/': 
            if y == 0: 
                raise ValueError("Divisão por zero não é permitida.") # Erro se div0
            resultado_exato_base = x / y 
        else: 
            raise ValueError("Operação inválida. Use +, -, *, ou /.") # Erro se operação dif

        print(f"{COLOR_BLUE}\nValor Exato da Operação: {x} {operacao} {y} = {resultado_exato_base:.4f} ou {normalizar_notacao_cientifica(resultado_exato_base)}.{COLOR_RESET}") 

        # --- Resultados para Truncamento --- 
        print(f"{COLOR_YELLOW}\n--- Resultados para Truncamento ---{COLOR_RESET}") 

        # O resultado aproximado para truncado é calculado 
        x_trunc = truncar(x, digitos) 
        y_trunc = truncar(y, digitos) 
        # Trunca os dois numeros 

        resultado_aproximado_trunc = 0.0 
        if operacao == '+': 
            resultado_aproximado_trunc = x_trunc + y_trunc 
        elif operacao == '-': 
            resultado_aproximado_trunc = x_trunc - y_trunc 
        elif operacao == '*': 
            resultado_aproximado_trunc = x_trunc * y_trunc 
        elif operacao == '/': 
            if y_trunc == 0: 
                raise ValueError("Divisão por zero com valores aproximados (truncamento) não é permitida.") 
            resultado_aproximado_trunc = x_trunc / y_trunc 

        erro_abs_trunc = calcular_erro_abs(resultado_exato_base, resultado_aproximado_trunc) 
        erro_relat_trunc = calcular_erro_relat(resultado_exato_base, resultado_aproximado_trunc) 

        print(f"Resultado Aproximado (Truncamento): {resultado_aproximado_trunc:.4f} ou {normalizar_notacao_cientifica(resultado_aproximado_trunc)}.") 
        print(f"Erro Absoluto (Truncamento) é |{resultado_exato_base:.7f} - {resultado_aproximado_trunc:.7f}| = {erro_abs_trunc:.7f}") 
        print(f"Erro Relativo (Truncamento) é |{erro_abs_trunc:.7f} / {resultado_aproximado_trunc:.7f}| = {erro_relat_trunc:.7f} (ou {erro_relat_trunc * 100:.4f}%).") 

        # --- Resultados para Arredondamento --- 
        print(f"{COLOR_YELLOW}\n--- Resultados para Arredondamento ---{COLOR_RESET}") 

        # O resultado aproximado para arredondado é calculado 
        x_arred = arredondar_para_n_significante_digitos(x, digitos) 
        y_arred = arredondar_para_n_significante_digitos(y, digitos) 
        resultado_aproximado_arred = 0.0 
        if operacao == '+': 
            resultado_aproximado_arred = x_arred + y_arred 
        elif operacao == '-': 
            resultado_aproximado_arred = x_arred - y_arred 
        elif operacao == '*': 
            resultado_aproximado_arred = x_arred * y_arred 
        elif operacao == '/': 
            if y_arred == 0: 
                raise ValueError("Divisão por zero com valores aproximados (arredondamento) não é permitida.") 
            resultado_aproximado_arred = x_arred / y_arred 

        erro_abs_arred = calcular_erro_abs(resultado_exato_base, resultado_aproximado_arred) 
        erro_relat_arred = calcular_erro_relat(resultado_exato_base, resultado_aproximado_arred) 

        print(f"Resultado Aproximado (Arredondamento): {resultado_aproximado_arred:.4f} ou {normalizar_notacao_cientifica(resultado_aproximado_arred)}.") 
        print(f"Erro Absoluto (Arredondamento) é |{resultado_exato_base:.7f} - {resultado_aproximado_arred:.7f}| = {erro_abs_arred:.7f}") 
        print(f"Erro Relativo (Arredondamento) é |{erro_abs_arred:.7f} / {resultado_aproximado_arred:.7f}| =  {erro_relat_arred:.9f} (ou {erro_relat_arred * 100:.2f}%).") 

    except ValueError as e: 
        print(f"{COLOR_RED}Erro: {e}{COLOR_RESET}") 
    # Qualquer tipo de erro relacionado ao que for digitado no bloco try
    # Imprime erro 

# Função 7, resumo das entradas + realização dos cálculos + resultados dos cálculos aritméticos 
def exibir_resultados(x, y, operacao, digitos, metodo, resultado_exato): 
# acima temos todas as variáveis que vão ser usadas nessa def (função), direta ou indiretamente 

    print(f"{COLOR_BLUE}{COLOR_BOLD}\n----- Resultados da Simulação -----{COLOR_RESET}") 
    print("Dados de entrada:") 
    print(f"x = {x}") 
    print(f"y = {y}") 
    print(f"Operação = {operacao}") 
    print(f"Dígitos significativos (n) = {digitos+1}") # Digitos+1 para corrigir o 0 como n1 padrão 
    print(f"Método de ajuste = {metodo}") 
    # Mostra os valores que entraram no sistema, na calculadora 

    print(f"\n{COLOR_BLUE}Valor Exato: {x} {operacao} {y} = {resultado_exato:.7f} ou {normalizar_notacao_cientifica(resultado_exato)}.{COLOR_RESET}") 
    # Valor exato da operação com 7 casas e em notação científica 

    print(f"\nAnálise com o Simulador (k={digitos}, com {metodo}):") 
    print(f"Primeiro, os números são representados na máquina:") 

    x_representado = arredondar_para_n_significante_digitos(x, digitos) if metodo == 'arredondamento' else truncar(x, digitos) 
    y_representado = arredondar_para_n_significante_digitos(y, digitos) if metodo == 'arredondamento' else truncar(y, digitos) 
    # Arrendonda ou trunca x e y (Dependendo da escolha)

    print(f"x_aprox = {x_representado} (ajustado para {digitos} dígitos)") 
    print(f"y_aprox = {y_representado} (ajustado para {digitos} dígitos)") 
    # Mostra os valores aproximados de cada um, antes da operação

    print(f"\nA operação é realizada com os valores aproximados:") 

    # Cálculo do resultado aproximado com 7 casas 
    resultado_aproximado_calculado = 0.0 # Start var
    if operacao == '+': 
        resultado_aproximado_calculado = x_representado + y_representado 
    elif operacao == '-': 
        resultado_aproximado_calculado = x_representado - y_representado 
    elif operacao == '*': 
        resultado_aproximado_calculado = x_representado * y_representado 
    elif operacao == '/': 
        if y_representado == 0: # Se o div0 
            raise ValueError("Divisão por zero com valores aproximados não é permitida.") # Erro caso ocorra div0
        resultado_aproximado_calculado = x_representado / y_representado 

    print(f"Resultado Aprox = {x_representado} {operacao} {y_representado} = {resultado_aproximado_calculado:.7f} ou {normalizar_notacao_cientifica(resultado_aproximado_calculado)}.") 
    # Mostra o resultado do cálculo com os valores aproximados

    print(f"\nComparação e Erros:") 

    erro_abs = calcular_erro_abs(resultado_exato, resultado_aproximado_calculado) 
    erro_relat = calcular_erro_relat(resultado_exato, resultado_aproximado_calculado) 

    print(f"Erro Absoluto: |{resultado_exato:.7f} - {resultado_aproximado_calculado:.7f}| = {erro_abs:.7f}") 
    print(f"Erro Relativo: |{erro_abs:.7f} / {resultado_aproximado_calculado:.7f}| = {erro_relat:.4f} (ou {erro_relat * 100:.4f}%).") 
   # Cálculo dos erros abs e relat chamando as funções, com 7 e 4 casas decimais de precisão

# Função 8, esse é o exemplo I onde são solicitados ao usuário as entradas necessárias 
# para que haja o uso da Função 7 (o comparativo entre truncado e arredondado). 
def exemplo1_operacao_simples(): 
    print(f"{COLOR_GREEN}{COLOR_BOLD}\n--- Exemplo 1: Operação Simples ---{COLOR_RESET}") 
    print("Realiza uma operação entre dois números, mostrando resultados por truncamento e arredondamento.") 

    x = float(input("Digite o primeiro número (x), ex: 0.12345: ")) 
    y = float(input("Digite o segundo número (y), ex: 0.67890: ")) 
    operacao = input("Digite a operação aritmética (+, -, *, /), ex: +: ") 
    digitos = int(input("Digite o número de dígitos significativos (n), ex: 4: ")) 

    exibir_comparacao_trunc_arred(x, y, operacao, digitos) 
    # Chama a função com os dados inseridos

# Função 9, exemplo II onde são solicitados ao usuário as entradas necessárias 
# para que haja o uso da Função 6 (exibir resultados da "simulação"). 
def exemplo2_cancelamento_subtrativo(): 
    print(f"{COLOR_GREEN}{COLOR_BOLD}\n--- Exemplo 2: Propagação de Erro e Cancelamento Subtrativo ---{COLOR_RESET}") 
    print("Demonstra como a subtração de números muito próximos pode levar a uma perda de dígitos significativos.") 

    x_input = float(input("Digite o primeiro número (x), ex: 0.76545: ")) 
    y_input = float(input("Digite o segundo número (y), ex: 0.76541: ")) 
    operacao_input = input("Digite a operação aritmética (+, -, *, /), ex: -: ") 
    digitos_input = int(input("Digite o número de dígitos significativos (n), ex: 4: ")) 
    metodo_input = input("Digite o método de ajuste (arredondamento ou truncamento), ex: arredondamento: ").lower() 

    try: 
        # Calcula o resultado exato da operação 
        resultado_exato = 0.0 
        if operacao_input == '+': 
            resultado_exato = x_input + y_input 
        elif operacao_input == '-': 
            resultado_exato = x_input - y_input 
        elif operacao_input == '*': 
            resultado_exato = x_input * y_input 
        elif operacao_input == '/': 
            if y_input == 0: 
                raise ValueError("Divisão por zero não é permitida.") 
            resultado_exato = x_input / y_input 

        # Passamos o resultado_exato duas vezes, pois exibir_resultados agora calcula o aproximado internamente 
        exibir_resultados(x_input, y_input, operacao_input, digitos_input, metodo_input, resultado_exato) 

    except ValueError as e: 
        print(f"{COLOR_RED}Erro: {e}{COLOR_RESET}") 

# Função 10, exemplo III onde são solicitados ao usuário as entradas necessárias 
# para que haja o uso da Função 1, 3, 4 e 5. 
def exemplo3_sequencia_somas(): 
    print(f"{COLOR_GREEN}{COLOR_BOLD}\n--- Exemplo 3: Propagação de Erro em uma Sequência de Operações ---{COLOR_RESET}") 
    print("Este exemplo mostra como pequenos erros se acumulam em operações repetidas.") 

    numero_base = float(input("Digite o número base (ex: 0.56786): ")) 
    operacao_repetida = input("Digite a operação a ser repetida (+, -, *, /), ex: +: ") 
    vezes_repetir = int(input("Quantas vezes repetir a operação (ex: 10): ")) 
    digitos = int(input("Digite o número de dígitos significativos (n), ex: 4: ")) 
    metodo = input("Digite o método de ajuste (arredondamento ou truncamento), ex: truncamento: ").lower() 

    # Calcula o valor exato total (para a operação repetida) 
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
    # O valor acumulado começa sendo o da base

    print(f"{COLOR_BLUE}\nValor Exato Total ({numero_base} {operacao_repetida} ... {operacao_repetida} {numero_base} ( {vezes_repetir} vezes)): {valor_exato_total:.4f}{COLOR_RESET}") 
    print(f"Análise com o Simulador (k={digitos}, com {metodo}):") 

    print(f"{COLOR_YELLOW}\n--- Passos da Operação Sequencialmente ---{COLOR_RESET}") 
    for i in range(1, vezes_repetir): 
        try: 
            # Primeiro, ajusta o valor acumulado e o número base para a precisão da máquina 
            valor_acumulado_representado = arredondar_para_n_significante_digitos(valor_aproximado_acumulado, digitos+1) if metodo == 'arredondamento' else truncar(valor_aproximado_acumulado, digitos+1) 
            numero_base_representado = arredondar_para_n_significante_digitos(numero_base, digitos+1) if metodo == 'arredondamento' else truncar(numero_base, digitos+1) 

            # Realiza a operação com os valores representados 
            if operacao_repetida == '+': 
                valor_aproximado_acumulado = valor_acumulado_representado + numero_base_representado 
            elif operacao_repetida == '-': 
                valor_aproximado_acumulado = valor_acumulado_representado - numero_base_representado 
            elif operacao_repetida == '*': 
                valor_aproximado_acumulado = valor_acumulado_representado * numero_base_representado 
            elif operacao_repetida == '/': 
                if numero_base_representado == 0: 
                    raise ValueError("Divisão por zero com valores aproximados no passo sequencial não é permitida.") 
                valor_aproximado_acumulado = valor_acumulado_representado / numero_base_representado 
            else: 
                raise ValueError("Operação inválida no passo sequencial.") 

            # Após a operação, o resultado é ajustado novamente para a precisão da máquina 
            if metodo == 'truncamento': 
                valor_aproximado_acumulado = truncar(valor_aproximado_acumulado, digitos+1) 
            elif metodo == 'arredondamento': 
                valor_aproximado_acumulado = arredondar_para_n_significante_digitos(valor_aproximado_acumulado, digitos+1) 

            print(f"Passo {i+1}: Resultado parcial aproximado = {valor_aproximado_acumulado:.4f}") 
        except ValueError as e: 
            print(f"{COLOR_RED}Erro no passo {i+1}: {e}{COLOR_RESET}") 
            break 
            # Finaliza o loop for de 1 até vezes_repetir

    print(f"\nResultado Final Aproximado (após {vezes_repetir} operações): {valor_aproximado_acumulado:.4f}") 

    erro_abs_total = calcular_erro_abs(valor_exato_total, valor_aproximado_acumulado) 
    erro_relat_total = calcular_erro_relat(valor_exato_total, valor_aproximado_acumulado) 
    
    print("")
    print(f"Erro Absoluto Total: |{valor_exato_total:.7f} - {valor_aproximado_acumulado:.7f}| = {erro_abs_total:.7f}") 
    print(f"Erro Relativo Total: |{erro_abs_total:.7f} / {valor_aproximado_acumulado:.7f}| = {erro_relat_total:.4f} (ou {erro_relat_total * 100:.4f}%).") 

# Função Menu para que o usuário fique num loop para testes de cada tipo de propragação de erros 
def main_menu(): # Def, menu principal que chama todos os exemplos e funções 
    while True: 
        print(f"{COLOR_BLUE}{COLOR_BOLD}\n--- Escolha um Exemplo para Simular a Propagação de Erros ---{COLOR_RESET}") 
        print(f"{COLOR_GREEN}1. Operação Simples{COLOR_RESET}") 
        print(f"{COLOR_GREEN}2. Propagação de Erro e Cancelamento Subtrativo{COLOR_RESET}") 
        print(f"{COLOR_GREEN}3. Propagação de Erro em uma Sequência de Operações{COLOR_RESET}") 
        print(f"{COLOR_YELLOW}0. Sair{COLOR_RESET}") 
        print("") 

        escolha = input(f"{COLOR_BLUE}Digite o número da sua escolha: {COLOR_RESET}") 

        if escolha == '1': 
            exemplo1_operacao_simples() 
        elif escolha == '2': 
            exemplo2_cancelamento_subtrativo() 
        elif escolha == '3': 
            exemplo3_sequencia_somas() 
        elif escolha == '0': 
            print(f"{COLOR_YELLOW}Saindo do simulador. Até mais!{COLOR_RESET}") 
            break 
        else: 
            print(f"{COLOR_RED}Escolha inválida. Por favor, digite 1, 2, 3 ou 0.{COLOR_RESET}") 

# Startar o menu para chamar todo o código se o script for rodado diretamente 
if __name__ == "__main__": 
    main_menu() 
    # Chama função

