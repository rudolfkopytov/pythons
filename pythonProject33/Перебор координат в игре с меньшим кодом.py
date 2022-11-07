field = [['-',] * 3 for _ in range(3)]
def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+ ' '+' '.join(field[i]))
show_field(field)



def win_v2(f,user):
    win_cord = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,2),(1,1),(2,0)),((0,0),(1,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)))


    for cord in win_cord:
        symbol = []
        for с in cord:
            symbol.append(f[c][0]][c][1])
        if symbol == [user,user,user]:
            return True
    return False

field = [['-',] * 3 for _ in range(3)]
count=0
while True:
    if count == 9:
        print(' Ничья ')
        break
    if count%2==0:
        user='x'
    else:
        user='0'
    show_field(field)
    x, y = user_input(field)

    field[x][y]=user
    if win_v2(field,user):
        print(f' Выиграл {user}')
        show_field(field)
    count+=1
