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

