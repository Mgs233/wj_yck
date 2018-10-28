roomsfile = open(r'D:\roomsfile.txt','a+')
roomsfile.seek(0)
rooms = []
for x in roomsfile:
    rooms.append(x.strip())
if rooms == []:
    rooms = [1,2,3,4,5]
else:
    rooms = [int(k) for k in rooms]
namesfile = open(r'D:\namesfile.txt','a+')
namesfile.seek(0)
names = []
for y in namesfile:
    names.append(y.strip())
if names == []:
    names = [0,0,0,0,0]
else:
    mgs = 0
print('欢迎使用活动室预约系统')
user_name = input('请输入你的用户名：')
while True:
    print('\n',user_name,'，请选择你要进行的操作\n')
    print('1：预约活动室','2：取消预约','3：查询预约情况')
    cz = input('请输入相应数字：')
    if cz == '1':
        while True:
            print('\n',rooms,'号活动室可预约')
            n = int(input('请输入相应序号：'))
            if n in rooms:
                rooms.remove(n)
                roomslist = [str(x)+'\n' for x in rooms]
                roomsfile = open(r'D:\roomsfile.txt','w')
                roomsfile.writelines(roomslist)
                roomsfile.close()
                names[n-1] = user_name
                nameslist = [str(y)+'\n' for y in names]
                namesfile = open(r'D:\namesfile.txt','w')
                namesfile.writelines(nameslist)
                namesfile.close()
                print('\n你成功预约了',n,'号活动室\n')
            else:
                if 0<=n<=5:
                    print('\n',n,'号活动室已被',names[n-1],'预约\n')
                else:
                    print('\n没有该活动室\n')
            gb = input('输入go继续预约，输入其他任意值返回上层：',)
            if gb == 'go':
                continue
            else:
                break
    elif cz == '2':
        while True:
            n=int(input('\n请选择要取消的活动室的序号：'))
            if 0<=n<=5:
                if names[n-1] == user_name:
                    rooms.insert(n-1,n)
                    roomslist = [str(x)+'\n' for x in rooms]
                    roomsfile = open(r'D:\roomsfile.txt','w')
                    roomsfile.writelines(roomslist)
                    roomsfile.close()
                    names[n-1] = 0
                    nameslist = [str(y)+'\n' for y in names]
                    namesfile = open(r'D:\namesfile.txt','w')
                    namesfile.writelines(nameslist)
                    namesfile.close()
                    print('\n取消成功')
                else:
                    print('\n你没有预约该活动室')
            else:
                print('\n没有该活动室')
            gb = input('\n输入go继续取消预约，输入其他任意值返回上层：')
            if gb == 'go':
                continue
            else:
                break
    elif cz == '3':
        i=0
        print('')
        for na in names:
            i+=1
            if int(na) == 0:
                print('还没人预约',i,'号活动室')
            else:
                print(na,'预约了',i,'号活动室')