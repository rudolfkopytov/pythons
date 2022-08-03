text = " Какой- то текст"
stat = {}
for s in text:
    if s in stat:
        stat[s]+=1
    else:
        stat[s]=1

for s, count in stat.items():
    print(f" Символ '{s}' встретится {count} раз")