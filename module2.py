start=int(input())
stop=int(input())
k=0
file=open('perepis.txt','r')
for i in file:
    god=int(str(i.split('  ')[3:4])[8:12])
    if start<god<stop:
        print(i)
        k+=1
print('Всего ',k)
file.close()