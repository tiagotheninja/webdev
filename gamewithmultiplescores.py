# Tiago @ SmartNinja
# 07 Março 2022
import random
import json


secret = random.randint(1,10)
guess = None
attempts = 0

scorefile = open("multiplescore.json", "r")
score_json = json.loads(scorefile.read())
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

playername = input("Qual o seu nome?")
score_json["SCORES"].append({
    "name": playername,
    "attempts": attempts
})


scorefile = open("multiplescore.json", "w")
scorefile.write(json.dumps(score_json))
scorefile.close()
