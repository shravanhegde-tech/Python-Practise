age=10   #int
print(type(age))

age=(age)

age1=10.333   #float
print(type(age1))

age3=age+age1
print(type(age3),"=",age3)

age4=25    #condition if with boolean
if age4<24:
    print(bool(age4))
else:
    print(bool(False))


age5='10str'   #you can use doubke quote also for string
print(type(age5))



list=["4","shravan","5","23"]   #list 
print(type(list),list)



set={"shravan",234}    #set
print(type(set),set)

tuple=(4,2,"shravan","5",bool(0),bool(1))   #tuple
print(type(tuple))
print(tuple)

dict={"name":"shravan","name":"shravan2"}  #distionary1
print(type(dict),dict)


dict1={"name":"shr","age":24}  #distionary2   

#here if i use "24" itll store as string but we cant calculate it
print(dict1)

print(dict1["age"]+23)


for i in dict1:
    print(i,':-',dict1[i],)   #i=key and dict1[i]=value given
    #print(i)