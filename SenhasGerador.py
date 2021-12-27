import Functioons.keegenerator as senhas
import Functioons.textos as textos
import os

# Declaração de variáveis
op01 = ""


# Imprimindo tela do sistema 
while op01 != "0":
    textos.limpar_tela()
    print(textos.Menu_titulo())
    print(textos.Menu_inicial())

    # Validando opção escolhida 
    op01 = input("Digite a opção desejada: ")
    if textos.validar_opcoes(op01,0,2):
        if op01 == "1":
            print(textos.Cor_amarelo() +  senhas.gerador_senhas() + textos.Cor_padrao())
            os.system("PAUSE")
    
