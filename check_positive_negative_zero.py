# Program to check positive, negative and zero numbers
pos = 0
neg = 0
zero = 0
n=int(input("enter user range: "))
for _ in range(n):
    num=int(input("enter number to check positive,negative or zero: "))
    if num > 0:
        print(num,"is positive number.")
        pos+=1
    elif num < 0:
        print(num,"is negative number.")
        neg+=1
    else:
       print(num,"is zero.")
       zero+=1
print("total number positive is ",pos)  
print("total number negative is ",neg)  
print("total number zero is ",zero)       