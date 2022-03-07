# Tiago @ SmartNinja
# 07 Março 2022
import random

secret = random.randint(1,10)
guess = None
attempts = 1
while secret != guess and attempts <= 3:
    guess = int(input("Introduza o numero a adivinhar"))
    if secret == guess:
        print("CERTO!!")
    elif secret < guess:
        print("O numero é menor que " + str(guess))
    else:
        print("O numero é maior que " + str(guess))

    print("Já tentas-te: " + str(attempts) + " vezes.")
    attempts = attempts + 1
if secret != guess and attempts == 4:
    print("Game over, é o fim da linha! Tchauzinho")
