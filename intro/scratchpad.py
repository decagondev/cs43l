# lets think about objects and the idea of OOP
# data: field, atribute
# behaviours: functions, methods, procedures
name = "something"
class SomeClassName:

    # initializer (other languages this is part of the constructor)
    def __init__(self, name):
        self.name = name # name field
        self.age = None
        

thisthing = SomeClassName("Dave") # calls __new__() which creates a self ref and calls __init__()
otherthing = SomeClassName("Joe")
thisthing.wooooooo = 3 # live patching of an object
print(thisthing.wooooooo) # => 3
# print(otherthing.wooooooo) # => error