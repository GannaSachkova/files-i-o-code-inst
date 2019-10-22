import re
import collections

# Here we'll read everything into a string called text use the read() method and in lowercase
text = open('book.txt').read().lower()

#  regular expressions + findall() method is used to pass that string and find words by pattern (w denotes anything that's not a whitespace, and the plus denotes one or more) + our text string. 
words = re.findall('\w+', text)

# Finally, we're going to use the counter() method from our collections, and we're also going to find the ten most common words
# the counter() method from collections counts how many occurrences there are and the most_common() method limits the results to ten words. 
# We see that we have then a list of tuples, where each tuple contains  the word and the number of occurrences
# output:  [('the', 83), ('and', 53), ('a', 33), ('he', 32), ('of', 31), ('to', 26), ('had', 19), ('was', 18), ('it', 16), ('his', 16)]
print(collections.Counter(words).most_common(10))

