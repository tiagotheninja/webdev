# calculadora de idade

ano_corrente = 2022
ano_nascimento = int(input("Introduza o ano de nascimento"))
ja_festejou = input("Já fez anos neste ano?")

if ja_festejou == "sim":
    idade = ano_corrente - ano_nascimento
else:
    idade = ano_corrente - ano_nascimento - 1

print("A idade é: "+str(idade))

if idade > 100:
    print("Mas isto agora é tudo centenário? Ai ai...")

x = 8
y = 10

if x < 10:
    print("o x é inferior a 10")
elif y == 10:
    print("o y é igual a 10")
