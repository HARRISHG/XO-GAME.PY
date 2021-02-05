def my_board(b):
    print(b[7] + '|' + b[8] + '|' + b[9])
    print('___')
    print(b[4] + '|' + b[5] + '|' + b[6])
    print('___')
    print(b[1] + '|' + b[2] + '|' + b[3])



def marker():
    m = 'w'
    while m != 'o' or m != 'x':
        m = input('enter the marker u need(only in small letter):')
        if m.lower() == 'x':
            print('''player1:x
player2 :o''')
            break
        elif m.lower() == 'o':
            print('''player1:o
player2:x''')
            break
        else:
            print('invalid marker')
    return m


def i_value():
    i = int(input('enter the index:'))
    return i


def a_value(b,i,m):
    if b[i] == ' ':
        b[i] = m
    else:
        print('it is already occpied')
    return b


def c_marker(m):
    if m == 'o':
        return 'x'
    elif m == 'x':
        return 'o'


def no_space(b):
    return ' ' in b


def already_placed(i,b):
    return b[i].lower() == 'o' or b[i].lower() == 'x'


def win_check(b,mark):
    return ((b[7] == mark and b[8] == mark and b[9] == mark) or  # across the top
            (b[4] == mark and b[5] == mark and b[6] == mark) or  # across the middle
            (b[1] == mark and b[2] == mark and b[3] == mark) or  # across the bottom
            (b[7] == mark and b[4] == mark and b[1] == mark) or  # down the middle
            (b[8] == mark and b[5] == mark and b[2] == mark) or  # down the middle
            (b[9] == mark and b[6] == mark and b[3] == mark) or  # down the right side
            (b[7] == mark and b[5] == mark and b[3] == mark) or  # diagonal
            (b[9] == mark and b[5] == mark and b[1] == mark))


b = ['3',' ',' ',' ',' ', ' ',' ',' ',' ',' ']
my_board(b)
m = marker()
i = 0
while ' ' in b:
    i += 1
    if i % 2 == 1:
        k = i_value()
        a = a_value(b,k,m)
        my_board(a)
        if win_check(a, m):
            print(f'{m} got won')
            break
        else:
            continue

    elif i % 2 == 0:
        k = i_value()
        h = c_marker(m)
        a = a_value(b, k, h)
        my_board(a)
        if win_check(a, h):
            print(f'{h} got won')
            break
        else:
            continue


if win_check(a,m) != True and win_check(a,h) != True:
    print('it is draw')
