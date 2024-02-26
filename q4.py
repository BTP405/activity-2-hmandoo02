def printStats(t):
    """
    Reads numbers from a file (numbers.txt) and prints statistics about them.

    Parameters:
    - t (str): The file name containing numbers.
    """
    numbersList = []  # Initialize an empty list to store the numbers.
    with open(t, 'r') as file: # open file to read each line
        for line in file:  # Iterate through each line in the file.
            for number in line.split():  # splitting the lines into individual numbers
                numbersList.append(float(number))  # converting numbers from string to float and appending them into the list I made earlier
        if numbersList:  # Checking if the list has numbers in it
            printStatsDecorator(numbersList)  # calling the deorator function

def printStatsDecorator(numbers):
    """
    Prints statistics about numbers input from the function printStats.

    Parameters:
    - numbers (list of float): The list of numbers.
    """
    numbersCount = len(numbers)  # Get the total count of all numbers in the list.
    averageOfNumbers = sum(numbers) / numbersCount  # Calculate the average of the sum of numbers.
    biggestNumber = max(numbers)  # Find the biggest number in the list using max.
    print("The numbers read from the file:", numbers)  # Print the list of numbers read in from the file.
    print("The total amount of individual numbers in the file:", numbersCount)  # Print the total count of all numbers in the list.
    print("The average of the numbers read from the file:", averageOfNumbers)  # Print the average of the sum of numbers.
    print("The biggest number from the file:", biggestNumber)  # Print the biggest number in the list using max.

def main():
    printStats('numbers.txt')

if __name__ == "__main__":
    main()

# 1.
# I chose a list as my data structure for this code because a list lets me simply store numbers but ordered and still changeable.
# I only really need the list to store numbers and reference them in calculations so I don't need a complicated data structure.

# 2.
# I need to iterate through the file's lines and then split it into individual numbers so I don't think we can avoid a loop here 
# because it works perfectly for a file that could contain any number of numbers.

# 3. 
# Yea technically you could completely put the logic of the decorator function into printStats but other than that we only have the main where we don't want to put all our logic.

# 4.
#  I don't think we have much repetitive code since my code is just loops to iterate through the file and then the decorator function to do calculations based on the numbers from the list and print the list. 