# JSON
import json

# READ JSON FILE
with open("ficheiro.json", "r") as file:
    content = json.loads(file.read())
    print(str(content['jogadores'][1]["points"]))

# 3º jogador: Ana, 1
content['jogadores'].append({
    "name": "Ana",
    "points": 1
})

# WRITE JSON FILE
with open("ficheiro.json", "w") as file:
    file.write(json.dumps(content))
