# 🧠 CLASS: A blueprint for creating objects (real-world things like a person, car, etc.)

class Person():
    # 🔧 The __init__ method is called a "constructor"
    # It automatically runs when we create a new object from this class
    def __init__(self, name, age, color):
        # 'self' represents the current object being created
        self.name = name      # store the name of the person
        self.age = age        # store the person's age
        self.color = color    # store their favorite color

    # 🗓️ A method to calculate year of birth
    def year_of_birth(self):
        return 2021 - self.age  # Example base year is 2021

    # ⏳ A method to calculate the projected age in the future
    def project_age(self, years=5):  # default projection = 5 years
        return self.age + years

# 👷 Creating an object from the Person class
new_Person = Person('Elon Musk', 38, 'blue')

# 🔍 Accessing attributes and methods
print(new_Person.color)                # Output: blue (his favorite color)
print(new_Person.year_of_birth())      # Output: 1983
print(new_Person.project_age())        # Output: 43 (default projection)
print(new_Person.project_age(10))      # Output: 48 (after 10 years)


# ______________________________________________________________________________________
# 👪 INHERITANCE

# Parent = Person (base class)
# Child = Astronaut (inherits everything from Person, and adds more stuff)

# 🧑‍🚀 Creating a child class from the Person class
class Astronaut(Person):
    # Constructor for Astronaut that also uses the constructor of Person
    def __init__(self, name, age, color, mission_length_in_months):
        # 🧬 super() allows us to reuse the parent (Person) class constructor
        super().__init__(name, age, color)
        self.mission_length_in_months = mission_length_in_months  # unique to astronauts

    # 🔁 Method to calculate age after returning from space
    def age_on_return(self):
        # ⏱️ Converts mission duration in months to years
        return self.project_age(years=self.mission_length_in_months / 12)

# 👨‍🚀 Creating an Astronaut object
new_astronaut = Astronaut('Nick', 99, 'purple', 48)

# 🔍 Accessing inherited and new methods/attributes
print(new_astronaut.age)                # Output: 99
print(new_astronaut.age_on_return())    # Output: 103.0 (after 4 years in space)

#super() lets a child class use methods and properties from its parent class — without having to rewrite them!



