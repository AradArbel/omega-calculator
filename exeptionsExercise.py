
try:
    num = int(input("enter a number"))
    print(num + 1)
except ValueError:
    print("please enter a vaild input not a string")
except EOFError:
    print("please enter a vaild input not end of file")




