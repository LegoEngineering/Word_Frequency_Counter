from collections import Counter
from itertools import combinations, islice, izip
import string
import ast
import re


file_data = open("text.txt", "r") #open the files
file = file_data.read() #convert the file to a string
result = open("result.csv","w") #generate a results file in .csv

def wordcount(file):
    word_count = Counter(file.lower().translate(None, string.punctuation).split()) #separate words at every space, eliminate special characters, change the string to lowercase
    total = 0
    for word, count in word_count.most_common(): #count the occurrances of a word and sort into most common       
          total = total + count 
    for word, count in word_count.most_common(): 
    	result.write("%s, %d, %0.2f \n" % (word , count, float(count)/total)) #write frequencies and word counts into results file
    print ("Word Count: %d" % total)


def sentencecount(file):
    num_sentences = file.count('.') + file.count('?') + file.count('!') #A sentence, regardless of whether it is nested, is counted if it has one of these three sentence-ending punctuation marks.
    print('Sentence Count: %d' % num_sentences)


def the_sentencecount(file):
    raw_content = file.lower().replace('"', '') #reduce the content to it's rawest ASCII form
    num_sentences = raw_content.count('.') + raw_content.count('?') + raw_content.count('!') #count occurances of sentence-ending punctuation
    the_count = raw_content.count('. the') + raw_content.count('? the') + raw_content.count('! the') #count the number of times "the" follows the end of a sentence
    print ("Sentences starting with 'the': %d, %0.2f" % (the_count, float(the_count)/num_sentences))


def bigramcount(file):
	bigram = re.findall('\w+', file) #find all words
	print(Counter(zip(bigram,bigram[1:])).most_common()) #count the number of times two words follow one another, sort by frequency

wordcount(file) #run each program
sentencecount(file)
the_sentencecount(file)
bigramcount(file)

file_data.close() #close the files
result.close()
