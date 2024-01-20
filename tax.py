n=int(input("Enter the number of items bought:"))
pricel=[]
sum=0
for i in range(0,n):
    a=float(input("PRICE of item:"))
    pricel.append(a)
    sum+=a

total=sum*(1.08)
print("Input :",pricel)
print("Total Cost :",total)
