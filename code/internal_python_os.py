import os

str = ""
str = os.getcwd()
print(str)
print(type(os.getcwd()))

os.chdir("..")  # one level up
print(os.getcwd())

parent_dir = os.path.dirname(os.getcwd())
print(parent_dir)

os.chdir(parent_dir)
print("Now in:", os.getcwd())
