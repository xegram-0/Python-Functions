# Exercise 7: Assign a different name to function 
# and call it through the new name

# Below is the function display_student(name, age). 
# Assign a new name show_tudent(name, age) to it 
# and call it using the new name.

# Given:

# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)

# You should be able to call the same function using

# show_student(name, age)
def display_student(name, age):
    print(name, age)

# I am so confused about this
# Conclusion:
# Just rename a function to call it
def main():
    if __name__=="__main__":
        name = input("Enter name: ")
        age = input("Enter age: ")
        show_student = display_student
        show_student(name, age)

main()