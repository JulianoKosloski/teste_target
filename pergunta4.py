"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

	SP – R$67.836,43
	RJ – R$36.678,66
	MG – R$29.229,88
	ES – R$27.165,48
	Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""

faturamentoPorEstado = [{"estado": "SP", "valor": 67836.43},
                        {"estado": "RJ", "valor": 36678.66}, 
                        {"estado": "MG", "valor": 29229.88}, 
                        {"estado": "ES", "valor": 27165.48},
                        {"estado": "Outros", "valor": 19849.53}]

def repPorEstado(faturamento):

    total = 0

    for fat in faturamento:
        if (fat['estado'] == "SP"):
            perSP = fat['valor']
        elif (fat['estado'] == "RJ"):
            perRJ = fat['valor']
        elif (fat['estado'] == "MG"):
            perMG = fat['valor']
        elif (fat['estado'] == "ES"):
            perES = fat['valor']
        elif (fat['estado'] == "Outros"):
            perOutros = fat['valor']

        total += fat['valor']
    
    perSP = perSP / total
    perRJ = perRJ / total
    perMG = perMG / total
    perES = perES / total
    perOutros = perOutros / total

    return perSP, perRJ, perMG, perES, perOutros


perSP, perRJ, perMG, perES, perOutros = repPorEstado(faturamentoPorEstado)

# valores convertidos para int para fins de apresentacao
print("Porcentagem SP = " + str(int(perSP * 100)) + "%")
print("Porcentagem RJ = " + str(int(perRJ * 100)) + "%")
print("Porcentagem MG = " + str(int(perMG * 100)) + "%")
print("Porcentagem ES = " + str(int(perES * 100)) + "%")
print("Porcentagem Outros = " + str(int(perOutros * 100)) + "%")
