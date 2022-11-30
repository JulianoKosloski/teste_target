"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: 
	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""


def fibo(target: int) -> None: #funcao calcula a sequencia de fibonacci

    fibo = [0, 1]
    indice1 = 0
    indice2 = 1
    resultado = False

    if (target == 0 or target == 1): #retorna se for um dos dois valores iniciais
        print("O número informado está na sequência de Fibonacci!")
        return

    while (resultado != True):
        proximo = fibo[indice1] + fibo[indice2]
        fibo.append(proximo)
        if (target == proximo): #compara se o valor alvo está na lista
            print("O número informado está na sequência de Fibonacci!")
            resultado = True
        elif (target < proximo): #informa se os valores da sequencia ja ultrapassaram o valor informado
            print("O número informado NÃO está na sequência de Fibonacci!")
            resultado = True

        indice1 += 1
        indice2 += 1


# algumas entradas para testar a função
fibo(0) #True
fibo(1) #True
fibo(4) #False
fibo(34) #True
fibo(-13) #False
fibo(27) #False