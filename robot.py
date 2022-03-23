steps = 0
direction = "N"
command = None


def print_status():
    print("O robot já deu " + str(steps) + " passos")
    print("O robot está virado para " + direction)


def print_error():
    print("Comando inválido")


def add_steps():
    global steps
    steps += 1


def turn(l_or_r):
    global direction
    if l_or_r == "left":
        if direction == "N":
            direction = "W"
        elif direction == "W":
            direction = "S"
        elif direction == "S":
            direction = "E"
        else:
            direction = "N"
    else:
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        else:
            direction = "N"


while True:
    command = input("Introduza comando > ")
    if command == "ANDAR":
        add_steps()
    elif command == "VIRAR ESQUERDA":
        turn("left")
    elif command == "VIRAR DIREITA":
        turn("right")
    elif command == "ESTADO":
        print_status()
    else:
        print_error()
