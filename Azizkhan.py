def fizzbuzz(number):
    """
    fizzbuzz checks if the given number is divisible by 3, 5
    or both and returns fizz, buzz or fizzbuzz respectively.
    Otherwise, it will return the same number.
    
    Params:
    ------
        number (int): user provided number, assumed to be valid
        
    returns:
        str : Fizz if divisible by 3
        str : Buzz if divisible by 5
        str : FizzBuzz if divisible by 3 and 5
        number (int): Same same parameter provided number
    """
    
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
        
    else:
        return number
        
    
def main():
    """
    main game function. Prompts the user for a number and 
    validates user input is valid as an integer.
    
    
    Params:
    ------
        None
        
    Returns:
    -------
        None
    """
    
    user_number = input("Enter a number: ")
    
    if user_number.isdigit():
        result = fizzbuzz( int(user_number) )
        print(result)
        
    else:
        print("invalid input, quitting...")
        return 
    
    
    
if __name__ == "__main__":
    main()

def is_even(num):
    """
    Determine if a number is even or odd
    
    
    return "even" if number is divisible by 2
    otherwise returns "odd"
    
    Parameters:
    num (int): user number
    
    Returns:
    str: "even" if num is divisible by 2, otherwise "odd"
    """
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
        
def main():
    """
    main function. Prompts the user for a number 
    parameters: none
    returns: none
    """
    num = int(input("Enter a number: "))
    
    result = is_even(num)
    print("Your number is ", result)
    
if __name__ == "__main__":
    main()






















def discount(price, student):
    """
    Calculate the discounted price
    
    
    
    Return price * 0.8 if price > 100 and student
    price * 0.9 if price > 100 but not a student
    otherwise return the original price
    
    Parameters:
    price (float): Original price 
    student_input (bool): True if the customer is a student, otherwise False
    
    Returns:
    float: Final price after discount
    

    """
    if price > 100 and student:
        return price * 0.8 # 20 % discount
        
    elif price > 100 and not student:
        return price * 0.9 # 10% discount
        
    else:
        return price # no discount
        
        
def main():
    price = float(input("Enter prace: "))
    student_input = input("Are you student, Yes/No: ").strip().lower() 
    
    if student_input == "yes":
        student = True
    else:
        student = False
        
    final_price = discount(price, student)
    print("Final price: ", final_price)
        
if __name__ == "__main__":
    main()









def division(user_input):  
    """

return "FizzBuzz" if user_input is divisible by 3 and 5
"Fizz" if user_input is divisible by 3
"Buzz" if user_input is divisible by 5


Paramaters:  user_input = int, the number to check 

returns:  str: result of the FizzBuzz logic
    """




    if user_input % 3 == 0 and user_input % 5 == 0:
        return "FizzBuzz"
    elif user_input % 3 == 0:
        return "Fizz"
    elif user_input % 5 == 0:
        return "Buzz"
    else:
        return user_input

def main():
    user_input = input("Enter a number: ")
    if user_input.isdigit():  
        user_input = int(user_input)
        result = division(user_input)
        print(result)        
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
