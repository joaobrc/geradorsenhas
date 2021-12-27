import random
""" 
Gerador de senhas em python 
Versão : 0.0.1
Status : Desenvolvimento 
Authores : MPA / JBC 
"""

# Gerar uma lista Ter uma lista de Letras maiúsculas 
def Char_uppercase_lists(): 
    return ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# Gerar uma lista de Letras minusculas 
def Char_lowercase_lists(): 
    return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Gerar uma lista de numeros 
def Char_numbers_list():  
    return ['1',"2","3","4","5","6","7","8","9","0"]


# Gerar uma lista de Caracteres especiais 
def Char_especial_list():  
    return ['!',"@","#","$","%","&","*","(",")","-","+",".",",","<",">","[","]","{","}"," "]



# Gerar numeros aleatórios entre 0 e e o tamanho da chave 
def chose_id_in_list(chaves):
    return random.randint(0,len(chaves)-1) # Identifica o tamanho da chave e passa um número aleatório entre 0 e esse tamanho 


def gerador_senhas(arquivo):
    #Lendo os parametros
    with open(arquivo, "r", encoding="UTF-8") as parametros:
        linhas = parametros.readlines()
    
    # Definindo variaveis importantes 
    parametros = {}
    listas_usadas = []
    lista_senhas = []
    senha = ""

    # Colocando os parametros dentro de um dicionario 
    for x in range(len(linhas)):
        linhas[x] = linhas[x].replace('\n',"")
        separados = linhas[x].split(" = ")
        parametros[separados[0]] = separados[1]
    
    # Definindo a lista de caracters de acordo com os parametros
    if parametros['Numéricos'] == "S": 
        listas_usadas.append(Char_numbers_list())
    if parametros['Maiúsculas'] == "S": 
        listas_usadas.append(Char_uppercase_lists())
    if parametros['Minusculas'] == "S": 
        listas_usadas.append(Char_lowercase_lists())
    if parametros['Especiais'] == "S": 
        listas_usadas.append(Char_especial_list())

    # Gerando as senhas com base nos parametros 
    for senhas in range(int(parametros["Quantidade_senhas"])):
        for digitos in range(int(parametros["Tamanho_Máximo"])):
            # Escolher uma lista aleatória dentro de listas_usadas 
            lista = listas_usadas[chose_id_in_list(listas_usadas)]
            # Escolher um char aleatório dentro da lista escolhida
            senha = senha + lista[chose_id_in_list(lista)]
        lista_senhas.append(senha)
        senha = ""
    return lista_senhas
