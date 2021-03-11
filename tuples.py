#slices
squares = [1,2,3,4,5,6,7,8,9]
print(squares[1:-1])
print(squares[7:])

#tuples
square = (1,2,3,4,5,6)
print(square)

nums = [4,5,6]
msg = "Numbers:{0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)


#other functions
print("Akbar".join(["Shaik","Basha"]))
print("Shaik,kjl".split('kjl'))
print("Shaik,kjl".split('no'))
print("Hello ME".replace("ME", "world"))
print("Hello ME".replace("MEI", "world"))
"""


double = lambda x: x*2
print(double(7))
