#concate
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
tuple3=tuple1+tuple2
print(tuple3)

list=['shravan']
list.append("hegde")
print(list)
 

str="shravan hegde hosalli"
print(str)
print(str.split())   #spliting the string into list

print(str[4:10])  #slicing from 4th to 9th index


print(str[-1])   #last character of the string ,-2 last but one character

print(str[1:-1]) 

print(str.upper()[0:3])
print(str.upper()[:3],str.lower()[3:])

string="shravan hegde hosalli"
words=string.split()
words[0]=words[0].upper()
result=" ".join(words)
print(result)


#reverse string
string="shravan"
res=''.join(reversed(string))
print(res)

#reverse string
string="shravan"
res=string[::-1]
print(res)

#vowels in string
vowels=['a','e','i','o','u','A','E','I','O','U']
string="shravwhgvaqkxueyXEBan"
res=string.split()
for i in string:
    if i in vowels:
        print(i)



#even numbers in list
list=[4,2,6,3,5,2,8,9]
for i in list:
    if i%2==0:
        print(i)
        
    
         