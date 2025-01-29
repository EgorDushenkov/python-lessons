file=open('perepis.txt','r')
k=0
for i in file:
    god=int(str(i.split('  ')[3:4])[8:12])
    if god<1978:
        print(i.split('  ')[0:1])
        k+=1
print('Всего ',k)
file.close()

