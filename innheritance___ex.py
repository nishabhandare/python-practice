#inheritance example
# 1.single inheritance
#simple parent class with constructor and a simple function for printing msg and use self keyword
class base:
    def __init__(self,fname,lname):
        print("\n1.base class:")
        print("\nbase class and its constructor and its one method.")
        self.fname=fname
        self.lname=lname
        print("msg print from a base constructor.")
        print("welcome in python programming ",fname,lname)
    def printing(self):
        print("\nmsg print fron a base class method")
        print("hello ",self.fname,self.lname)
b=base("john","don")
b.printing()
        
 #child class and run its own constructor       
class child(base):
    def __init__(self,Fastn,Lastn):
        print("\n2.child class:")
        print("\nchild class and run its own constructor.")
        self.Fastn=Fastn
        self.Lastn=Lastn
        print("msg printing from child constructor.")
        print("hello, ",Fastn,Lastn)
c=child("ashish","kale")
        
#other child class for run a parent class constructor using a first limne of calling a parent class constructor.
class derived(base):
    def __init__(self,fname,lname):
        base.__init__(self,fname,lname)
        print("\n3.derived class")
        print("\nderived class for the calling of parent class constructor using a classname and constructor define.")
        self.fname=fname
        self.lname=lname
        print("msg printing from a derived class constructor")
        print("hello ",fname,lname)
d=derived("yash","patil")   

class sub(base):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("\n4.sub class")
        print("sub class for a run a base class constructor using a 'super' keyword.")
        self.fname=fname
        self.lname=lname
        print("\nmsg printting from a sub class constructor.")
        print("student name is ",fname,lname)
s=sub("aastha","suryvanshi")


#simple class inheritance example
#parent class
class parent:
    def p1():
        print("\n1.simple inheritance ex.")
        print("hello from a parent.")
p=parent
p.p1()

#child class with simple method
class child(parent):
    def c1():
        print("\n2.child class inherit from a parent class.")
        print("welcome in child class.")
c=child
c.p1() 
c.c1()  

#derive class method and parameter
class derived(parent):
    def d1(name,age):
        print("\n3.derived class with method and parameter.")
        print("welcome in derived class ,name: ",name," age: ",age,".")
d=derived
d.p1()
d.d1("sarthk",12)   
   
