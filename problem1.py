#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

n = float(input("Enter a number: "))
if n/6 == int(n/6) and n/8 != int(n/8):
    print(f"{n} is Frue")
else:
    print(f"{n} is not Frue")