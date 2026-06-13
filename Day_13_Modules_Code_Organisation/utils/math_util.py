def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

print(f'value of __name__ is {__name__}')

if __name__=="__main__":
    if add(2,3) == 5:
        print("Add function test successfull!")

    if subtract(2,3) == -1:
        print("Subtract function test successfull!")

    print("I'm another __name__ block")