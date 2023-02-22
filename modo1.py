def jogar():
     import random
     parada = 1
     def win():     
          print("Párabens, você acertou o número e fez {} pontos" .format(pontos)) 
          print("fim de jogo")
          print("Iniciar nova partida?\n (1)sim\n (0)não")

     def lose():
          print("Você perdeu! :( Escolha um novo modo de jogo!)")
          print("Iniciar nova partida?\n (1)sim\n (0)não")  

     def chute_maior():
          print("Tente um número maior ")

     def chute_menor():
          print("Tente um número menor: ")

     while parada == 1:
          print("Você selecionou o modo de adivinhação com a soma de dois números.")
          print("*****************************")
          print("Irei escolher um número aleatorio de acordo com o nível de dificuldade escolhido\nSera que pode descobrir qual é o número?")
          print("*****************************")
          print("Como Jogar:")
          print("*****************************")
          print("Você ira escolher 2 números e a soma deles, deve ser = ao número perdido")
          print("*****************************")
          print("Primeiro vamos definir um nível de Dificuldade: " "\n1 = 20 Tentativas e o número pode ser de 1 a 100" "\n2 = 10 Tentativas e o número pode ser de 1 a 50" "\n3= 5 tentativas e o número pode ser de 1 a 10")

          nivel = int(input("Defina o nivel de dificuldade: "))

          if(nivel == 1): 
               pontos = 1000
               num1=100
               numero_tentativas = 20
               num_escondido = random.randrange(1,101)
               print("Você escolheu o Nivel 1")
          if(nivel == 2): 
               pontos = 1000
               num1=50
               numero_tentativas = 10
               num_escondido = random.randrange(1,51)
               print("Você escolheu o Nivel 2")
          if(nivel == 3): 
               pontos = 1000
               num1=10
               numero_tentativas = 5
               num_escondido = random.randrange(1,11)
               ("Você escolheu o Nivel 3")

          if(nivel < 1 or nivel > 3): 
               print("Você deve definir um nível de dificuldade entre 1 e 3 (Leia a descrição) !!!!!!!!!")       

          for rodada in range (1, numero_tentativas + 1):                 
               print("Tentativa {} de {}".format(rodada,numero_tentativas) )

               first = int(input("Digite o primeiro número: "))
               sec   = int(input ("Digite o segundo número: "))
               soma  = first + sec
               acertou = soma == num_escondido
               maior   = soma < num_escondido
               menor   = soma > num_escondido
               perdeu = rodada == numero_tentativas
               erro = soma < 1 or soma > num1

               if(erro): 
                    print("o resultado da soma deve ser um número entre 1 e {}" .format(num1))

               if(acertou): 
                    win()
                    iniciar_nova = int(input())
                    parada = iniciar_nova 
                    break

               elif (perdeu):
                    lose()
                    iniciar_nova = int(input())
                    parada = iniciar_nova 
                    break          
                              
               else:
                    if(maior): 
                         chute_maior()
                    elif(menor): 
                         chute_menor()

               pontos_perdidos = abs( rodada - numero_tentativas)
               pontos = pontos - pontos_perdidos

if(__name__ == "___main___"):
     jogar()