bodycount = {
    'Проклятие Черной жемчужины': {
        'человек': 17
    },

    'Сундук мертвеца': {
        'человек': 56,
        'раков-отшельников': 1
    },

    'На краю света': {
        'человек': 88
    },

    'На странных берегах': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}
dead = 0
for info in bodycount.values():
    # print(info)
    dead += sum(info.values())

print(dead) 