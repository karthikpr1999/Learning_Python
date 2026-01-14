#First we need three variables for storing the values
#Number 1
number_1 = int(input("Enter first number: "))
#Number 2
number_2 = int(input("Enter second number: "))
#Number 3
number_3 = int(input("Enter third number: "))
#Now evaluating which is greatest number using if statements
#if Number 1 is greater than Number 2 then move forward to evaluate other two numbers

if number_1 > number_2:
    if number_1 > number_3:
        print("Number 1 is largest number: ",number_1)
    else:
        print("Number 3 is largest number: ",number_3)
else:
    if number_2 > number_3:
        print("Number 2 is largest number: ",number_2)
    else:
        print("Number 3 is largest number: ",number_3)

    