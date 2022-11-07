#field = [[" "] * 3 for i in range(3) ]# создаём массив из 9 цифр.

#print(field)
field = [['-',] * 3 for _ in range(3)]
#print(*field)-'*'-это оператор распаковки

#print('  0 1 2')
#for i in range (len(field)):
 #   print(str(i),*field[i])
#print('  0 1 2')
#for i in range(len(field)):

 #   print(str(i)+ ' '+' '.join(field(i)))- не работает!

#num='  a b c'
#print(num)
#for row,i in zip(field,num.split()):
#    print(f'{i} {' '.join(str(i) for i in row)}')

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+ ' '+' '.join(field[i]))
show_field(field)

def user_input(f):
    while True:
        place = input(' Введите координаты:').split()
        if len(place) !=2:
            print(' Введите две координаты')
            continue

        if not(place[0]. isdigit() and place[1]. isdigit()):
            print(' Введите числа')
            continue
        x,y=map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print(' Вы вышли из диапазона')
            continue
        if f[x][y]!='-':
            print(' Клетка занята ')
            continue
        break
    return x,y
user_input(field)


field = [['-'] * 3 for _ in range(3)]
count=0
while True:
    if count==9:
        print(' Ничья ')
        break
    if count%2==0:
        user='x'
    else:
        user='0'
    show_field(field)
    x,y= user_input(field)
    field[x][y]=user
    count+=1

def win_v1(f,user):
    def check_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
        for n in range(3):
            if check_line(f[n][0], f[n][1], f[n][2], user) or \
            check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
            check_line(f[2][0], f[1][1], f[0][2], user) :
                return True
        return False
    win_v1 (field,user)

field = [['-'] * 3 for _ in range(3)]
count=0
while True:
    if count==9:
        print(' Ничья ')
        break
    if count%2==0:
        user='x'
    else:
        user='0'
    show_field(field)
    x,y= user_input(field)
    field[x][y]=user
    if win_v1(field, user):
        print(f' Выиграл! {user}')
        show_field(field)
        break
    count +=1