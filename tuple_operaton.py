#creating tuple
my_tuple=(100,200,300,400,500)
print("my tuple is ",my_tuple)
#printing 1st element
print("1st element in the tuple ",my_tuple[0])
#print last element
print("last element in the tuple (using index [-1])",my_tuple[-1])
print("last element in the tuple (using index [4])",my_tuple[4])
#print tuple length
length=len(my_tuple)
print("tuple length is ",length)
#checking element is present or not using in
n=int(input("enter element to check is present or not:"))
check= n in my_tuple
print("check the user entered element is present or not in tuple ",check)
#concate 2 tuple using + operator
t1=(1,2,3)
t2=(4,5,6)
print("1st tuple is ",t1)
print("2nd tuple is ",t2)
new_tuple=t1+t2
print("new tuple is ",new_tuple)
# repeating a tuple using *
print("repeated tuple",t1*4)
#counting a specific element repetition time using count()
count=my_tuple.count(300)
print("count number of times repeated an element ",count)
# find index of specific element using index()
i=my_tuple.index(200)
print("index of element",i)
#slicing elements
s=(my_tuple[0:3])
print("1st 3 elements ",s)

