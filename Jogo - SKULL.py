def jogo_de_perguntas_com_dicas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    print("Tente adivinhar onde eu 'moro'.")

    resposta_correta = "no caixão"
    tentativas = 3

    dicas = [
        "Dica 1: Eu fico em um lugar onde ninguém quer ficar depois da meia-noite ☠︎︎ ☠︎︎ ☠︎︎.",
        "Dica 2: As pessoas perdem peso muito rápido por aqui",
        "Dica 3: Muito apertado, quase claustrofóbico... e o teto fica a 3 cm do meu rosto."
    ]

    for i in range(tentativas):
        resposta = input(f"Você tem {tentativas - i} tentativa(s). Onde eu moro? ")

        if resposta.lower() == resposta_correta:
            print("Parabéns! Você acertou. Eu já morri!")
            break
        else:
            if i < len(dicas):
                print(f"Resposta errada. {dicas[i]}")
            else:
                print("Resposta errada. Só são essas 3 meu bem.")

        if i == tentativas - 1:
            print("Acho que é o fim da linha. A resposta correta é: Eu moro no caixão.")

# Executar o jogo
jogo_de_perguntas_com_dicas()