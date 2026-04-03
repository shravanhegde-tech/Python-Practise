#DECLAIMER::MANY TIMES I USE '#' BECAUSE SOME CODES CAN CHANGE THE ORIGINAL FILE LIKE OVERWRITE ,COPYING DATA


r=open('file_handling.txt','r')
print(r.read()) #print all text in file

print(r.readline(),end="#")  #itll read only first line      #end="#" means if you want to print next line  after first is completed to know eher it ends this will help you
print(r.readline())  #itll read only second line

w=open('file_handling.txt','w')
#print(w.write('God is Great'))  #itll overwrite  means delte old text and write god is great


#if there is no file by using w function itll  create new file and write text inside it
f=open('shravan.txt','w')
f.write('im shravan\n')

#for append
f1=open('shravan.txt','a')
f1.write('helo bruhh')

#to copy data from one file to another
#r=open('file_handling.txt','r')
#f=open('shravan.txt','w')
#for data in r:
    #f.write(data)


#count lines in file 
count=0
r=open('file_handling.txt','r')
for line in r:
    count+=1
print("lines in file:",count)


#to print photo     #here photo.jpg we need to save some photos
p=open('photo.jpg','rb')  #rb means read binary cause we need to decode it
p1=open('photo_copy.jpg','wb')  #wb means write binary
for i in p:
    p1.write(i)
