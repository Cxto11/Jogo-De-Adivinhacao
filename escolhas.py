import modo1
import modo2

print("Olá, seja bem vindo ao meu primeiro jogo.")
print("***************")
print("Teremos dois modos do mesmo jogo de adivinhação")
print("***************")
print("Digite (1) para definir o modo de adivinhação com a soma de dois números.")
print("Digite (2) Para o modo de adivinhação simples")
modo = int(input("Defina o modo de jogo: "))

if modo == 1:
    modo1.jogar()
elif modo == 2:
    modo2.jogar()