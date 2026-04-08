#Error Handling

try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print('result is=',a/b)

except ZeroDivisionError as zr:
     print('cant devide by zaro::',zr)   
except ValueError as vr:
     print('numeric values only',vr)  
except Exception as e:
    print("error occuring::",e)

finally:
    print("this is fixed even cod erun or not itll print")

print("practise")

#file open
try:
    s=open("file_handlig.txt",'r')
    print(s.read())
except Exception as e:
    print('file not found please check::',e)

finally:
    print('file check successfully')



#for list checking    
try:
    a=int(input('enter input size of list'))
    if a>5:
        raise Exception('you cant print more than 5')
    print('given elements are:')
    for i in range(a):
        print(input())

except Exception as e:
    print('you cant:',e)
finally:
    print('successfully checked list')


