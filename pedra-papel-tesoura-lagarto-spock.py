import random

placarj = 0    #placar do jogador
placarc = 0    #placar do computador

i = 0

print ("Bem vindo ao jogo pedra-papel-tesoura-lagarto-spock!!! Quem fizer 3 pontos seguidos primeiro é campeão do jogo!") 

while i==0:

    jogador = str(input("Coloque sua jogada:"))

    computer = random.randint(1,5)
    print ("Tabela de jogadas do computador: 1-Pedra / 2-Papel / 3-Tesoura / 4-Lagarto / 5-Spock")
    
# Denominação das variaveis = 
    if jogador == "pedra":
        jogador = 1
    elif jogador == "papel":
        jogador = 2
    elif jogador == "tesoura":
        jogador = 3
    elif jogador == "lagarto":
        jogador = 4
    elif jogador == "spock":
        jogador = 5
        
#Pedra:
    if jogador == 1:                                
        if (computer == 3 or computer == 4):
            print ("O computador jogou %d"%computer)
            print ("Você ganhou!")
            placarj = placarj + 1
            placarc = placarc * 0 
        if (computer ==2 or computer == 5):
            print ("O computador jogou %d"%computer)
            print ("O computador ganhou!")
            placarc = placarc + 1
            placarj = placarj * 0
        if (computer == 1):
            print ("O computador jogou %d"%computer)
            print ("Empate")
            placarc = placarc * 0
            placarj = placarj * 0
        print ("Novamente:")
        
#Papel:
    if jogador == 2:                                
        if (computer == 1 or computer == 5):
            print ("O computador jogou %d"%computer)
            print ("Você ganhou!")
            placarj = placarj + 1
            placarc = placarc * 0 
        if (computer == 3 or computer == 4):
            print ("O computador jogou %d"%computer)
            print ("O Computador ganhou!")
            placarc = placarc + 1
            placarj = placarj * 0
        if (computer == 2):
            print ("O computador jogou %d"%computer)
            print ("Empate")
            placarc = placarc * 0
            placarj = placarj * 0
        print ("Novamente:")
    
#Tesoura:    
    if jogador == 3:                              
        if (computer == 1 or computer == 4):
            print ("O computador jogou %d"%computer)
            print ("Você ganhou!")
            placarj = placarj + 1
            placarc = placarc * 0 
        if (computer == 2 or computer == 5):
            print ("O computador jogou %d"%computer)
            print ("O computador ganhou!")
            placarc = placarc + 1
            placarj = placarj * 0
        if (computer == 3):
            print ("O computador jogou %d"%computer)
            print ("Empate")
            placarc = placarc * 0
            placarj = placarj * 0
        print ("Novamente:")
        
#Lagarto:   
    if jogador == 4:                              
        if (computer == 2 or computer == 5):
            print ("O computador jogou %d"%computer)
            print ("Você ganhou!")
            placarj = placarj + 1
            placarc = placarc * 0 
        if (computer == 1 or computer == 3):
            print ("O computador jogou %d"%computer)
            print ("O computador ganhou!")
            placarc = placarc + 1
            placarj = placarj * 0
        if (computer == 4):
            print ("O computador jogou %d"%computer)
            print ("Empate")
            placarc = placarc * 0
            placarj = placarj * 0
        print ("Novamente:")
        
#Spock        
    if jogador == 5:                              
        if (computer == 1 or computer == 3):
            print ("O computador jogou %d"%computer)
            print ("Você ganhou!")
            placarj = placarj + 1
            placarc = placarc * 0 
        if (computer == 2 or computer == 4):
            print ("O computador jogou %d"%computer)
            print ("O computador ganhou!")
            placarc = placarc + 1
            placarj = placarj * 0
        if (computer == 5):
            print ("O computador jogou %d"%computer)
            print ("Empate")
            placarc = placarc * 0
            placarj = placarj * 0
        print ("Novamente:")
            
# Placares = 
    if placarj < 3:
        i = 0
    elif placarj == 3:
        print ("Você é campeão!!!!!!!!!")
        i = 1
        i = int(input("Para jogar novamente pressione 0"))
        
    if placarc < 3:
        i = 0
    elif placarc == 3:
        print ("O computador é campeão!!!!!!!!!!!!Game Over")
        i = 1
        i = int(input("Para jogar novamente pressione 0:\n"))
        
        