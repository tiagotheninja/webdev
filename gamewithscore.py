# Tiago @ SmartNinja
# 07 Março 2022
import random

secret = random.randint(1,10)
guess = None
attempts = 0

scorefile = open("score.txt", "r")
scorename = scorefile.readline()
scorevalue = scorefile.readline()
print("O ultimo jogador foi " + scorename + " ganhou à " + scorevalue + " tentativa")
scorefile.close()

while secret != guess and attempts < 3:
    guess = int(input("Introduza o numero a adivinhar"))
    if secret == guess:
        print("CERTO!!")
    elif secret < guess:
        print("O numero é menor que " + str(guess))
    else:
        print("O numero é maior que " + str(guess))
    attempts += 1
    print("Já tentas-te: " + str(attempts) + " vezes.")

if secret != guess and attempts == 4:
    print("Game over, é o fim da linha! Tchauzinho")

if attempts < int(scorevalue):
    scorefile = open("score.txt", "w")
    playername = input("Introduza o seu nome")
    scorefile.write(playername + "\n" + str(attempts))
    scorefile.close()
