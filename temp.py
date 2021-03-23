test_file_path = "D:/git_orange/python_tools/log/21010037/21010037-3-1.txt"

f_read = open(test_file_path,encoding="utf-8",errors="ignore")

lines = f_read.readlines()
for line in lines:
    item = line.split(" ")
    for i in item:
        if i == "失败" or i == "失败\n":
            print(line)