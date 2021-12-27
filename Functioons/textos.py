""" 
Gerador de senhas em python 
Versão : 0.0.1
Status : Desenvolvimento 
Authores : MPA / JBC 
"""

import os


def Cor_amarelo():
    return " \033[33m "


def Cor_padrao():
    return " \033[m "


def Menu_titulo():
    texto = """\033[33m
------------------------------------------------------------------------------------------------------------------------------------------------------------
  ####    ######   #####      ##     ####      ####    #####             ####     ######             ####    ######   ##  ##   ##  ##     ##      ####
 ##  ##   ##       ##  ##    ####    ## ##    ##  ##   ##  ##            ## ##    ##                ##  ##   ##       ### ##   ##  ##    ####    ##  ##
 ##       ##       ##  ##   ##  ##   ##  ##   ##  ##   ##  ##            ##  ##   ##                ##       ##       ######   ##  ##   ##  ##   ##
 ## ###   ####     #####    ######   ##  ##   ##  ##   #####             ##  ##   ####               ####    ####     ######   ######   ######    ####
 ##  ##   ##       ####     ##  ##   ##  ##   ##  ##   ####              ##  ##   ##                    ##   ##       ## ###   ##  ##   ##  ##       ##
 ##  ##   ##       ## ##    ##  ##   ## ##    ##  ##   ## ##             ## ##    ##                ##  ##   ##       ##  ##   ##  ##   ##  ##   ##  ##
  ####    ######   ##  ##   ##  ##   ####      ####    ##  ##            ####     ######             ####    ######   ##  ##   ##  ##   ##  ##    ####
------------------------------------------------------------------------------------------------------------------------------------------------------------\033[m"""
    return texto


def Menu_inicial():
    texto = """
Digite uma das opções abaixo: 
\033[33m [1] \033[m - Gerar senhas novas 
\033[33m [2] \033[m - Configurações 
\033[33m [0] \033[m - Sair e fechaar o programa 
------------------------------------------------------------------------------------------------------------------------------------------------------------"""
    return texto


def Menu_opcoes_invalidas():
    texto = """ Opção invalida por favor escolha uma opção valida  """
    return texto


def validar_opcoes(opcao,menor=0,maior=1000):
    try:
        if int(opcao) not in range(menor,maior+1):
            print("a opcao digitada foi : {} não existem parametros pra essa opção escolha uma opção entre {} e {}.".format(opcao, menor, maior))
            os.system("PAUSE")
            return False
    except:
        print("a opcao digitada foi : {} não existem parametros pra essa opção escolha uma opção entre {} e {}.".format(opcao, menor, maior))
        os.system("PAUSE")
        return False
    return True


def limpar_tela():
    os.system("CLS")


def Processando():
    return "Processando Dados e configurações"
