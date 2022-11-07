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


    def win_v1(f, user):
        def check_line(a1, a2, a3, user):
            if a1 == user and a2 == user and a3 == user:
                return True
            for n in range(3):
                if check_line(f[n][0], f[n][1], f[n][2], user) or \
                        check_line(f[0][n], f[1][n], f[2][n], user) or \
                        check_line(f[0][0], f[1][1], f[2][2], user) or \
                        check_line(f[2][0], f[1][1], f[0][2], user):
                    return True
            return False

        win_v1(field, user)
