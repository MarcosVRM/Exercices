from random import randrange
import jogos

def jogar():
    mensagem_de_abertura()
    gerar_palavra()
    palavra_secreta = gerar_palavra()
    letras_acertadas = ocultar_palavra(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    print("A palavra secreta tem {} letras".format(letras_acertadas.count("_")))

    while not enforcou and not acertou:

        chute = pedir_chute()


        if chute in palavra_secreta:
            marcacao(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)
        acertou = "_" not in letras_acertadas
        enforcou = erros == 7
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    repetir()
    selecao_jogo()

def marcacao(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def pedir_chute():
    chute = input("Qual a Letra?")
    chute = chute.strip().upper()
    return chute

def mensagem_de_abertura():
    print('*' * 27)
    print('Bem vindo ao jogo de Forca!')
    print('*' * 27)

def gerar_palavra():
    arquivo = open("Fruit_list.txt", "r")
    palavras = []
    for x in arquivo:
        palavras.append(x.strip())

    arquivo.close()

    y = randrange(0, len(palavras))
    palavra_secreta = palavras[y].upper()
    return palavra_secreta

def ocultar_palavra(palavra_secreta):
    return ["_" for x in palavra_secreta]

def repetir():
    s = False
    n = False
    while not s and not n:
        print("Gostaria de tentar novamente?\nDigite S para sim e N para Não")
        x = input()
        x = x.strip().upper()
        if x == "S":
            s = True
        elif x == "N":
            n = True
        else:
            print("Por favor utilize S ou N")
    if s:
        jogar()
    elif n:
        print("Obrigado por jogar")

def selecao_jogo():
    s = False

    while not s:
        print("Utilize S para sim e N para Não")
        x =input("Voltar a seleção de jogos?")
        x = x.strip().upper()
        if x == "S":
            jogos.escolhe_jogo()
        elif x == "N":
            s = True

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era: {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == "__main__":
    jogar()