def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "cant divisiable by zero"
    else:
        return x/y
    
opertion_dict = {"add":add,"sub":sub,"mul":mul,"div":div}

def cal():
    while True:
        print("Welcome to calculator Choose Options")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'quit' to stop program")
        user_input = input("Enter your options :").lower().strip()

        if user_input == "quit":
            print("Thank you and visit again")
            break
        elif user_input in opertion_dict:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            operation = opertion_dict[user_input]
            result = operation(num1,num2)
            print("result : ",result)

        else:
            print("Invalid input")

cal()
        