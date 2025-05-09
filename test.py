import json

decoder = json.JSONDecoder()

with open("./src/data/skills.json", "r") as f:
    data = f.read()
    f.close()
    data = decoder.decode(data)

    for i in data.get("skills"):
        print("Name =", i.get("type"))
        for j in i.get("list"):
            print(j)