#Identifiers 
#Keywords 
#DeclaringVariables 
#DynamicTyping
num = 12
print(num,type(num))
num = "A"
print(num,type(num))

#input()

input_var = input("please enter data as per your wish")
print(input_var)

#adding from the Github edit option from web


#print()
#Format specifiers

p = "India"
q = 101.101
r = 501
print(p,q,r)
print(p,q,r,sep=":")
print(p,q,r,end=" ")
print(p,q,r)
print("q=%0.2f"%q)
print("q=%1.1f"%q)
print("q=%7.1f"%q)
print("r=%8d" %r)
print("r=%-8d" %r)
print("r=%4d"%r)
print("Value of p is %s" %p)
print("Value of p is %%s", p)
print("Value of p is %s" %p)


#Operators
#Arithmetic#Relational#Assignment#Logical
# Type Conversion

num1 = 10
num2 = '20'
#result = num1 + num2 
#Python does not support implict type conversion. Above cause Type Error
# Below is Explict Type conversion (Also called as Type Casting)
result = num1 + int(num2)
print(result)

