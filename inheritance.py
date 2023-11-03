class Parent:
    variable = "EDEDE"

    def __init__(self, familyname, name):
        self.family_name = familyname
        self.name = name
        self.children = []

    def make_babies(self):
        for child in self.children:
            child.age += 1
        self.children.append(Boy(self.family_name, f"Child{len(self.children)}"))


class Boy(Parent):
    gender = "Boy"
    age = 0

    def __init__(self, familyname, name):
        super().__init__(familyname, name)

    def print_info(self):
        print(f"Im a boy!")
        print(f"I'm {self.age} years old.")
        print(f"My name is {self.name} {self.family_name}")
        print(self.variable)

# class Girl(Parent):
#     gender = "Girl"
#
#     def __init__(self, familyname, familyname):
#         self.name = familyname
#         self.family_name = familyname
#         super().__init__(familyname)
#
#     def print_info(self):
#         print(f"Im a girl!")
#         print(f"I'm {self.age} years old.")
#         print(f"My name is {self.name} {self.family_name}")
#         print(self.gender)


Eve = Parent("Winston", "Borr")
Eve.make_babies()
Eve.make_babies()
for child in Eve.children:
    child.print_info()
Eve.children[0].make_babies()
Eve.children[0].make_babies()
Eve.children[0].make_babies()
Eve.children[0].make_babies()
Eve.children[0].make_babies()
print(Eve.children)
for child in Eve.children:
    print(child.name, child.family_name)
print(Eve.children[0].children)
for child in Eve.children[0].children:
    child.print_info()
    print(child.name, child.family_name)


# ME no get it
