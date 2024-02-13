
def checkPrimeNumber(number):
    """
    Function to check if the given number is prime or not.
    Parameters:
    - number (integer): the parameter inputted to check if its prime or not
    Returns:
    - bool: if the number inputted is prime then the function returns true, if it isn't then returns false.
    """
    if number == 1:
        return False
    for x in range(2, number):
        if (number % x) == 0:
            return False
    return True

def getPrimeNumbers(number):
    """
    Function to generate a list of prime numbers between 2 and a given number (number).
    Parameters:
    - number (integer): the parameter used to generate the limit of prime numbers.
    Returns:
    - list: the function returns a list containing prime numbers between 2 and number.
    """
    return [x for x in range(2, number + 1) if checkPrimeNumber(x)]
    # for each element in range(starts at 2, stops at number + 1 only returns the number if checkPrimeNumber returns true)

def main():
    print("What number would you like to check prime numbers for: ")
    number = input()
    result = getPrimeNumbers(int(number))
    print("Prime numbers between 2 and " +str(number)+" : " +str(result))

if __name__ == "__main__":
    main()

# 1.
# I used a list for collection and returning the collection of prime numbers 
# because lists are good for iterating or indexing between a list of things such as prime numbers

# 2.    
# I use a for loop in my function (checkPrimeNumber) because without it the code would have to 
# slowly and unoptimally go through the list line by line instead of quickly using the for loop

# 3.    
# I can't avoid a function call here because I am using a helper function to check if a number is prime or not
# instead of including that logic in my getPrimeNumbers function. I also call getPrimeNumbers in 
# main which is another function call

# 4.    
# checkPrimeNumber goes through every number between 2 and the specified 
# number to check if each number between those numbers are prime.

# getPrimeNumbers generates a list of prime numbers between 2 and the specified number using checkPrimeNumber 
# to see if the number in the list is prime or not.

# lastly my main function takes input from the user and calls getPrimeNumbers to output the list