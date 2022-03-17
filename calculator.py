# Tiago @ SmartNinja
# 02 Março 2022
# exercicio 8.3 calculadora

def soma(x=0, y=0):
    return x+y

def subtr(x, y):
    return x-y


while True:
    fir = int(input("Introduza um valor"))
    sec = int(input("Introduza um valor"))
    opr = input("Qual a operação, escolha uma das opções: +, -, *, /")

    if opr == "+":
        print(soma(fir, sec))
    elif opr == "-":
        print(subtr(fir, sec))
    elif opr == "*":
        print(fir*sec)
    elif opr == "/":
        print(fir/sec)
    else:
        print("não sei o que tu queres, mas o IKEA deve ter")



