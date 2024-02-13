def wordCount(t):
    
	f = open(t, "r") # Open the file specified by the 't' in read mode
	wordDictionary = dict() # Initialize an empty dictionary to store word counts
	wordLineCount = 1 # Initialize a counter variable to track the line number 
	
	for word in f: # reading each line in the file a for using loop
		word = word.strip() # Remove leading and trailing whitespace from the line
		word = word.lower() # Convert the line to lowercase to standardize word case
		individualWords = word.split(" ")	# Split the line into words			

		for word in individualWords: # Iterate over each individual word
			if word in wordDictionary: # If: the word is already in the dictionary
				wordDictionary[word].append(wordLineCount) # If the word is present, append the line number to its list of occurrences
			else: # Else: the word is not in the dictionary
				wordDictionary[word] = [] # Create a new list for the word in the dictionary
				wordDictionary[word].append(wordLineCount) # Append the current line number to the list of occurrences for the word
		wordLineCount += 1 # Increment the line number counter
	return wordDictionary # returns a dictionary for the words and their line numbers

def main():
    print(wordCount("testWord.txt"))

if __name__ == "__main__":
    main()
	

# 1.
# I chose a dictionary data structure because it allows for efficient lookup of words and their associated list of line numbers. 
# In this case, each word encountered in the file is used as a key in the dictionary, and its associated value is a list of line numbers where the word occurs.
	
# 2.
# I don't think you can avoid a loop here because you need to iterate through the file and make sure all the words don't have trailing spaces, as well as
# making them all lowercase. Then you need to check if the words are in the dictionary or not already which requires another loop. If there is a library that does this already you can avoid
# loops by calling functions from that library.
	
# 3.
# We only have 1 function here which is wordCount so I don't think we can avoid this function call unless we put all of our logic in the main function.
	
# 4.
# my for loops go through different parts (first for loop going through the file and then second going through the words individually) so I think we can't avoid repetitive code here unless I use
# different functions to replace parts