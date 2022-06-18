text='five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
spis=[]
list=text.split() 
d={'one':1,'two':2,'tree':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11, 'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
for i in range(len(list)): 
    print(d[list[i]],end=' ') 
    spis.append(d[list[i]]) 
print()
#преобразовал в числа

spis.sort() 
print(spis)
#отсортировал по возрастанию

b=len(spis)-2
for j in range(b-1):
    if len(spis)-1==j:
        break
    elif spis[j]==spis[j+1]:
        del spis[j] 
        b-=1
        j-=1
print(spis) 
#исключил дубликаты 

spis2=[]
for i in range(len(spis)-1):
    if i%2==0:
        spis2.append(str(spis[i]*spis[i+1]))
    else:
        spis2.append(str(spis[i]+spis[i+1]))
print(spis2)
# вывел произвеление первого и второго числа, сумму второго и третьего и т.д.....

sum1=0
for i in range(len(spis2)):
    if (int(spis2[i])%10)%2!=0: 
        sum1+=int(spis2[i])
print(sum1)
# вывел полную сумму всех нечётных чисел
