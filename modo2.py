def jogar():
    import random

    parada = 1

    def win():     
        print("Párabens, você acertou o número e fez {} pontos" .format(pontos)) 
        print("fim de jogo")
        print("Iniciar nova partida?\n (1)sim\n (0)não")

    def lose():
        print("Você perdeu!")
        print("Iniciar nova partida?\n (1)sim\n (0)não")  

    def chute_maior():
        print("Tente um número maior ")

    def chute_menor():
        print("Tente um número menor: ")

    while parada == 1:
        print("Você escolheu o modo simples de adivinhação!")
        print("Você deve adivinhar um número de acordo com a dificuldade que escolher!")
        print("Primeiro vamos definir um nível de Dificuldade: " "\n1 = 20 Tentativas e o número pode ser de 1 a 100" "\n2 = 10 Tentativas e o número pode ser de 1 a 50" "\n3= 5 tentativas e o número pode ser de 1 a 10")         
        nivel = int(input("Defina o nivel de dificuldade: "))

        if(nivel == 1):
            pontos = 1000
            numero_tentativas = 20
            num1 = 100
            num_escondido = random.randrange(1,101)
            print("Você escolheu o nivel 1")
            
        if(nivel == 2):
            pontos = 1000 
            num1 = 50
            numero_tentativas = 10
            num_escondido = random.randrange(1,51)
            print("Você escolheu o Nivel 2")

        if(nivel == 3): 
            pontos = 1000
            num1 = 10
            numero_tentativas = 5
            num_escondido = random.randrange(1,11)
            print("Você escolheu o Nivel 3")

        if(nivel < 1 or nivel > 3): 
            print("Você deve definir um nível de dificuldade entre 1 e 3 (Leia a descrição) !!!!!!!!!")  

        for rodada in range (1, numero_tentativas + 1): 
            print("Tentativa {} de {}".format(rodada,numero_tentativas) )
                
            chute  = int(input("Digite um número: "))
            perdeu = rodada == numero_tentativas
            venceu = chute  == num_escondido
            maior  = chute < num_escondido
            menor  = chute > num_escondido
            erro   = chute < 1 or chute > num1

            if(erro):
                print("O número deve ser maior que 1 e menor que {}" .format(num1))

            if (perdeu):
                lose()
                iniciar_nova = int(input())
                parada = iniciar_nova

            elif(venceu):   
                win()             
                iniciar_nova = int(input())
                parada       = iniciar_nova
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