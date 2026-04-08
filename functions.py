def add(x,y):
    
    return x+y,x-y
    

print(add(2,3))
print("addition : ",add(4,3))


def sub(x,y):
    return x-y

print(sub(3,5))


#multiplication table using functions
def mul(x,y):
    return x*y
for x in range(1,11):
    print(mul(x,2))


#palindrome or not using function
def palindrome(s):
    s=s.replace(" ","")
    r=s[::-1]
    if s==r:
        print('given string is palindrome')
    else:
        print('not a palindrome')

palindrome('12321')

#factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))

#using loop
def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
        return res
print(fact(4))


#sort list of dictionaries by score using simple function
dicts = {"name":'shravan',"score":100},{'name':'abhi',"score":80},{'name':'boss',"score":90}

def std(dict):
    return dict['score']
sorted_dict=sorted(dicts,key=std,reverse=True)
print(sorted_dict)

# Sort list of dictionaries by 'score' in descending order
#sorted_students = sorted(dict, key=lambda x: x['score'], reverse=True)
#print(sorted_students)
