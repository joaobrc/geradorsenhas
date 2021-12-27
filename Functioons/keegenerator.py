import random
""" 
Gerador de senhas em python 
Versão : 0.0.1
Status : Desenvolvimento 
Authores : MPA / JBC 
"""

# Etapa 01 - Lista 00 - Ter uma lista de Letras maiúsculas 
def Char_uppercase_lists(): # Retorna uma lista com letras minúsculas 
    return ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# Etapa 02 - Lista 01 - Ter uma lista de Letras minusculas 
def Char_lowercase_lists(): # Retorna uma lista com letras minusculas 
    return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Etapa 03 - Lista 02 - Ter uma lista de numeros 
def Char_numbers_list(): # Retorna uma lista com numeros 
    return ['1',"2","3","4","5","6","7","8","9","0"]


# Gerar numeros aleatórios entre 0 e e o tamanho da chave 
def chose_id_in_list(chaves):
    return random.randint(0,len(chaves)-1) # Identifica o tamanho da chave e passa um número aleatório entre 0 e esse tamanho 


def gerador_senhas(quantidade_digitos = 5):
    listas_usadas = [
        Char_uppercase_lists(),
        Char_lowercase_lists(),
        Char_numbers_list()
    ]
    senha = ""
    # Repetir o comandos até que forme a senha 
    for x in range(quantidade_digitos):
        # Escolher uma lista aleatória dentro de listas_usadas 
        lista = listas_usadas[chose_id_in_list(listas_usadas)]
        # Escolher um char aleatório dentro da lista escolhida
        senha = senha + lista[chose_id_in_list(lista)]
    return senha
