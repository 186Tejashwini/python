# ✅ Classes act like blueprints or templates for creating objects.
#    Just like a blueprint for building houses — you define once, build many.

class Person():
    # ❌ WRONG: You had written "__it__" instead of "__init__"
    # ✅ "__init__" is a special method called a **constructor**.
    #    It runs automatically when you create a new object from this class.
    def __init__(self, name, age, color):  # <- Make sure it's spelled exactly "__init__"
        # ✅ self refers to the current object being created
        #    It's like saying: "store this value inside this particular object"
        self.name = name    # storing the name given during object creation
        self.age = age      # storing the age
        self.color = color  # storing the color


    #Date of birth method
    def year_of_birth(self):
            return 2021-self.age
    #Projected Age
    def project_age(self,years=5):
         return self.age+years

# ✅ Now we create (or "instantiate") a new object from the class
#    Think of this as building a real person based on the blueprint
new_Person = Person('Elon Musk', 38, 'blue')

# ✅ Accessing an attribute of the object
#    We're asking: "Hey, new_Person, what's your favorite color?"
print(new_Person.color)  # Output: blue
print(new_Person.year_of_birth())
print(new_Person.project_age())
print(new_Person.project_age(years=10))


'''#---------------------------------------------------------------------------
 
# 📦 Definition of an Object in Python:

# ✅ An object is a real-world instance of a class that contains both data (attributes) and behavior (methods).

# 🔁 Analogy:
# Think of a class as a cookie cutter 🍪 — a blueprint.
# Each cookie you make from it is an object.
# So, a class defines what something should look like,
# and the object is the real thing you use in your program.

# 👇 Example to understand objects:

class Car:
    def __init__(self, brand):
        self.brand = brand

# Creating an object from the Car class
my_car = Car("Tesla")  # <-- 'my_car' is an object of class 'Car'

# Accessing object attribute
print(my_car.brand)    # Output: Tesla

# 🧠 Summary:
# - 'Car' is the class (blueprint)
# - 'my_car' is the object (real car made using the blueprint)
# - '.brand' is an attribute stored inside the object '''

