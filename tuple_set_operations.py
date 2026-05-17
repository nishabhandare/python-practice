print("----- TUPLE AND SET OPERATIONS -----")
# user input list
item=input("enter items: ")
my_list=list(map(int,item.split()))
print("user entered items in list format: ",my_list)
# convert list into tuple
first_tuple=tuple(my_list)
print("user entered list converted into tuple is:" ,first_tuple)
#count tuple length
print("length of tuple: ",len(first_tuple))
if len(first_tuple)>0:
    # access 1st element
    print("1st element in the tuple: ",first_tuple[0])
    #access last element
    print("last element in the tuple: ",first_tuple[-1])
    #reversed tuple
    print("reverse tuple: ",first_tuple[::-1])
else:
    print("empty tuple")

# convert tuple into set to remove duplicates
#user enter 2nd list then convert into tuple
element=input("enter item: ")
my_list2=list(map(int,element.split()))
second_tuple=tuple(my_list2)
print("2nd tuple is ",second_tuple)
#convert tuple into set
set1=set(first_tuple)
print("1st tuple converted into set:",set1)
set2=set(second_tuple)
print("2nd tuple converted into set:",set2)
new_set=set1 | set2
print()
print("union of both sets:",new_set)
#sorting a new set
print("sorted new created set: ",sorted(new_set))