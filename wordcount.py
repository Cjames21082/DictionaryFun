
from sys import argv
import re


def clean_file(text_string):

	text_string = text_string.lower().replace('!', ' ').replace('?', ' ').replace(',', ' ').replace('-', ' ').replace('.'," ").replace('\n', ' ').replace(':', ' ').replace('\'', ' ').replace('\"', ' ').replace('_', ' ').replace(';', ' ')

	# Will come back to this later....
	#text_string = re.sub("[?!.,;'\n''['']''\"'*]", " ", text_string.lower())

	return text_string

def count_words(text_string):
	word_counts = {}

	words = text_string.split(' ')

	for w in words:
		if word_counts.get(w) == None:
			word_counts[w] = 1
		else:
			word_counts[w] += 1

	return word_counts

def sort_d(dictionary):

	#http://blog.client9.com/2007/11/sorting-python-dict-by-value.html
	for key, value in sorted(dictionary.iteritems(), key =lambda (k,v):(-v,k)):

		print "%s : %s" %(key, value)



script, file_name = argv

text = open(file_name)
content = text.read()
text.close()

cleaned = clean_file(content)

word_counts = count_words(cleaned)

sort_dictionary= sort_d(word_counts)


print sort_dictionary