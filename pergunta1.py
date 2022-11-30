"""
Observe o trecho de código abaixo:

	int INDICE = 13, SOMA = 0, K = 0;

	enquanto K < INDICE faça
	{
		K = K + 1;
		SOMA = SOMA + K;
	}

	imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

"""

# vou primeiramente replicar o código acima usando Python

indice = 13
soma = 0
k = 0

while (k < indice):

    k += 1 #esse loop deve rodar 13 vezes, aumentando o valor de k em 1 a cada iteração
    soma += k #soma adiciona o valor de k a cada iteração (soma de todos os numeros de 0 a 13)


# para confirmar o resultado, podemos criar uma função teste
def testeSoma(soma: int) -> bool:
	"""
	Compara dois valores para verificar a soma realizada (0 a 13), retorna True se os valores forem iguais

	params: 
	soma: soma a ser comparada
	"""

	valorTeste = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13

	if (valorTeste == soma):
		print("Passou no teste")
		return True
	else:
		print("Não passou no teste")
		return False

print (soma) #imprime 91 na tela
testeSoma(soma)


