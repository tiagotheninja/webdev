# Tiago @ SmartNinja
# 07 Março 2022
import random

secret = random.randint(1,3)
guess = None

for attempts in range(3):
    guess = int(input("Introduza o numero a adivinhar"))
    if secret == guess:
        print("CERTO!!")
        break
    elif secret < guess:
        print("O numero é menor que " + str(guess))
    else:
        print("O numero é maior que " + str(guess))

    print("Já tentas-te: " + str(attempts+1) + " vezes.")

if secret != guess and attempts == 3:
    print("Game over, é o fim da linha! Tchauzinho")
