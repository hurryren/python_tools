

def cal(a:list,b:list):
    result_a = []
    result_b = []
    if len(a) >= len(b):
        for i in range(len(b)):
            if (a[i] != b[i]):
                result_a.append(a[i])
                result_b.append(b[i])
        result_a += a[len(b)::]

    if len(b) > len(a):
        for i in range(len(a)):
            if (a[i] != b[i]):
                result_a.append(a[i])
                result_b.append(b[i])
        result_b += b[len(a)::]

    a,b = result_a,result_b
    if len(b) > len(a):
        for i in range(len(a)):
            if (a[i] == b[i + 1]):
                del b[i]
                return a, b, True
            if i < len(a) -1:
                if (b[i] == a[i + 1]):
                    del a[i]
                    return a, b, True
    elif len(b) < len(a):
        for i in range(len(b)):
            if i < len(b) - 1:
                if (a[i] == b[i + 1]):
                    del b[i]
                    return a, b, True

            if (b[i] == a[i + 1]):
                del a[i]
                return a, b, True
    else:
        for i in range(len(a)-1):
            if (a[i] == b[i+1]):
                del b[i]
                return a,b,True

            if (b[i] == a[i+1]):
                del a[i]
                return a,b,True
    return a,b,False





def main(list_a,list_b):
    flag = True
    while (flag):
        list_a,list_b,c = cal(list_a,list_b)
        if c:
            continue
        else:
            break

    result = abs(len(list_a) - len(list_b))
    length = len(list_a) if len(list_b) > len(list_a) else len(list_b)
    for i in range(length):
        temp = ord(list_a[i]) - ord(list_b[i])
        result += temp

    print("result is: ",result)


input_str = ["MYARTLOLLIPOPS MYLARBALLOONS", "MASSACHUSETTSBAYCOLONY MINUTEMANNATIONALHISTORICALPARK","LOWERMACTOWNSHIPPA CRANBERRYTOWNSHIPPA", "AMERICANCOMPUTERSCIENCELEAGUE NATIONALACADEMICGAMESLEAGUE", "ABCDEFGHIJK ABDCEFGKILKJMN"]



for i in range(5):
    print("第 {} 题 ".format(i))
    a, b = input_str[i].split(" ")
    list_a = []
    list_b = []
    for cha in a:
        list_a.append(cha)
    for cha in b:
        list_b.append(cha)

    main(list_a, list_b)
    print("------------ 分割线 ——-——————")


