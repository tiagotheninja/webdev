# listas : tipo de dados estruturado ORDENADO
list_of_numbers = []

new_number = None
while new_number != 0:
    new_number = int(input("Introduza novo numero>"))
    list_of_numbers.append(new_number)


print(list_of_numbers.pop())
print(list_of_numbers.pop())

total = 0
for elem in list_of_numbers:
    total = total + elem
print("o total da soma é: " + str(total))
