# Solution 1

def myfunc():
    print('Hello World')


# Solution 2

def myfunc(name):
    #return 'Hello {}'.format(name)
    print('Hello {}'.format(name))


# Solution 3

def myfunc(x):
    if x == True:
        # print('Hello')
        return 'Hello'
    elif x == False:
        # print('Goodbye')
        return 'Goodbye'


# Solution 4

def myfunc(x,y,z):
    if z:
        # print(x)
        return x
    else:
        # print(y)
        return y


# Solution 5

def myfunc(a,b):
    print(a+b)
    # return a+b


# Solution 6

def is_even(n):
    if n%2 == 0:
        return True
        # print(True)  **tested to make sure it DOESN'T work
    else:
        return False


# Solution 7

def is_greater(x,y):
    return x>y


# Solution 8

def myfunc(*args):
    return sum(args)


# Solution 9

def myfunc(*args):
    out = []
    for num in args:
        if num%2==0:
            out.append(num)
    return out


#Solution 10

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

