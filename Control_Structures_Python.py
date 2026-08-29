#One-Way select statement

a = 5
if (a>0):
    print("+ve integer")


#Indentation in python

#if 1==1:
#print("Indentation is Important")

#above fails due to - IndentationError: expected an indented block after 'if' statement on line 10

#Two-Way select statement
a = -0
if a > 0 :
    print("Positive Integer")
else:
    print("not positive Integer")

#Multi-Way select statement

a = 0
if (a>0):
    print("+ve")
elif (a<0):
    print("-ve")
else:
    print("its 0") 


#nested if
p = 40
q = 20
r = 5
if (p>q):
    if (p>r):
        print("p is greatest")
    else:
        print("r is greatest")
elif (q>r):
    print("q is greatest")
else :
    print("r is greatest")


'''
write a program that displays message given below:
1. if it is a mulitple of 3, display 'Tic'
2. if it is a multiple of 5, display 'Tac'
3. if it is a multiple of 3 and 5, display 'Toe'
4. if it does not satisfy any of the condition, display 'Oooops'
'''

inp = int(input("enter number and I will check if its multiple of 3 or 5 or none of these. Lets try!!"))

if (inp%3 == 0):
    if (inp%5 == 0):
        print("Toe")
    else:
        print("Tic")
elif (inp%5 == 0):
    print("Tac")
else:
    print("Oooops")
 

"""
Ternary Operators
num = int(input("Enter a number: "))
print('Toe' if num % 15 == 0 else 'Tic' if num % 3 == 0 else 'Tac' if num % 5 == 0 else 'Oops')


#The interpreter views your code as a series of nested "if not this, then try that" choices.
'Toe' if num % 15 == 0 else ('Tic' if num % 3 == 0 else ('Tac' if num % 5 == 0 else 'Oops'))

"""



#for-loop

for number in 2,1,4,3,5:
    print("The number is : ", number)


start = 1
end = 10
step = 2

for number in range(start,end,step):
    print("The current number is : ", number)


#for-else loop

for i in range(10):
    print(i)
else:
    print("There was no Break. Finished Printing all numbers FOR you!!")

for i in range(10):
    print(i)
    if i ==3:
        break
else:
    print("There was no Break. Finished Printing all numbers FOR you!!")


#while

number = 5
count = 1

while count <= number:
    print("The count is : ", count)
    count+=1

#while-else

i = 1

while i < 10 :
    print(i)
    i+=1
else:
    print("There was no Break. Finished printing numbers in a While !!!!")


#Exercise Programs for for-loop
for number in range(1,10):
    print("The current number is : ", number)

print("--------------------------------------")

for number in range(1,7,2):
    print("The current number is : ",number)

print("--------------------------------------")

for number in range(5,0,-1):
    print("The current number is : ",number)



#Nested Loops


print("---- for -----")
number_of_passengers = 5
number_of_baggages = 2
security_checks = True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggages+1):
        if(security_checks==True):
            print("Security check of passenger ", passenger_count, "-- baggage :", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger ", passenger_count,"-- baggage :", baggage_count,"baggage cleared")

#Optimized
print("----- Optimized -----")
number_of_passengers = 5
number_of_baggages = 2
security_checks = True
status = "baggage cleared" if security_checks else "baggage not cleared"
for passenger_count in range(1,number_of_passengers+1):
    for baggage_count in range(1,number_of_baggages+1):
        print("Security check of passenger ", passenger_count,"-- baggage :",baggage_count, status)


#using While
print("----- While ----")
number_of_passengers = 5
number_of_baggages = 2
security_checks = True
for passenger_count in range(1,number_of_passengers+1):
    baggage_count = 1
    while baggage_count <= number_of_baggages:
        if (security_checks == True):
            print("Security check of passenger ", passenger_count,"-- baggage :",baggage_count,"baggage cleared")
        else:
            print("Security check of passenger ", passenger_count,"-- baggage :", baggage_count,"baggage not cleared")
        baggage_count+=1


'''
Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6

Note: Initialize the number with various values and test your program.
'''

inp = int(input("Enter a number and I will add digits. Cool right. Now please enter."))

total = 0
while inp > 0:
    rem = inp%10
    total+=rem
    inp = inp//10
    print(inp)
print("Total is : ", total)

"""
Alternates: 

inp = input("Enter a number: ")
total = sum(int(digit) for digit in inp if digit.isdigit())
print("Total is:", total)


inp = input("Enter a number: ")
total = sum(map(int, inp))
print("Total is:", total)

"""


#Break
#Continue
#Pass

for i in range(1,5):
    if i == 3 :
        break
    print(i)

for i in range(1,5):
    if i == 3 :
        continue
    print(i)

for i in range(1,5):
    if i == 3 :
        pass
    print(i)


# in usage 

for alpha in ('a','b','c','d','e'):
    if alpha in ('a','b'):
        print("first  two")
    else:
        print("Others")


#Program to check Prime


