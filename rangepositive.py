n=int(input("Enter no of elements in list:"))
y=[]
for i in range(n):
    x=(input("enter element:"))
    y.append(int(x))
print("The input list is:",y)
t=[]
for num in y:
    if num >= 0:
        t.append(num)
print("The output list is",t)