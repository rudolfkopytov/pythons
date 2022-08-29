def plot_stat(data, signs, height = 12):

    for i in range(height):
        if i % 3 ==0 :
            current = max(data) - (max(data) - min(data)) / height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = " "*10
        for num in data:
            if max(data) - (max(data)-min(data))/height*(i+1) < num:
                line += "█   "
            else:
                line += "    "

        print(line)

    print(f"{str(round(min(data), 2)):10}" + "█   " * len(data))
    print(" "*10 + "█   " * len(data))
    line = " "*10
    for sign in signs:
        line += f"{sign:4}"

    print(line)

plot_stat([3, 5, 1, 4],["A","B","C","D"])