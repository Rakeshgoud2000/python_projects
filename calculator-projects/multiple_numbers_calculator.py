def add(*args):
    return sum(args)

def sub(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def mul(*args):
    reult = 1
    for num in args:
        result *= num
    return result

def div(*args):
    result = 0
    for num in args[1:]:
        if num == 0:
            return "cant division by Zero"
        result /= num

    
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
            numbers =  input("Enter numbers separately by space : ")
            nums = [float(n) for n in numbers.split()]
            operation = opertion_dict[user_input]
            result = operation(*nums)
            print("result : ",result)

        else:
            print("Invalid input")

cal()