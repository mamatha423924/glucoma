sentence = input("Enter a sentence: ") # get input from user

# create a list of words from the sentence
words = sentence.split()

longest_word = "" # initialize the longest word variable

# loop through each word in the list
for word in words:
    # check if the word contains only letters
    if word.isalpha():
        # check if the length of the word is greater than the length of the current longest word
        if len(word) > len(longest_word):
            longest_word = word # update the longest word variable

print("The longest word in the sentence is:", longest_word)
