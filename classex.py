#simple class ex
class my:
    print("\n1.simple class ex.")
    print("this msg for class,'welcome!'")
m=my

#class with simple function
class myclass:
    def myfun(self):
        print("\n2.class ex with a simple function.")
        print("welcome from a class method.")
my=myclass()
my.myfun()

#class with function and parameters.
class myExample:
    def funex(self, roll_no, name, age):
        print("\n3.class example with function using a parameters.")
        print("welcome!")
        print("roll_no: ",roll_no," Name:",name," Age: ",age,".")
e=myExample()
e.funex(1,"sathish",21)
e.funex(2,"raj",22)

# class with __init__() only.
class myclass:
    def __init__(self):
        print("\n4.class ex with a __init__() method.")
        print("hello,welcome in coding.")
m=myclass()

#class with __init__()method and parameter.
class ex:
    def __init__(self,name):
        print("\n5.class ex with __init__() and parameter name.")
        print("welcome!",name)
        print("hello ",name)
e=ex("asha")
ep=ex("asasasa")

#class wirth __init__() and parameter default value.
class example:
    def __init__(self,name,age,salary=50000):
        print("\n6.class ex with __init__() method and default value.")
        print("hello!")
        print("welcome ",name," Age:",age," Salary:",salary,".")

ex=example("gauri",32,40000)
e=example("radha",21)


#class with a __init__() and self keyword.
class base:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("\n7. Class example with __init__() and self keyword.")
        print("msg print from a constructor.")
        print("welcome in python programming ",self.fname,self.lname)
    def printing(self):
        print("msg print fron a method")
        print("hello ",self.fname,self.lname)
b=base("john","don")
b.printing()
