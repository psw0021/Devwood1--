import sys

# creating variables needed for this computation
k = dict()
boolean_flag = True


# functions that are going to be used for binomial calculator program
def check_space(b, kl):
    """
    This is a function to check whether or not there exists a space between the integers
    (the value of a variable in which the user has input). Also, it make sures that if the
    entered input does not start with 'def', the function will return 0.
    """
    if kl[0:3] == 'def':
        if b.isnumeric() is False:
            return 1
        if b.isnumeric() is True:
            return 0
    else:
        return 0


def show_var(dictionary):
    """
    This is a function to show the variables entered
    when 'see' is entered by the user.
    """
    print('------Variables-------')
    print('----------------------')
    for key in k:
        print(key, ':', dictionary[key])
    print('----------------------')
    print('----------------------')


def error_find(ip):
    """
    This function is used to check whether or not input entered
    by the user is either quit, see. Also, it will check whether
    or not the input starts with def, see, or calc and quit. If it
    doesn't this function will prompt the user for another input.
    """
    # when the input is neither 'def', 'see', 'calc':
    while ip[0: 3] != 'def' and ip != 'see' and ip[0: 4] != 'calc':
        while ip == 'see':
            show_var(k)
            ip = input('>>> ')
        if ip.lower() == 'quit':
            sys.exit()
        ip = input('>>> ')

    # when the input is in lower case: 'quit', terminate the whole program.
    if ip.lower() == 'quit':
        sys.exit()

    # when the input is 'see', show the graphics of variables using show_var
    # function, and ask the user for another input.
    while ip == 'see':
        show_var(k)
        ip = input('>>> ')
        ip = error_find(ip)
    return ip


def check_variables(var1, globe):
    """
    This is a function for checking whether the variable user
    entered for calculation exists. If the user input integer, it
    is okay. If it is a string, check for the dictionary whether the
    user has defined it or not.
    """
    # first, make sure to check that the user input starts with 'calc'
    if globe[0:4] != 'calc':
        return 0

    # secondly, check to see if the user input is integer. If it is,
    # the function will not look up at the dictionary.
    try:
        int(var1)
        return int(var1)

    # if the process above failed, look up at the dictionary to find
    # a key that the user has input
    except ValueError:
        try:
            k[var1]
            return int(k[var1])

        # if the dictionary does not contain the key required, check
        # if the next input starts with 'calc' and print an error message along with
        # returning numerical value 1
        except KeyError:
            if globe[0:4] == 'calc':
                print('Error : non_existing variable entered')
                return 1
            if globe[0:4] != 'calc':
                return 0


def addition(var1, var2):
    """
    Function for adding the two variables that the user input.
    """
    return int(var1) + int(var2)


def subtraction(var1, var2):
    """
    Function for subtracting the two variables that the user input.
    """
    return int(var1) - int(var2)


def multiplication(var1, var2):
    """
    Function for multiplying the two variables that the user input
    """
    return int(var1) * int(var2)


def division(var1, var2, pi, qw):
    """
    This is a function for computing the division between the two variables.
    It will also check to see whether or not the denominator of the division is
    not zero. If it is, it will print an error message.
    """
    # process of trying to divided the two input. If denominator doesn't contain zero,
    # print out the input and return True
    try:
        var1 / var2
        if var1 % var2 == 0:
            if pi == 1:
                print(int(var1 / var2))
            return True
        if var1 % var2 != 0:
            if pi == 1:
                print(format(var1 / var2, '.3f'))
            return True

    # if the process above resulted in ZeroDivisionError, check to see if another input
    # starts with calc. numeric value pi is used to make sure that error message is not
    # posted every time ZeroDivision error was called.
    except ZeroDivisionError:
        if pi == 0:

            # if it does start with calc, post error message and return False boolean value
            if qw[0:4] == 'calc' and qw.count('/') == 1:
                print('Error: Division by zero')
                return False

            # if it doesn't start with calc, just return the boolean value False
            if y[0:4] != 'calc':
                return False
        if pi == 1:
            return False


