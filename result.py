import math

# (! **) (* / % //) (+ -)
list_oper_1 = ['**']
list_oper_2 = ['*', '/', '%', '//']
list_oper_3 = ['+', '-']


def result(l: str):
    #print(l)
    while '(' in l:
        tag = 0
        start = [0, False]
        ending = 0
        for i in range(len(l)):
            if l[i] == '(':
                tag += 1
                if start[1] == False:
                    start[0] = i
                    start[1] = True
            elif l[i] == ')':
                tag -= 1
            if tag == 0 and start[1] == True:
                ending = i
                break
        l1 = list(l)

        l1[start[0]:(ending + 1)] = result(''.join(l1[start[0] + 1:(ending)]))
        l = ''.join(l1)

    return result_without(l)


def result_without(l: str):
    M = []
    tmp_str = ""
    mode = 'int'
    for i in range(len(l)):
        if (l[i] == '*') or (l[i] == '/') or (l[i] == '%') or (l[i] == '+') or (l[i] == '-'):
            if mode == 'int':
                M.append(tmp_str)
                mode = 'comma'
                tmp_str = l[i]
            else:
                tmp_str += l[i]
        else:
            if mode == 'int':
                tmp_str += l[i]
            else:
                M.append(tmp_str)
                mode = 'int'
                tmp_str = l[i]
    M.append(tmp_str)
    for i in range(len(M)):
        if M[i][-1] == '!':
            M[i] = str(math.factorial(int(M[i][:-1])))
    try:
        for i in range(len(M)):
            if M[i] in list_oper_1:
                tmp_res = float(M[i - 1]) ** float(M[i + 1])
                M[i] = str(tmp_res)
                del M[i - 1]
                del M[i]
            elif M[i] in list_oper_2:
                if M[i] == '*':
                    tmp_res = float(M[i - 1]) * float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
                if M[i] == '/':
                    tmp_res = float(M[i - 1]) / float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
                if M[i] == '%':
                    tmp_res = float(M[i - 1]) % float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
                if M[i] == '//':
                    tmp_res = float(M[i - 1]) // float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
            elif M[i] in list_oper_3:
                if M[i] == '+':
                    tmp_res = float(M[i - 1]) + float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
                if M[i] == '-':
                    tmp_res = float(M[i - 1]) - float(M[i + 1])
                    M[i] = str(tmp_res)
                    del M[i - 1]
                    del M[i]
    except IndexError:
        pass
    if len(M) == 1:
        return M[0]
    else:
        s = ''
        for i in M:
            s += i
        return result_without(s)



#print(result("(12!+48*(1+1))+1"))
# if (l[i] != '!') and (l[i] != '*') and (l[i] != '/') and (l[i] != '%') and (l[i] != '+') and (l[i] != '-'):
