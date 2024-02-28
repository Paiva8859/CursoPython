# jogo.py
import random
from perguntas import perguntas

def apresentar_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)

def verificar_resposta(pergunta, resposta):
    return resposta.lower() == pergunta["resposta"]

def obter_dica(pergunta):
    return pergunta["dica"]

def jogar():
    premio = 0
    dicas_restantes = 3  # Número máximo de dicas permitidas por partida

    perguntas_disponiveis = perguntas[:]
    random.shuffle(perguntas_disponiveis)

    for pergunta in perguntas_disponiveis:
        apresentar_pergunta(pergunta)

        while True:
            resposta = input("Digite a letra da sua resposta ou 'dica' para pedir uma dica: ")

            if resposta.lower() == "dica" and dicas_restantes > 0:
                print("Dica:")
                print(obter_dica(pergunta))
                dicas_restantes -= 1
            elif resposta.lower() == "dica" and dicas_restantes == 0:
                print("Você não tem mais dicas sobrando!")
            else:
                if verificar_resposta(pergunta, resposta):
                    print("Resposta correta!\n")
                    premio += 1000
                    print(f"Você ganhou R$ {premio}!\n")  
                    continuar = input("Deseja continuar para a próxima pergunta? (s/n): ")
                    if continuar.lower() != "s":
                        return
                    break
                else:
                    print("Resposta incorreta! Tente novamente.")

    print(f"Parabens! Você ganhou R$ {premio}")

if __name__ == "__main__":
    print("Bem-vindo ao Quem Quer Ser um Milionário!")
    print("Responda corretamente a todas as perguntas para ganhar R$ 1.000 cada!")
    print("Digite a letra correspondente à sua resposta ou 'dica' para pedir uma dica.\n")
    jogar()
