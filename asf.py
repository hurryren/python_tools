input = ["MYARTLOLLIPOPS MYLARBALLOONS",
"MASSACHUSETTSBAYCOLONY MINUTEMANNATIONALHISTORICALPARK",
"LOWERMACTOWNSHIPPA CRANBERRYTOWNSHIPPA",
"AMERICANCOMPUTERSCIENCELEAGUE NATIONALACADEMICGAMESLEAGUE",
"ABCDEFGHIJK ABDCEFGKILKJMN"]


test0 = "abcdeft abxcgbtzfp"
test1 = "blameablenesses blamelessnesses"
test2 = "mezzamines razzmatazz"

def get_list(input):
    a, b = input.split(" ")
    a_list = []
    b_list = []
    for item in a:
        a_list.append(item)
    for item in b:
        b_list.append(item)
    return a_list,b_list

def del_same(a:list,b:list):
    temp_a = []
    temp_b = []
    length = len(a) if len(b) > len(a) else len(b)
    for i in range(length):
        if(a[i] != b[i]):
            temp_a.append(a[i])
            temp_b.append(b[i])



    if len(a) > len(b):
        temp_a += a[len(b)::]
    if len(b) > len(a):
        temp_b += b[len(a)::]

    return temp_a,temp_b

def align(a:list,b:list):
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



def cal_asf(a:list,b:list):
    result = abs(len(a) - len(b))
    length = len(a) if len(b) > len(a) else len(b)
    for i in range(length):
        temp = ord(a[i]) - ord(b[i])
        result += temp
    print("asf value is: {}".format(result))



def cal_result(a,b):
    c = True
    while (c):
        a,b = del_same(a,b)
        print("a: ", a)
        print("b: ", b)
        print("***********************")

        a,b,c = align(a,b)
        if c:
            print("a: ", a)
            print("b: ", b)
            print("***********************")

        else:
            print("result")
            print("a: ", a)
            print("b: ", b)
            print("***********************")
            break

    cal_asf(a,b)

if __name__ == "__main__":
    a,b = get_list(input[0])
    print("test 0")
    a,b = get_list(test0)
    cal_result(a, b)
    print()


    print("test 1")
    a, b = get_list(test1)
    cal_result(a, b)
    print()

    print("test 2")
    a, b = get_list(test2)
    cal_result(a, b)
    print()

    print("start calculate!!!")
    for i in range(5):
        print("case: {}".format(i))
        a, b = get_list(input[i])
        print("input a: ", a)
        print("input b: ", b)
        cal_result(a, b)
        print()


