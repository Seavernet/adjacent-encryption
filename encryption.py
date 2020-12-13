'''
* = odd
** = even
% = equal
'''


def encrypt(message):
    newmessageodd = list()
    newmessageeven = list()
    encryptedmessage = str()
    message = list(message)
    l = len(message)
    for i in range(l):
        if i % 2 == 0:
            newmessageeven.append(message[i])
        else: 
            newmessageodd.append(message[i])
    l1 = len(newmessageeven)
    l2 = len(newmessageodd)
    l3 = l1 + l2
    if l1 > l2:
        char = '**'
    elif l1 < l2:
        char = '*'
    elif l1 == l2:
        char= '%'
    for ele in newmessageeven:
        encryptedmessage += ele
    for elee in newmessageodd:
        encryptedmessage += elee
    encryptedmessage += str(l3)
    encryptedmessage += char
    return encryptedmessage

def calc(y):
    if y == 1:
        return 'odd'
    elif y == 2:
        return 'even'
    elif y == 3:
        return 'equal'
    else:
        raise(IndexError)

def decrypt(message):
    message = list(message)
    amount = list()
    even = list()
    count = int()
    neweven = list()
    newodd = list()
    odd = list()
    newmessage = list()
    a = str()
    l = len(message)
    for i in range(l):
        if message[i] == '*':
            count += 1
        elif message[i] == '%':
            count +=3
    for i in range(l):
        if message[i].isdigit() == True:
            amount.append(message[i])
        elif message[i] == '%' or message[i] == '*':
            pass
        else:
            newmessage.append(message[i])
    for ele in amount:
        a += ele
    a = int(a)
    risk = calc(count)
    le = len(newmessage) / 2
    le = int(le)
    if risk == 'equal':
        pass
    elif risk == 'odd':
        le = le - 1
    elif risk == 'even':
        le = le + 1
    for i in range(le):
        if i % 2 == 0:
            neweven.append(newmessage[i])
        elif i % 2 == 1:
            newodd.append(newmessage[i])
    first = list()
    
    if len(neweven) > len(newodd):
        l3 = len(neweven)
    else:
        l3 = len(newodd)
    for i in range(l3):
        try:
            first.append(neweven[i])
        except IndexError:
            pass
        try:
            first.append(newodd[i])
        except IndexError:
            pass
    newfirst = str()
    neweven2 = list()
    newodd2 = list()
    for w in first:
        newfirst += w
    print(newfirst)
    for i in range(le):
        if i % 2 == 0:
            neweven2.append(newmessage[i + le])
        elif i % 2 == 1:
                newodd2.append(newmessage[i + le])
            
    second = list()
    if len(neweven2) > len(newodd2):
        l3 = len(neweven2)
    else:
        l3 = len(newodd2)
    for i in range(l3):
        try:
            second.append(neweven2[i])
        except IndexError:
            pass
        try:
            second.append(newodd2[i])
        except IndexError:
            pass
    newsecond = str()
    for w2 in second:
        newsecond += w2
    print(newsecond)
    final = list()
    if len(newfirst) > len(newsecond):
        l4 = len(newfirst)
    else:
        l4 = len(newsecond)
    for i in range(l4):
        try:
            final.append(newfirst[i])
        except IndexError:
            pass
        try:
            final.append(newsecond[i])
        except IndexError:
            pass
    newfinal = str()
    for r in final:
        newfinal += r
    return newfinal


