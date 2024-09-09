class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"hello, my name is {self.name}, I am {self.age} years old, and I am 100% {self.gender}.")

#create an instance of the person class
person1 = person("George Watson", 65, "male")

#call the introduece method to display the person's information
person1.introduce()