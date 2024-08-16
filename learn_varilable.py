# no need to mention the data type
a = 10
b = "Lingesh" # single quote can also be used.
c = True  # case-sensitive, should not use true
d = 12.3

print(a)
print(b)
print(c)
print(d)

# variable can be reused with different type
a = 'Dhanusu'
print(a)

# type() method can help with finding data type
print(type(a))
print(type(c))

# Type casting can be done using,
a = int(2)
b = float(45)
print(a)
print(b)

# Variables are case sensitive.
A = "Lingeshvaran"
print(a)
print(A)

# multiple variables declared in one line
x,y,z = 12,34,"World"
print(x)
print(y)
print(z)

# Single value can be assigned to multiple variables like,
x = y = z = 234
print(x)
print(y)
print(z)

# Values in a collection can be assigned to individual variables. Note that number of variables should be equal to number of elements in the collection.
colors = ['red','blue','black']
p, q, r = colors
print(p)
print(q)
print(r)

# comma and also plus can be used to print multiple things.
print(x+y+z)
print(x,y,z)

# Global variables are the ones declared outside of the function.
h = "out"
def func1():
    print(h)
func1()

# we can create a global variable inside a function by using global keyword. Note that global keyword and initialization should not be in the same line.
def func2():
    global u
    u = 'inside the function'
func2()
print(u)

# To change the value of the global variable, it should be defined first with global keyword. Global declaration should at the first line.
# When a global varilable value is changed simply without global declaration at the begining of the method, then it will be considered as local variable.
def func3():
    global h
    print(h)
    h = 'changed inside'
func3()
print(h)