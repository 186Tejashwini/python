'''dict={x:x**2 for x in range(1,6)}
print(dict)'''
'''dict={x:"even" if x%2==0 else "odd" for x in range(1,11)   }
print(dict)'''

'''words=["banana","Apple","Orange","Mango"]
dict={words:len(words) for words in words}
print(dict)'''

#keys are numbers from 1 to 5 and values are factorials of those number
f_dict={}

for num in range(1,6):
    fact=1
    for i in range(1,num+1):
        fact*=i
    f_dict[num]=fact
print(f_dict)



