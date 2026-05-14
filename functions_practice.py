print ("--- function ---")
#addition of two parameters
print("\naddition function")
def add(a,b):
    return a+b
print("using a function addition is ",add(3,5),".")
#even odd check using function 
print("\neven odd checker function")
def even_odd(num):
    if num%2==0:
        print(num,"is an even number.")
    else:
        print(num,"is an odd number.")
even_odd(5)