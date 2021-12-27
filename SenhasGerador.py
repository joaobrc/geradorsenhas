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
            print(textos.Processando())
            x = 0
            for novas_senhas in senhas.gerador_senhas(os.path.join(os.getcwd(),"Parametros.txt")): 
                x = x+1
                print("Senha numero {}".format(x) + textos.Cor_amarelo() +  novas_senhas + textos.Cor_padrao())
            os.system("PAUSE")
        
        # Quando escolher a opção de configuração vamos editar o arquivo TXT de configs  
        if op01 == "2":
            op02 = input("informe quantas senhas deseja gerar : ")
            op03 = input("informe Tamanho Minimo da senha : ")
            op04 = input("informe Tamanho Maximo da senha : ")
            op05 = (input("Vai ter Numéricos na senha? S - Simm , N - Não: ")).upper()
            op06 = (input("Vai ter Maiúsculas na senha? S - Simm , N - Não: ")).upper()
            op07 = (input("Vai ter Minusculas na senha? S - Simm , N - Não: ")).upper()
            op08 = (input("Vai ter Especiais na senha? S - Simm , N - Não: ")).upper()
            # Verifica se o foi escolhida uma quantidade maior que 0 
            while textos.validar_opcoes(op02,1) == False:
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op02 = input("Parametro Quantidade incorreto por favor informe quantas senhas deseja gerar: ")
            # Verificar se foi escolhido um numero miimo aceitavel: 
            while textos.validar_opcoes(op03,5) == False:
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op03 = input("Parametro Tamanho_minimo incorreto Não pode ser menor que 5 ou letras .... \n por favor informe Tamanho Minimo da senha: ")
            # Verifica se foi escolhido um nuemro maximo aceitavel 
            while textos.validar_opcoes(op04,5,256) == False:
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op04 = input("Parametro Tamanho_maximo incorreto Não pode ser menor que 5 ou letras ou aior que 256.... \n por favor informe Tamanho Maximo da senha: ")
            # Verifica se foi escolhido um opção valida para numerico S ou N 
            while op05 != "S" and op05 != "N":
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op05 = (input("Parametro Char_Numerico incorreto informar S para sim ou N para Não ....\nPor favor informe Vai ter Numéricos na senha? S - Simm , N - Não: ")).upper()
            # Verifica se foi escolhido um opção valida para Maiusculas S ou N 
            while op06 != "S" and op06 != "N":
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op06 = (input("Parametro Char_Maiusculo incorreto informar S para sim ou N para Não ....\nPor favor informe Vai ter Maiúsculas na senha? S - Simm , N - Não: ")).upper()
            # Verifica se foi escolhido um opção valida para Minusculas  S ou N 
            while op07 != "S" and op07 != "N":
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op07 = (input("Parametro Char_Minusculas incorreto informar S para sim ou N para Não ....\nPor favor informe Vai ter Minusculas na senha? S - Simm , N - Não: ")).upper()
            # Verifica se foi escolhido um opção valida para Especiais  S ou N 
            while op08 != "S" and op08 != "N":
                textos.limpar_tela()
                print(textos.Menu_titulo())
                op08 = (input("Parametro Char_Especiais incorreto informar S para sim ou N para Não ....\nPor favor informe Vai ter Especiais na senha? S - Simm , N - Não: ")).upper()
            with open("Parametros.txt","w", encoding= "UTF-8") as parametros:
                parametros.write("Quantidade_senhas = {}\nTamanho_mínimo = {}\nTamanho_Máximo = {}\nNuméricos = {}\nMaiúsculas = {}\nMinusculas = {}\nEspeciais = {}".format(op02,op03,op04,op05,op06,op07,op08))
