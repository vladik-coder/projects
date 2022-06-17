sum=int(input('Введите начальную сумму депозита ')) 
time=int(input('Введите cрок на который открывается депозит год/лет ')) 
perc=int(input('Введите cтавку в %/год ')) 
month=time*12
a=1
while a<=month:
    sum2=sum+(sum/100)*(perc/12)
    sum=sum2
    a+=1
print('Cумма на счету в конце указанного срока составит:',sum)