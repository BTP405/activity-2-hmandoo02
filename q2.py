import matplotlib.pyplot as plt

def graphSnowfall(t):
    """
    Read snowfall data from a text file, aggregate the values into 10 cm ranges,
    and display the information in a bar chart.

    Parameters:
    - file_path (str): The path to the text file containing snowfall data.
    """
    with open(t, 'r') as file:
        snowfallData = [int(line.strip()) for line in file]
    # here we open the file t (the file name is declared in main) and 'r' tells the program we want to read the file
    # next we strip each line using a for loop in the file so we don't include leading, and trailing whitespaces
    # we make sure to convert each line into int because by default when we read lines they are str.

    snowfallValueMax = max(snowfallData) # here we're finding the max value of the data we pulled from the file
    rangeOfSnowfall = [] # here we make a list for the range for the graph which will show the ranges (0-10, 10-20, etc)
    rangeCountsOfSnowfall = [] # here we make a list for the range count for the graph which will show the data per range
    rangeLimit = 10 # this is our upper range

    while rangeLimit - 10 <= snowfallValueMax: # while the range is smaller than or equal to the max value of data
        rangeCount = 0 # the count for the data to append to our list later
        for data in snowfallData: # for each member of the snowfallData list
            if data <= rangeLimit and data > rangeLimit - 10: # Check if the data from snowfallData falls in the current range
                rangeCount += 1 # Increment count if it does
        rangeCountsOfSnowfall.append(rangeCount) # Append rangeCount to the rangeCountsOfSnowfall list
        rangeOfSnowfall.append(f"{rangeLimit-10}-{rangeLimit}") # Add the current range  to the rangeOfSnowfall list
        rangeLimit += 10 # Increase the upper range by 10 for the next group

    plt.bar(rangeOfSnowfall, rangeCountsOfSnowfall, color='red') # plot the graph using rangeOfSnowfall, rangeCountsOfSnowfall and make the color of the bars red
    plt.yticks(range(max(rangeCountsOfSnowfall)+1)) # make the y ticks increment by only 1 (0,1,2)
    plt.xlabel('Snowfall Ranges (cms)') # X Label
    plt.ylabel('Number of Occurrences') # Y Label
    plt.show() # display the graph

def main():
    graphSnowfall('snowData.txt')

if __name__ == "__main__":
    main()

# 1.
# Lists were chosen for their simplicity, flexibility, and efficiency in storing sequential data such as snowfall measurements, range limits, and counts.
    
# 2.
# I think you can probably avoid loops using libraries such as numpy and using numpy's functions to simplify the logic that you use loops for.
    
# 3.
# Here we're calling the graphSnowfall function and including all our logic in that function so we can just simply call the main and reference the text file we would like to run through the function.
# So I don't think we can avoid a function call here.

# 4.
# We could probably put lines 22 to 29 in another function as a helper function and just call it in graphSnowfall.