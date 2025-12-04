import json

with open('./../textfiles/products.json', 'r') as file:
    data = json.load(file)
    for d in data:
        d["discount"]=5
    print(data)
    with open('./../textfiles/products_discount.json', 'w') as file1:
        file1.write(json.dumps(data,indent=4))