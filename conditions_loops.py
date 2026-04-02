#largest of three numbers
#a=14
#b=4
#c=45
a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))

if  a>b & a>c:
    print("a is greater")
elif b>a & b>c:
    print("b is greater")
else:
    print("c is greater")
    

#multipliation table
print("enter number")
n=int(input())
i=1
while i<=10:
    print(str(n)+"*"+str(i)+"="+str(n*i))
    i+=1

s=input("enter string\n")
#s1=s.split()   #to check number of words in  string
print(len(s))
    

p=(input("enter numbers\n"))
print(max(p))

#prime number
i=28
while i<=50:
    is_prime=True
    for j in range(100):
        if i%j==0:
            is_prime=False
    if is_prime:
        print(i)
    i+=1
        
    

