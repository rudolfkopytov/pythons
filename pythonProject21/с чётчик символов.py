from collections import  Counter

text = " какой - там текст"

stat = Counter(text)

for s, count in stat.items():
    print(f" Символ '{s}' встретится {count} раз "  )