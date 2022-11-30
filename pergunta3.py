import json

"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
	• O menor valor de faturamento ocorrido em um dia do mês;
	• O maior valor de faturamento ocorrido em um dia do mês;
	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

data = open("dados.json") #abre o arquivo JSON
faturamentoMensal = json.load(data) #guarda os dados em uma variavel
print(faturamentoMensal) #imprime os dados completos 

def analiseFaturamento(vetor):
    soma = 0
    dias = 0
    diasSup = 0
    menor = vetor[0]['valor']
    maior = vetor[0]['valor']

    for valorDia in vetor:
        if (valorDia['valor'] == 0):
            continue
        else:

            if (valorDia['valor'] > maior):
                maior = valorDia['valor']
            elif (valorDia['valor'] < menor):
                menor = valorDia['valor']

            soma += valorDia['valor']
            dias += 1
    
    media = soma / dias

    for valorDia in vetor:

        if (valorDia['valor'] > media):
            diasSup += 1

    return media, maior, menor, diasSup

mediaMensal, maiorValor, menorValor, diasFaturamentoSuperior = analiseFaturamento(faturamentoMensal)

print("Essa eh a media mensal: " + str(mediaMensal))
print("Esse foi o menor faturamento diario: " + str(menorValor))
print("Esse foi o maior faturamento diario: " + str(maiorValor))
print("Quantidade de dias com faturamento superior a media: " + str(diasFaturamentoSuperior))



