# 3.1 Octopus's Garden
from operator import itemgetter

def is_stop_word(word):
    stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}
    return word in stop_words

# Read in the lyrics
with open('lyrics.txt') as file:
    contents = file.read()

# fix data issues
contents = contents.replace('(', '').replace(')', '').replace(',', '')

# convert contents into a list of words
words = contents.split()

# Using a dictionary, count how many times the words that are NOT stop words appear
word_dict = {}
for word in words:
    word = word.strip().lower()
    if not is_stop_word(word):
        word_dict[word] = word_dict.get(word, 0)+ 1

# The print out how many times "octopus's", "sea" and "happy" appear
print('This many octopi: ' + str(word_dict.get("octopus's", 0)))
print('In this many seas: ' + str(word_dict.get("sea", 0)))
print('Is happy this many times: ' + str(word_dict.get("happy", 0)))

# And find the most used word(s)
word_list = sorted(word_dict.items(), key=itemgetter(1), reverse = True)
print("The most common words: " + word_list[0][0] +"and "+ word_list[1][0])
