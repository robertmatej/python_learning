import json

dictionary = { 'Adam':[23, 'mandela'], 'Janek': [24, "kolarz"]}
lista = ['Anna', 22, True]
strings = 'Jestem napisem,  nie znaczy'

out = json.dumps('co to za jatka')
#print(out)

with open('plik_json1.json', 'w', encoding="utf-8") as file:
    json.dump(dictionary, file)

with open('plik_json2.json', 'w') as file2:
    json.dump(out, file2)

with open('plik_json2.json', 'r', encoding="utf-8") as file3:
    inputs = json.load(file3)
    transform = json.loads(inputs)
    print(f"inputs: {inputs[1]}")
    print(f'transform: {transform[1]}')