import os

class fileinfo:
    def __init__(self):
        self.dir_name = ""
        self.file_name = ""
        self.full_path = ""
        self.is_fail = 0
        self.fail_lines = []


dir_list = []
all_file_full_path = []
fileinfo_list = []

root_path = "D:/git_orange/python_tools/log/"
result_path = "D:/git_orange/python_tools/result.txt"
dir_list_t = os.walk(root_path)

for root,dirs,file in dir_list_t:
    for dir in dirs:
        # print(dir)
        dir_full_path = os.path.join(root,dir)
        # print(dir_full_path)
        dir_list.append(dir_full_path)
        # file_dir_list = os.walk(dir_full_path)
        # for root, dirs, files in file_dir_list:
        #     for file in files:
        #         filename = os.path.join(root,file)
        #         if os.path.exists(filename):
        #             all_file_full_path.append(filename)

# print(dir_list)
for item in dir_list:
    file_list = os.walk(item)
    for root,dirs,files in file_list:
        for file in files:
            filename = os.path.join(root,file)
            all_file_full_path.append(filename)
            # print(filename)
# print(all_file_full_path)



f_reault = open(result_path,mode='a',encoding="utf-8")

# test_file_path = "D:/git_orange/python_tools/log/21010032/21010032-1.txt"
test_file_path = "full pathD:/git_orange/python_tools/log/21010037\21010037-3-1.txt"
for file_path in all_file_full_path:
    error_list = []



    f_read = open(file_path,encoding="utf-8",errors="ignore")

    lines = f_read.readlines()
    for line in lines:
        item = line.split(" ")
        for i in item:
            if i == "失败" or i == "失败\n":
                error_list.append(line)
                # f_reault.write(line)

    f_read.close()
    if len(error_list) > 0:
        print(len(error_list))
        print(file_path)
        f_reault.write("\n\n\n************ 分割线 **********\n")
        f_reault.write(file_path)
        f_reault.write("\n")
        for error_item in error_list:
            f_reault.write(error_item)


test_file_path = "full pathD:/git_orange/python_tools/log/21010037/21010037-3-1.txt"

f_reault.close()

