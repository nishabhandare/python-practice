print("----- LIST OPERATIONS PROGRAM -----")
total=0
even=0
odd=0
# creating a list using user input.
num=input("enter list element: ")
element=list(map(int,num.split()))
num=element
print("numbers in the list : ",num)
# appending element using user input.
val=int(input("enter value to append in the list: "))
num.append(val)
print("appended list is ",num)
# inserting element using user index and element.
index=int(input("enter index to add element: "))
value=int(input("enter value to add user index: "))
num.insert(index,value)
print("inserted list is ",num)
# removing element using user input.
r=int(input("enter number to remove."))
if r in num:
    num.remove(r)
    print(r," element is present and removed.")
    print("removed list is ",num)
else:
    print("element is not present in the list.")
#counting list length.
length=len(num)
print("length of list is ",length)

maxi=num[0]
mini=num[0]
for i in num:
 #addition of all elements in the list.
        total=total+i
 #find the maximum element in the list.
        if i > maxi:
            maxi=i
 #find the minimum element in the list.         
        if i < mini:
            mini=i
 # counting even and odd numbers.
        if i%2==0:
            even+=1
        else:
            odd+=1
#printing msg
print("addition of all element is ",total)
print("total even numbers: ",even)
print("total odd numbers: ",odd)
print(mini," is a minimum number in the above list.")
print(maxi," is a maximum number in the above list.")
#sorting a list
num.sort()
print("sorted list: ",num)
#reversing a list
num.reverse()
print("reversed list: ",num)