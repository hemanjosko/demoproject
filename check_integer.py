def check_int():
    val = input("Enter your value: ") 
    #print(type(val))

    #if isinstance(val, int):
    if val.isdigit():
        print("i am integer")
    else:
        print("this is not integer")

check_int()
