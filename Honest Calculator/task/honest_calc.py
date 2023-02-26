M = '0'  # variable for memory value


def main(memory='0'):
    print(message(0))

    calc = input().split()
    if len(calc) != 3:
        main()
    else:
        x, oper, y = calc

        x = memory if x == 'M' else x
        y = memory if y == 'M' else y

        if num_checker(x, y):
            if oper_checker(oper):
                lazy_check(float(x), oper, float(y))
                calculator(x, oper, y)


def message(arg):
    if arg == 0:
        msg = "Enter an equation"
    elif arg == 1:
        msg = "Do you even know what numbers are? Stay focused!"
    elif arg == 2:
        msg = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif arg == 3:
        msg = "Yeah... division by zero. Smart move..."
    elif arg == 4:
        msg = "Do you want to store the result? (y / n):"
    elif arg == 5:
        msg = "Do you want to continue calculations? (y / n):"
    elif arg == 6:
        msg = " ... lazy"
    elif arg == 7:
        msg = " ... very lazy"
    elif arg == 8:
        msg = " ... very, very lazy"
    elif arg == 9:
        msg = "You are"
    elif arg == 10:
        msg = "Are you sure? It is only one digit! (y / n)"
    elif arg == 11:
        msg = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif arg == 12:
        msg = "Last chance! Do you really want to embarrass yourself? (y / n)"

    return msg


def num_checker(x, y):
    x = x.replace('.', '')
    y = y.replace('.', '')

    if x.isdigit() and y.isdigit():
        return True
    else:
        print(message(1))
        main()


def oper_checker(oper):
    if oper in ['+', '-', '*', '/']:
        return True
    else:
        print(message(2))
        main()


def calculator(x, oper, y):
    x = float(x)
    y = float(y)
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print(message(3))
            main()
    print(result)
    memo(result)


def memo(arg):
    answer = input(message(4)).lower()
    while answer not in ['y', 'n']:
        answer = input(message(4)).lower()
    else:
        if answer == 'y':
            if is_one_digit(arg):
                msg_index = 10
                while msg_index < 13:
                    answer = input(message(msg_index)).lower().strip()
                    while answer not in ['y', 'n']:
                        answer = input(message(msg_index)).lower().strip()
                    else:
                        if answer == 'y':
                            msg_index += 1
                        else:
                            answer = 'n'
                            break
        if answer == 'y':
            global M
            M = str(arg)

        answer_2 = input(message(5)).lower()
        while answer_2 not in ['y', 'n']:
            answer_2 = input(message(5)).lower()
        else:
            if answer_2 == 'y':
                main(M)
            else:
                quit()


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def lazy_check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v3):
        msg += message(6)
    if (v1 == 1 or v3 == 1) and v2 == '*':
        msg += message(7)
    if (v1 == 0 or v3 == 0) and v2 in ['*', '+', '-']:
        msg += message(8)

    if msg != '':
        print(message(9) + msg)



main()
