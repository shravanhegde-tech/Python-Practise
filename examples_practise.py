#Student Grade Analyzer — dict of students, function filters passed ones, handles string grades
dicts=[{'name':'shravan','score':99},{'name':'boss','score':90},{'name':'koustub','score':100},{'name':'abhi','score':76},{'name':'raj','score':60},{'name':'unknown','score':5}]
def sol(dict):
    return dict['score']
sorted_d=sorted(dicts,key=sol,reverse=True)
print(sorted_d)
for i in sorted_d:
    if i['score']>90:
        print('A+ grade students are\n',i['name'])
    elif i['score']>75:
        print('b+ grade students are\n',i['name'])
    elif i['score']>35:
        print('c+ grade students are\n',i['name'])
    else:
        print('failed students are\n',i['name'])


#vowels in string and writing into file
list=['a','e','i','o','u','A','E','I','O','U']
def vowels(str):
    found=[]
    for i in str:
        if i in list:
            found.append(i)
    return found
        
str=input('string is\n')
res=vowels(str)
print('vowels in given string\n',res)

f=open('vowels.txt','w')
for i in str:
    f.write(i)
for i in res:
    f.write(i)

#basic calsi
x=input('enter operator\n')
def calsi(a,b):
    try:
        if x=='+':
            return ('addition of a and b :',(a+b))
        elif x=='-':
            return('subtraction of a and b :',(a-b))
        elif x=='*':
            return('multiplication of a and b :',(a*b))
        elif x=='/':
            return('division of a and b :',(a/b))
        elif x=='%':
            return('module of a and b :',(a%b))
        else:
            return('invalid choice\n')
    except Exception as e:
        print('error found::',e)
    finally:
        print('calsi executed')
print(calsi(24,0))

#word frequency
x=(input('enter sentence\n'))
spl=x.split()
count={}
for i in spl:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
          
#log file
from datetime import datetime
with open('logfile.txt','a') as file:
    file.write(f'{datetime.now()}:program started\n')
    file.write('program typing',datetime.now())
    file.write(f'{datetime.now()}:program ended\n')

print('successfully uploaded',datetime.now())
    

#multiplication table in file
"""y=open('multiplication.txt','w')
for i in range(1,6):
    for n in range(1,11):
        x=f'{i}*{n}={i*n}\n'
        y.write(x)"""
        

with open('multiplication.txt','a') as y:
    for i in range(1,6):
        for n in range(1,11):
            if i*n>20:
                x=f'{i}*{n}={i*n}\n'
                print(x.strip())
                y.write(x)

#even or odd and sum in file
y=open('even.txt','w+')
z=open('odd.txt','w+')
even=[]
odd=[]
for i in range(1,21):
    if i%2==0:
        y.write(f'{i}\n')
        even.append(i)
    else:
        z.write(f'{i}\n')
        odd.append(i)

print('sum of even num',sum(even))
print('sum of odd num',sum(odd))



#to-do list 
tasks=[{'task':'god','status':'pending'},
       {'task':'python','status':'pending'},
       {'task':'exercise','status':'pending'}]

tasks[0]['status']="completed"
tasks[2]['status']='completed'
z=open('todo.txt','w')
for t in tasks:
    x=f'{t["task"]}-{t["status"]}\n'
    print(x.strip())
    z.write(x)

    