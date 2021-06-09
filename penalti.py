#importando a funcao random:
import random

#FUNCOES:
#verifica_chute: recebe as escolhas do chute e goleiro e retorna se foi erro ou acerto.
def verifica_chute(chute, goleiro):
    #gabarito:   O - gol          X - errou
    acerto = "O"
    erro = "X"
    if chute == goleiro:
        print("O goleiro defendeu!!!!")
        return erro
    else:
        #criando um caso onde o jogador possa chutar p/ fora do gol:
        chuteErrado = random.randint(1,100)     #funcao random() que seleciona um valor entre 1 e 100
        if chuteErrado >= 65:
            print("Chute pra fora!!!")
            return erro
        else:
            print("GOOOOOOLLLL!!!")
            return acerto

#texto_escolhas: mostra as escolhas possiveis na tela.
def texto_escolhas():
    print("Escolha o canto:")
    print("\t0 - Direita")
    print("\t1 - Meio")
    print("\t2 - Esquerda")

#variaveis:
vez = True          #usado para trocar a ordem de chute
placarJogador = []
placarBot = []
rodadas = 0


#JOGO:
print("DISPUTA DE PENALTIS:\n")
#loop while que para somente o numero de rodadas chegar a 5
while(rodadas<5):
    #caso if "vez = True" o Jogador chuta, e o Bot chuta caso contrario:
    if vez == True:
        print("Vez de Chutar :")
        #imprimindo as escolhas:
        texto_escolhas()
        #input da escolha do jogador:
        escolhaJogador = str(input("Insira o canto: "))
        #usando a funcao random para a escolha do bot:
        escolhaBot = random.randint(0, 2)
        #adicionando a lista o resultado do chute(O ou X):
        placarJogador.append(verifica_chute(escolhaJogador, escolhaBot))
        #trocando a vez:
        vez = not vez 
        #imprimindo o placar ao vivo:
            #print("PLACAR:")
            #print("Jogador: " , placarJogador)
            #print("Bot: " ,  placarBot)
    else:
        print("Vez de Defender:")
        #imprimindo as escolhas:
        texto_escolhas()
        #input da escolha do jogador:
        escolhaJogador = str(input("Insira o canto: "))
        #usando a funcao random para a escolha do bot:
        escolhaBot = random.randint(0, 2)
        #adicionando a lista o resultado do chute(O ou X):
        placarBot.append(verifica_chute(escolhaBot, escolhaJogador))
        #trocando a vez:
        vez = not vez
        #incrementando o numero de rodadas:
        rodadas += 1
        #imprimindo o placar ao vivo:
        print("PLACAR:")
        print("Jogador: " , placarJogador)
        print("Bot: " , placarBot)

#imprimindo o placar final:     
print("FIM DE JOGO:")
#funcao "nome_da_lista".count(): conta e mostra o numero de caracteres iguais ao dentro do parenteses.
print("Jogador " , placarJogador.count("O"), " X ", placarBot.count("O") , " Bot")
