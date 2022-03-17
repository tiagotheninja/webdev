ficheiro = open("database.csv")

for line in ficheiro:
    data = line.split(",")
    print(data[0] + " is " + data[1] + " years old and " + data[2])

ficheiro.close()
