# Import `re` to enable the use of `re.sub()`
import re

def count_words(sentence):
    # Convert the entire sentence to lowercase
    lower_sentence = sentence.lower()

    # Use `re.sub()` and a regular expression to remove apostrophes that appear
    # at the beginning or end of any word, and also remove any character that
    # isn't a lowercase letter, a number, whitespace, or apostrophe. The removed
    # characters are replace by a space
    clean_sentence = re.sub(r"(?<!\w)'|'(?!\w)|[^a-z0-9\s']+", " ", lower_sentence)

    # Split the sentence on whitespace
    split_sentence = clean_sentence.split()

    # Create an empty dictionary of words
    words = {}

    # Loop through each word in the sentence
    for word in split_sentence:
        # If the current word is already in the dictionary...
        if word in words:
            # Increment that word's count by 1
            words[word] += 1

        # If it's not in the dictionary yet...
        else:
            # Add it to the dictionary with a count of 1
            words[word] = 1

    # Return the dictionary of words
    return words
