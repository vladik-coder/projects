from method import *

def parenthesis(line):
    while True:
        i = end = line.find(')')
        if i == -1:
            break
        while line[i] != '(':
            i -= 1
        expression = line[i + 1:end]
        method = find_method(expression)
        if expression.find(method) == 0 and find_method(expression[1:]) == None:
            res = expression
        else:
            elements = expression.split(method, 1)
            if find_method(elements[0]) or find_method(elements[1]):
                res = without_parenthesis(expression)
            else:
                res = do_method(method, elements)
        line = line.replace(line[i:end + 1], res)
    return without_parenthesis(line)


def find_method(expression):
    methods1 = ['*', '/']
    methods2 = ['+','-']
    for i in expression:
        if i in methods1:
            return i
    for i in expression:
        if i in methods2:
            return i


def without_parenthesis(line):
    method = find_method(line)
    while method:
        i = start = line.find(method)
        if i == 0 and find_method(line[1:]) == None:
            break
        elif i == 0:
            method = find_method(line[1:])
            i = line[1:].find(method) + 2
            if line[i] == '-':
                i += 1
            while i < len(line) and line[i] not in ['*', '/', '+', '-']:
                i += 1
            expression = line[1:i]
            elements = expression.split(method, 1)
            elements[0] = '-' + elements[0]
            res = do_method(method, elements)
            line = line.replace(line[:i], res,1)
        else:
            i += 1
            start -= 1
            if line[i] == '-':
                i += 1
            while i < len(line) and line[i] not in ['*', '/', '+', '-']:
                i += 1
            while start >= 0 and line[start] not in ['*', '/', '+', '-']:
                start -= 1
            if start == 0 and line[0] == '-':
                start -= 1
            expression = line[start + 1:i]
            elements = expression.split(method, 1)
            res = do_method(method, elements)
            line = line.replace(line[start + 1:i], res,1)
        method = find_method(line)
    return line


def do_method(method, elements):
    if method == '+':
        res = add(elements[0], elements[1])
    elif method == '-':
        res = minus(elements[0], elements[1])
    elif method == '*':
        res = mult(elements[0], elements[1])
    elif method == '/':
        res = div(elements[0], elements[1])
    return res


while True:
    line = input('Please enter your expression:\n')
    print(parenthesis(line))
