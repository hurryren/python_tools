

input = ["RUNNERISFOLKERANDTHREAD 2",
"BITCOINISNOTMONNEYITISMOOONEY 3",
"YOUSAYITTISMMYYYOUUUUNESTBROTHER 3",
"WEWILLSAYITISRIGHTORNOT 3",
"VOLUNTEERVOLUNTEER 2",]


test0 = "MBAMMDXXMMMGGMMZ 3"
test1 = "MHHHHJLDDHHDDD 3"


def get_list(input_str):
    a, b = input_str.split(" ")
    a_list = []
    length = int(b)
    for item in a:
        a_list.append(item)
    return a_list,length

def split_string(a:list):
    result = []
    pre = a[0]
    now = ''
    temp = a[0]
    for i in range(1,len(a)):

        if a[i] == pre:
            if i == len(a) -1:
                temp += a[i]
                result.append(temp)

            temp += a[i]
        else:
            if i == len(a) -1:

                result.append(a[i])
            else:
                result.append(temp)
                pre = a[i]
                temp = a[i]

    print(result)
    return result


def cal(in_str):
    result = []
    in_str, length = get_list(in_str)
    print("a: ", in_str)
    print("b: ", length)
    split_result = split_string(in_str)
    split_result.sort()

    sorted_list = []
    for i in range(len(in_str), 0, -1):
        for item in split_result:
            if len(item) == i:
                sorted_list.append(item)
    print(sorted_list)

    a = ''
    for item in sorted_list:
        if len(item) > length:
            item = item[0:length]
            a += item
            print(item,end="")
        else:
            a += item
            print(item,end="")

    print()
    dec_repeat(a,length)


def dec_repeat(in_str,length):
    split_result = split_string(in_str)
    print("结果是  :")
    for item in split_result:
        if len(item) > length:
            item = item[0:length]
            print(item, end="")
        else:
            print(item, end="")
    print()
    print()
    print()






if __name__ == "__main__":
    cal(test0)
    cal(test1)
    for i in range(5):

        cal(input[i])







"""
NNADDEEFHIKLNORRSU
OOONNBCEIIIMMNNNOOOSSTTTYY
UUUYYYMMTTABEHIINOOORRSSSTTUYY
LLAEGHIIINORRSSTTTY
EELLNNOORRTTUUVV
"""





    # print("start calculate!!!")
    # for i in range(5):
    #     print("case: {}".format(i))
    #     a, b = get_list(input[i])
    #     print("a: ", a)
    #     print("b: ", b)
    #     cal_result(a, b)
    #     print()

