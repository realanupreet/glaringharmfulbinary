# try:
#     x = int(input("input an integer :"))
#     print(x)
# except ValueError:
#     print("something went wrong...try again")
# else:

#     print("nothing went wrong")
# finally:
#     print("FInally")


# import os


# countfile = open(os.path.join(os.path.dirname(__file__), 'hello.txt'), "w")

# countfile.write("this is the new text written in a file in ")
# countfile.write(os.path.dirname(__file__))


# for i in range(5):
#     file = open(os.path.join(os.path.dirname(
#         __file__), str(i)+".txt"), "w")
#     file.write("this is file number: ")
#     file.write(str(i))

# countfile.close()
from hello import student


class Myclass(student):
    pass

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, "is", self.age)


p1 = Myclass("john", 45)
print(p1.name, "is", p1.age)
p1.display()
print(p1.name, "has taken", p1.subject)
