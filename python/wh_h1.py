#import os
#def clear():
#    os.system('cls')
print("使用本程序之前请输入姓名以获得使用许可")
name = input()
while True:
    print(name,"""欢迎使用简陋的木叶村活动室预约程序。注意每一选项必须按0返回后才可关闭程序，否则操作无效\n\n
          1:预约活动室     2：取消活动室预约   3：查询 （管理员权限）  4：退出程序""")
    #创建
    roomfile = open(r'D:\roomdata.txt','a+')
    roomfile.seek(0)
    roomlist = []
    for x in roomfile:
        roomlist.append(x.strip())
    if roomlist == []:
        roomlist = [0,0,0,0,0]
    else:
        roomlist = [int(k) for k in roomlist]
    namesfile = open(r'D:\namesdata.txt','a+')
    namesfile.seek(0)
    nameslist = []
    for y in namesfile:
        nameslist.append(y.strip())
    if nameslist == []:
        nameslist = [0,0,0,0,0]
    else:
        q=1
    number = int(input("请输入"))
    if number == 1:
        while True:
            print("输入0返回上一界面")
            count = 0
            list1 = []
            for x in roomlist:
                count += 1
                if x == 0:
                    list1.append(count)
                else:q=1
            print(list1,"活动室还可以预约     ",end="")
            n = int(input("请输入预约活动室序号（1——5）"))
            if n in list(range(1,6)):
                if roomlist[n-1] != 1:
                    roomlist[n-1] = 1
                    print("已经成功预约活动室",n,)
                    nameslist[n-1] = name#出现在开始时
                else:
                    print("此活动室已经被",nameslist[n-1],"预约了")
            if n == 0:
                nameslist = [str(x)+'\n' for x in nameslist]
                namesfile = open(r'D:\namesdata.txt','w')
                namesfile.writelines(nameslist)
                namesfile.close()
                
                roomlist = [str(z)+'\n' for z in roomlist]
                roomfile = open(r'D:\roomdata.txt','w')
                roomfile.writelines(roomlist)
                roomfile.close()
                break

    if number == 2:
        while True:
            print("输入0返回上一界面")
            print("请输入你要取消预约的活动室序号")
            n = int(input())
            if roomlist[n-1] == 1:
                if  nameslist[n-1] == name:
                    nameslist[n-1] = 0
                    roomlist[n-1] = 0
                    print(name,"你预约的活动室",n,"已经被成功取消")
                else:
                    print("卧槽，不允许修改他人预约")
            elif n == 0:
                nameslist = [str(x)+'\n' for x in nameslist]
                namesfile = open(r'D:\namesdata.txt','w')
                namesfile.writelines(nameslist)
                namesfile.close()
                    
                roomlist = [str(z)+'\n' for z in roomlist]
                roomfile = open(r'D:\roomdata.txt','w')
                roomfile.writelines(roomlist)
                roomfile.close()
                break
            else:
                print("干嘛，这个活动室没被预约啊")
    if number == 3:
        print('请输入管理员密码（111）')
        print("输入0返回上一界面")
        key = int(input())
        if key == 111:
            print("请输入查询活动室序号")
            n = int(input())
            if roomlist[n-1] == 1:
                namex = str(nameslist[n-1])
                print(namex,"预约了此活动室")
            else:
                print("此活动室未被预约")
        else:
            if key == 0:
                break
            else:
                print("密码错了，前面都说了是111，卧槽")
        
    if number == 4:
        print("自己叉掉不行啊")
        #os._exit()

                
