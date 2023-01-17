import os
import re

# 读取文件，默认以文本读取，编码类型为utf-8
def readFromFile(file, mode="r", encoding='utf-8'):
    with open(file, mode, encoding=encoding) as f:
        text = f.read()
    return text

# 将数据data，写入文件file，默认模式是w
def writeToFile(file, data, mode="w", encoding='utf-8'):
    with open(file, mode, encoding=encoding) as f:
        f.write(data)

def generateCodeFromFile(file, data, mode="w"):
    code = readFromFile(file)
    # 使用正则匹配
    pattern = re.compile(r"\{\{\$[0-9]+\}\}")
    # 将匹配的结果使用set去重
    result = set(pattern.findall(code))

    # 分割文件的名字和后缀
    tmp = os.path.splitext(file)

    # 生成len(data[0])个文件或在同一个文件内追加len(data[0])条数据
    for i in range(len(data[0])):
        file_data = code
        # 将所有占位符替换成有效数据
        for res in result:
            file_data = file_data.replace(res, data[int(res[3:-2])][i])
        
        if mode == "w":
            writeToFile(tmp[0] + "_" + str(i+1) + tmp[1], file_data + "\n", mode)
        elif mode == "a+":
            writeToFile(tmp[0] + "_" + "1"+ tmp[1], file_data + "\n", mode)
        else:
            print("This feature is not currently supported\n")

def clear(files):
    for file in files:
        os.remove(file)

if __name__ == '__main__':
    # print("设置当前工作目录")
    # os.chdir("../docs")
    data = [[], []]
    # {{$0}}对应的数据
    data[0] = [str(i + 1) for i in range(256)]
    # {{$1}}对应的数据
    data[1] = [str(i + 30001) for i in range(256)]
    
    
    clear(["codeTemplate_1.txt"])
    generateCodeFromFile("codeTemplate.txt", data, "a+")

    # files = ["system_" + str(i+1) + ".xml" for i in range(256)]
    # clear(files)
    # generateCodeFromFile("system.xml", data, "w")


