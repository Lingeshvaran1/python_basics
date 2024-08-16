# simple if ends with colon, spacing is used to identify the block of code.
a = 10
b = 20
if a < b:
    print('a is less than b')

# else if can be written as elif
if a > b:
    print('a is greater than b')
elif a < b:
    print('a less than b 2')

# like java, else will come at last.
if a > b:
    print('a is greater than b')
elif a < b:
    print('a less than b 3')
else:
    print('a and b are same')

# if only one line to execute then it can be written in the single line.
if a < b: print('a less than b 4')

# if only one line to execute in both if and else then it can be written in the single line.
print('a less than b 6') if a < b else print('a is greater than b')

# if only one line to execute in if, else if and else then it can be written in the single line.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# "AND" is used for combining more than one condition.
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR is used for either or condition.
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# not is used as same !=
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# if the statement doesnt have a body then use pass.
a = 33
b = 200

if b > a:
  pass