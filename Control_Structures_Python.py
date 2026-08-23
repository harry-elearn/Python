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
    print("There was no Break. Finished Printing all numbers!!")

for i in range(10):
    print(i)
    if i ==3:
        break
else:
    print("There was no Break. Finished Printing all numbers!!")