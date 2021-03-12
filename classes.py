#functions
def my_Func(name):
    print("hi",name)
my_Func("Akbar")


def sum(a,b):
    return a+b;
a=int(input("Enter first input:"))
b=int(input("Enter second input:"))
print("sum=",sum(a,b))


def sec_Func(name,psno,emailid):
   if name=="Akbar":
       return name;
   else:
       return psno;


#Classes
name=input("Enter the user name:")
psno=int(input("Enter the users psNo:"))
emailid = input("Enter the users emailid:")
print("Details=",sec_Func(name,psno,emailid))


class Employee:
    name="Akbar"
    psno=769
    email="ska"
    def my_Fun(self):
        print("Name:%s\nPsno:%d\nEmail:%s"%(self.name,self.psno,self.email))
emp=Employee()
emp.my_Fun()



