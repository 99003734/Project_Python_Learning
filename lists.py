student_Id = ["Akbar",["basha",21,2654],20,3734]
print(student_Id[0])
print(student_Id[1][0])


student_Id = ["Akbar",["basha",21,2654],20,3734]
print("Akbar" in student_Id)
print("Akbar"not  in student_Id )

student_Id = ["Akbar","Basha","Shaik"]
for Akbar in student_Id:
    print("yes")
    break

num1 = list(range(0,20))
print(num1)



#try and except
n=int(input())
try:
    if n>3:
        print("HELLO")
    else:
        print("BYE")

except:
    if n<0:
        print("hello")
    else:
        print("bye")



#if and elif
num1 = 20
num2 = 22
if num1>num2:
    print("Hello")
elif num1<num2:
    print("Hi")

#2.if and elif
x = 4
y = 2
if  1 + 3 == y or  x == 4 and not 7 == 8:
  print("Yes")
elif x > y:
  print("No")


#strings
second_Input = int(input())
print(second_Input)
second_Input = 43
print("Hello"+str(second_Input))

t1 = int(input("Enter the number:"))
print(t1)
print("Hello"=="ello")
print(22>=22.0)
print("akbar">"aksar")


#Function
def my_Function():
    print("Hello")
    print(("Hey"))
my_Function()