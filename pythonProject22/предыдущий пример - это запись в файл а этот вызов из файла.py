import json


def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)



def load_info():
    with open("info.json") as f:
        info = json.load(f)

        return info


info = load_info()
print(info)