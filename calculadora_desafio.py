def calculadora():
    while True:
        print("Calculadora Simples:")
        print()
        print("1. soma ")
        print("2. subtração ")
        print("3. multiplicação ")
        print("4. Divisão ")
        print("S. sair   " )
        operacao = input("Selecione uma opção ou S para sair  ")

        if operacao == 'S' or operacao == 's':
            print("obrigado por utilizar a calculadora simples!")
            break
        if operacao not in ['1','2','3','4']:
            print("operação invalida! tente novamente")
            continue

        numero_1 = float(input("primeiro numero: "))
        numero_2 = float(input("segundo numero: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação soma é: ", resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("o resultado da subtração é: ", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("o resulatado da multiplicação é : ", resultado)
        else:
            if numero_2 == 0:
                print("Divisão por zero não são possiveis. Tente novamente.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O seultado da divisão é: ", resultado)

calculadora()




