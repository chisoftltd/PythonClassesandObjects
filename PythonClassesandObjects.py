# Python Classes and Objects
class MyClass:
    x = 5
p1 = MyClass()
print(MyClass.x)
print(p1.x)
print()

# The __init__() Function
# The self Parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Benjamin", 47)

print(p1.name)
print(p1.age)
print()

class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc1(abc):
    print("Hello my name is " + abc.name)

p1 = Person1("Joy", 36)
p1.myfunc1()

# Modify Object Properties
p1.age = 55
print(p1.age)

# Delete Object Properties
del p1.age
print(p1.name)
# print(p1.age)
print()

# Delete Objects
print(p1.name)
del p1
#print(p1.name)

# The pass Statement
class Person:
  pass
