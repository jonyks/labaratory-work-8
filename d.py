try:     #Для проверки числовго ввода
    a=int(input('Введите количество сотрудников '))
except:
    print('Неправильный ввод данных')
    quit()
c=dict()
sum=0
b=input('Введите количество километров для каждого сотрудника ').split()
if a==len(b):     #Для проверки количества пассажиров
    for i in range(a):
        c[i+1]=float(b[i])
else:
    print('Неправильный ввод данных')
    quit()
c = sorted(c.items(), key=lambda x: x[1])
d=dict()
e=input('Введите стоимость 1 километра для каждого такси ').split()
if a==len(e):     #Для проверки количества такси
    for i in range(a):
        d[i+1]=float(e[i])
else:
    print('Неправильный ввод данных')
    quit()
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
l=[]
for i in range(a):
    l.append(d[i][0])
print('Порядок:',end='')
print(*l,sep=', ')
for i in range(a):
    sum+=int(d[i][1]*c[i][1])
print(f'Итого: {sum}')
#Программа из 4-ого домашнего задания(ограничен до 100000)
des=['','десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
sot=['','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']
edin=['','одна','две','три','четыре','пять','шесть','семь','восемь','девять']
edins=['','один рубль','два рубля','три рубля','четыре рубля','пять рублей','шесть рублей','семь рублей','восемь рублей','девять рублей']
tis=['','тысяча','тысячи','тысячи','тысяч','тысяч','тысяч','тысяч','тысяч','тысяч']
nadc=['десять','одиннадцать','двенадцать','тринацать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
answer=[]  
if sum==100000:print('Сто тысяч рублей')
elif not(sum>100000 or sum<1):
    while True:
        if sum//10000>=1:
            b=sum//10000
            answer.append(des[b])
            sum=sum%10000
            if not sum//1000>=1:
                answer.append('тысяч')
            continue
        if sum//1000>=1:
            b=sum//1000
            answer.append(edin[b]+' '+tis[b])
            sum=sum%1000
            continue
        if sum//100>=1:
            b=sum//100
            answer.append(sot[b])
            sum=sum%100
            continue
        if sum//10>=1:
            b=sum//10
            if b==1:
                c=sum%10
                answer.append(nadc[c]+' рублей')
                break
            answer.append(des[b])
            sum=sum%10
            continue
        if sum%10>=1:
            b=sum%10
            answer.append(edins[b])
            break
        else :
            answer.append('рублей')
            break
    answer[0]=answer[0].capitalize()
    print(*[item for item in answer])