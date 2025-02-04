f=open('111.txt','r')
data8=[]
data9=[]
data10=[]
data11=[]
for i in f:
    L=i.split()
    if int(L[2]) == 8:
        data8.append(L)
    elif int(L[2]) == 9:
        data9.append(L)
    elif int(L[2]) == 10:
        data10.append(L)
    elif int(L[2]) == 11:
        data11.append(L)

data_o=[data8,data9,data10,data11]

k=7
for data in data_o:
    k+=1
    print('Победитель среди ',k,' классов:')
    maxim=max(data, key=lambda x: x[3]+x[4])
    win = [x for x in data if x[3]+x[4]==maxim[3]+maxim[4]]
    for i in win:
        print(i[0], i[1], int(i[3])+int(i[4]))
    print()


data_o=data8+data9+data10+data11

max_alg=max(data_o, key=lambda x: x[3])
win_alg = [x for x in data_o if x[3]==max_alg[3]]


max_geom=max(data_o, key=lambda x: x[4])
win_geom = [x for x in data_o if x[4]==max_geom[4]]

print()
print('Самый высокий балл по алгебре')
for i in win_alg:
    print(i[0], i[1], i[2],'класс.', i[3])

print()
print('Самый высокий балл по геометрии')
for i in win_geom:
    print(i[0], i[1], i[2],'класс.', i[4])



