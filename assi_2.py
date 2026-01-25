#Task 1: Check if a Number is Even or Odd
#1.Takes an integer input from the user.
a=int(input("Enter the number"))
#2.Checks whether the number is even or odd using an if-else statement.
if a%2==0:
    print("Even")
else:
    print("Odd")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1,51):
    sum=sum+i 

print("sum",sum)
