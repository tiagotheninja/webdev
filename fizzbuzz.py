until = int(input("Introduza um numero de 1 a 100"))

for x in range(1, until+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)
