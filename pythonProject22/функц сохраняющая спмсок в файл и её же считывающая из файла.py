import json


def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)



a= [
    {1 :2},
    {"b": "c"},
    "1234565",
    123
]
save_info(a)