# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and 
# salary and display both.
# If the salary is missing in the function call 
# then assign default value 9000 to salary
# Given:

# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# Expected output:

# Name: Ben salary: 12000
# Name: Jessa salary: 9000
def show_employee(name:str,salary=9000):
    print(f"Employee {name} has salary of {salary}")
def main():
    if __name__=="__main__":
        show_employee("Ben",12000)
        show_employee("Jessa")

main()