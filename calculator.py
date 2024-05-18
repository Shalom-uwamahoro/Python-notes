def add(a,b):
    answer=a+b
    return answer

def substract(a,b):
    answer=a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def remainder(a,b):
    answer=a%b
    return answer

def power_of(a,b):
    answer=a**b
    return answer

#creating a function that can add any number of numbers

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total   # always ensure you return outside the loop so that it won't return before finishing looping

def multiplication(*numbers):
    product = 1
    for number in numbers:
        product*=number
    return product

# creating a function that accepts any number of keyword arguments

def create_sentence(**words): # the 2 asterisks turns the argument words into a dictionary by default
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence

#creating a function that takes in any number of both positional and keyword arguments

def sum_and_greet(*args, **kwargs):
    total = 0
    for number in args:
        total += number
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    greeting = f"Hello {first_name} {last_name}, the sum of {list(args)} is {total}"
    return greeting
    

    
