num_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite o seu número:')
    print('Voce digitou', chute_str)
    chute = int(chute_str)

    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto

    if(acertou):
        print('Você acertou!')
        break
    else:
        if(maior):
            print('Você errou!\nSeu chute foi maior que o número secreto.')
        elif(menor):
            print('Você errou!\nSeu chute foi menor que o número secreto.')
    rodada = rodada + 1

print('Fim do jogo!')
