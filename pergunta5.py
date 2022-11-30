"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
	b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def strReverse(word:str) -> str:
    #recebe uma string e retorna a string reversa

    new_word = ""

    i = len(word)
    while (i > 0): 
        new_word = new_word + word[i-1]
        i -= 1

    print("String invertida: " + new_word)
    return new_word


#testando a funcao
strReverse("Hello")
strReverse("Monty Python")
strReverse("Juliano Kosloski")
strReverse("Anotaram a data da maratona")
