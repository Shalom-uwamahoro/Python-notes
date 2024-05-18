def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)

#Apply 'if statement'/else statement/ elif statement condition whose result is always boolean(check if operation is true or false)
        
def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 != 0:
            print(number)

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(number)

def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2 != 0:
            print(f"{number} is odd")
        else:
            print(f"{number} not odd")

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(f"{number} is divisible by 2")

        elif number %3 == 0:
            print(f"{number} is divisible by 3")

        elif number %5 == 0:
            print(f"{number} is divisible by 5")

        else:
            print(f"{number} is not divisible by 2,3 or 5")

#fizzbuzz question

def fizzbuzz(n):
    numbers = range(n)
    for number in numbers:
        if number%3 == 0:
            print(f"fizz")

        elif number %5 == 0:
            print(f"buzz")

        else:
           print(f"fizzbuzz")

def countdown(n):
    while n>0:
        print(n)
        n-=1

def countdown_to_five(n):
    while n>0:
        print(n)
        if n==5:
            break
        n-=1

def divisible_by_seven(n):
   x=0
   while x<=n:
       x+=1
       if x%7 !=0:
           continue
       print(f"{x} is divisible by 7")

# question: Using while, if and continure, print all the odd numbers between 0 and 100
       
def check_odd():
   x=0
   while x<100:
       x+=1
       if x%2 ==0:
           continue
       print(f"{x} is odd")
