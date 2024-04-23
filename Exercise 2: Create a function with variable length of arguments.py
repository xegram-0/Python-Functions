# Exercise 2: Create a function with 
# variable length of arguments


def func1(*num):
    print("Printing values:")
    for i in num:
        print(i)

def main():
    if __name__=="__main__":
        func1(20,40,60)
        func1(80,100)
main()