# Start --main-- program
# first user input for the binomial calculator program
y = input('>>> ')

# if the lower case of input is not 'quit', keep looping without pause.
while y.lower() != 'quit':

    # if the input is neither 'def', 'see', and 'calc'.
    while y[0:3] != 'def' and y != 'see' and y[0:4] != 'calc':
        y = input('>>> ')
        if y.lower() == 'quit':
            sys.exit()

    # if the user input starts with 'def'
    while y[0:3] == 'def':
        while (y.count('=') >= 2 or y.count('=') == 0) and y[0:3] == 'def':
            print('Error: invalid command')
            y = input('>>> ')
            y = error_find(y)

        # check to see whether the input above starts with 'def'
        if y[0:3] == 'def':
            z = []
            for i in y:
                if i != ' ':
                    z.append(i)
            d = y[3:]
            # below is the process to remove last space and acquire
            # variable name and the value of it

            # variable name
            if d.count(z[z.index('=') - 1]) == 1:
                m = d[d.index(z[3]): d.index(z[z.index('=') - 1]) + 1]
            elif d.count(z[z.index('=') - 1]) != 1:
                p = 0
                list4 = []
                for v in d:
                    if v == z[z.index('=') - 1]:
                        list4.append(p)
                    p = p + 1
                m = d[d.index(z[3]): max(list4) + 1]

            # value of the variable
            if y.count(z[len(z) - 1]) == 1:
                n = y[y.index(z[z.index('=') + 1]): y.index(z[len(z) - 1]) + 1]
            elif y.count(z[len(z) - 1]) != 1:
                q = 0
                list5 = []
                for w in y:
                    if w == z[len(z) - 1]:
                        list5.append(q)
                    q = q + 1
                n = y[y.index(z[z.index('=') + 1]): max(list5) + 1]

            # check to see whether there is a space or string in the value
            # the value should only contain integers
            t = check_space(n, y)
            True_flag = True
            r = 0
            while t != 0 and y[0:3] == 'def':
                print('Error: invalid variable')
                r = r + 1
                y = input('>>> ')
                error_find(y)

                # repeat the process until the correct format of input
                # is entered
                if y[0:3] == 'def':
                    z = []
                    for i in y:
                        if i != ' ':
                            z.append(i)
                    d = y[3:]
                    if d.count(z[z.index('=') - 1]) == 1:
                        m = d[d.index(z[3]): d.index(z[z.index('=') - 1]) + 1]
                    elif d.count(z[z.index('=') - 1]) != 1:
                        p = 0
                        list4 = []
                        for v in d:
                            if v == z[z.index('=') - 1]:
                                list4.append(p)
                            p = p + 1
                        m = d[d.index(z[3]): max(list4) + 1]
                    if y.count(z[len(z) - 1]) == 1:
                        n = y[y.index(z[z.index('=') + 1]): y.index(z[len(z) - 1]) + 1]
                    elif y.count(z[len(z) - 1]) != 1:
                        q = 0
                        list5 = []
                        for w in y:
                            if w == z[len(z) - 1]:
                                list5.append(q)
                            q = q + 1
                        n = y[y.index(z[z.index('=') + 1]): max(list5) + 1]
                    t = check_space(n, y)
                if y[0:3] != 'def':
                    True_flag = False

            # if there are no problem with the format
            # of the input, add the variable name and value to the
            # dictionary
            if y[0:3] == 'def':
                k[m] = n

            if y[0:3] == 'def' and r == 0:
                y = input('>>> ')
                y = error_find(y)

    # if the user input is neither def, see, or calc
    while y[0:3] != 'def' and y != 'see' and y[0: 4] != 'calc':
        while y == 'see':
            show_var(k)
            y = input('>>> ')
        if y.lower() == 'quit':
            sys.exit()

    # if the user input starts with calc
    while y[0:4] == 'calc':

        # check if the input has faulty amount of operators
        while y.count('-') + y.count('+') + y.count('*') + y.count('/') > 1 or \
                y.count('-') + y.count('+') + y.count('*') + y.count('/') == 0\
                and y[0:4] == 'calc':
            print('Error: invalid command')
            y = input('>>> ')
            y = error_find(y)
        second = y.split()

        # if there are no problem with the above process, and
        # if the input starts with 'calc', process the below code
        if y[0:4] == 'calc':
            if y.count('-') == 1:
                a = '-'
            if y.count('+') == 1:
                a = '+'
            if y.count('*') == 1:
                a = '*'
            if y.count('/') == 1:
                a = '/'
            o = []
            for i in y:
                if i != ' ':
                    o.append(i)

            # process of acquiring the first operand
            i = y[4:]
            if i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) == 1:
                variable1 = i[i.index(o[4]): i.index(o[o.index(a) - 1]) + 1]
            elif i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) != 1:
                p = 0
                list4 = []
                for v in i[i.index(o[4]):i.index(a)]:
                    if v == o[o.index(a) - 1]:
                        list4.append(p)
                    p = p + 1
                variable1 = i[i.index(o[4]): max(list4) + 1]

            # process of acquiring the second operand
            c = y[y.index(a) + 1:]
            if c.count(o[len(o) - 1]) == 1:
                variable2 = c[c.index(o[o.index(a) + 1]):c.index(o[len(o) - 1]) + 1]
            elif c.count(o[len(o) - 1]) != 1:
                first = 0
                list6 = []
                for x in c:
                    if x == o[len(o) - 1]:
                        list6.append(first)
                    first = first + 1
                variable2 = c[c.index(o[o.index(a) + 1]): max(list6) + 1]
        if y[0:3] == 'def':
            z = []
            for i in y:
                if i != ' ':
                    z.append(i)
            variable1 = y[y.index(z[3]): y.index(z[z.index('=') - 1]) + 1]
            variable2 = y[-1]

        # process to check whether or not the operand is a valid one
        # if it is an integer, it is okay. If it is a string, check the dictionary
        while check_variables(variable1, y) == 1 or check_variables(variable2, y) == 1:
            y = input('>>> ')
            y = error_find(y)

            # if the new input has faulty amount of operators
            while y.count('-') + y.count('+') + y.count('*') + y.count('/') > 1 or \
                    y.count('-') + y.count('+') + y.count('*') + y.count('/') == 0 \
                    and y[0:4] == 'calc':
                print('Error: invalid command')
                y = input('>>> ')
                y = error_find(y)

            # if the new input is okay
            if y[0:4] == 'calc':
                if y.count('-') == 1:
                    a = '-'
                if y.count('+') == 1:
                    a = '+'
                if y.count('*') == 1:
                    a = '*'
                if y.count('/') == 1:
                    a = '/'
                o = []
                for i in y:
                    if i != ' ':
                        o.append(i)

                # process of acquiring first operand
                i = y[4:]
                if i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) == 1:
                    variable1 = i[i.index(o[4]): i.index(o[o.index(a) - 1]) + 1]
                elif i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) != 1:
                    p = 0
                    list4 = []
                    for v in i[i.index(o[4]):i.index(a)]:
                        if v == o[o.index(a) - 1]:
                            list4.append(p)
                        p = p + 1
                    variable1 = i[i.index(o[4]): max(list4) + 1]

                # process of acquiring second operand
                c = y[y.index(a) + 1:]
                if c.count(o[len(o) - 1]) == 1:
                    variable2 = c[c.index(o[o.index(a) + 1]): c.index(o[len(o) - 1]) + 1]
                elif c.count(o[len(o) - 1]) != 1:
                    first = 0
                    list6 = []
                    for x in c:
                        if x == o[len(o) - 1]:
                            list6.append(first)
                        first = first + 1
                    variable2 = c[c.index(o[o.index(a) + 1]): max(list6) + 1]

        # user input: subtraction
        if y.count('-') == 1:
            print(subtraction(check_variables(variable1, y), check_variables(variable2, y)))
            y = input('>>> ')
            y = error_find(y)

        # user input: addition
        elif y.count('+') == 1:
            print(addition(check_variables(variable1, y), check_variables(variable2, y)))
            y = input('>>> ')
            y = error_find(y)

        # user input: multiplication
        elif y.count('*') == 1:
            print(multiplication(check_variables(variable1, y), check_variables(variable2, y)))
            y = input('>>> ')
            y = error_find(y)

        # user input: division
        elif y.count('/') == 1:

            # if division is supposed to be done, first check if the denominator is zero.
            while division(check_variables(variable1, y), check_variables(variable2, y), 0, y)\
                    is False and y.count('/') == 1 and y[0:4] == 'calc':
                y = input('>>> ')
                y = error_find(y)

                # check for faulty amount of operators
                while y.count('-') + y.count('+') + y.count('*') + y.count('/') > 1 or \
                        y.count('-') + y.count('+') + y.count('*') + y.count('/') == 0 \
                        and y[0:4] == 'calc' and y.count('/') == 1:
                    print('Error: invalid command')
                    y = input('>>> ')
                    y = error_find(y)
                if y[0:4] == 'calc' and y.count('/') == 1:
                    o = []
                    for i in y:
                        if i != ' ':
                            o.append(i)

                    # process of acquiring first operand
                    i = y[4:]
                    if i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) == 1:
                        variable1 = i[i.index(o[4]): i.index(o[o.index(a) - 1]) + 1]
                    elif i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) != 1:
                        p = 0
                        list4 = []
                        for v in i[i.index(o[4]):i.index(a)]:
                            if v == o[o.index(a) - 1]:
                                list4.append(p)
                            p = p + 1
                        variable1 = i[i.index(o[4]): max(list4) + 1]
                    c = y[y.index(a) + 1:]

                    # process of acquiring second operand
                    if c.count(o[len(o) - 1]) == 1:
                        variable2 = c[c.index(o[o.index(a) + 1]): c.index(o[len(o) - 1]) + 1]
                    elif c.count(o[len(o) - 1]) != 1:
                        first = 0
                        list6 = []
                        for x in c:
                            if x == o[len(o) - 1]:
                                list6.append(first)
                            first = first + 1
                        variable2 = c[c.index(o[o.index(a) + 1]): max(list6) + 1]
            if y[0:4] == 'calc' and y.count('/') == 1:
                if y.count('-') == 1:
                    a = '-'
                elif y.count('+') == 1:
                    a = '+'
                elif y.count('*') == 1:
                    a = '*'
                elif y.count('/') == 1:
                    a = '/'
                o = []
                for i in y:
                    if i != ' ':
                        o.append(i)

                # process of acquiring first operand
                i = y[4:]
                if i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) == 1:
                    variable1 = i[i.index(o[4]): i.index(o[o.index(a) - 1]) + 1]
                elif i[i.index(o[4]):i.index(a)].count(o[o.index(a) - 1]) != 1:
                    p = 0
                    list4 = []
                    for v in i[i.index(o[4]):i.index(a)]:
                        if v == o[o.index(a) - 1]:
                            list4.append(p)
                        p = p + 1
                    variable1 = i[i.index(o[4]): max(list4) + 1]

                # process of acquiring second operand
                c = y[y.index(a) + 1:]
                if c.count(o[len(o) - 1]) == 1:
                    variable2 = c[c.index(o[o.index(a) + 1]): c.index(o[len(o) - 1]) + 1]
                elif c.count(o[len(o) - 1]) != 1:
                    first = 0
                    list6 = []
                    for x in c:
                        if x == o[len(o) - 1]:
                            list6.append(first)
                        first = first + 1
                    variable2 = c[c.index(o[o.index(a) + 1]): max(list6) + 1]
                while check_variables(variable1, y) is True or check_variables(variable2, y) is True:
                    y = input('>>> ')
                    y = error_find(y)

                # if there are no problem, print out the output of the calculation
                division(check_variables(variable1, y), check_variables(variable2, y), 1, y)

                y = input('>>> ')
                y = error_find(y)
