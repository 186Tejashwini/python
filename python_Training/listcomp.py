'''num=[x for x in range(0,5)]
print(num)'''
'''n=6
num=[x**2 for x in range(1,n)]

print(num)'''

'''num=[x for x in range(0,11) if x%2==0]
print(num)'''

'''words=["Hello","String","New"]
s=[word.upper() for word in words]
print(s)'''

'''rows=int(input("Enter row:"))
cols=int(input("Enter column:"))
two=[[col for col in range(cols)] for row in range(rows)]
print(two)

transpose=[[row for row in range(rows)] for col in range(cols)]
print(transpose)'''
'''row =4
col=4

two=[[num for num in range(start,start+col*2) if num%2==0] for start in range(2,2+row*col*2,col*2)]
print(two)'''

'''n=int(input("Enter value: "))
two=[[1 if i==j else 0 for j in range(n) ] for i in range(n)]
print(two)'''

'''n=int(input("Enter value: "))
two=[[1 if i<=j else 0 for j in range(n) ] for i in range(n)]
print(two)

n=int(input("Enter value: "))
two=[[1 if i>=j else 0 for j in range(n) ] for i in range(n)]
print(two)'''

'''n=int(input("Enter value: "))
x=0
two=[[x:=x+1  for j in range(n) ] for i in range(n)]
print(two)'''

n=int(input())
dig=1
nums=[[1 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if(i>j):
            nums[i][j]=0
        else:
            nums[i][j]=dig
        dig+=1
print(nums)
    





