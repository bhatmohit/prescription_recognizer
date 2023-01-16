import pandas

import nltk
print('NTLK version: %s' % (nltk.__version__))

from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

'''

#spacy
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from pprint import pprint
nlp = en_core_web_sm.load()


doc = nlp(line)
	pprint([(X.text, X.label_, X.pos_) for X in doc.ents])
'''

import nltk
from nltk.tag.stanford import StanfordNERTagger

'''sentence = u"Twenty miles east of Reno, Nev., " \
    "where packs of wild mustangs roam free through " \
    "the parched landscape, Tesla Gigafactory 1 " \
    "sprawls near Interstate 80."'''

jar = './stanford-ner-2018-10-16/stanford-ner.jar'
model = './stanford-ner-2018-10-16/mp.ser.gz'

# Prepare NER tagger with english model
ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

# Tokenize: Split sentence into words


# Run NER tagger on words

mystr = []
mystr2 = []
mystr3 = []
mystr4 = []
mystr5 = []
mystr6 = []
mystr7 = []
mystrd = []


filePath = "myfilename.txt"
file1 = open("mpformat.tex","a") 
wordList = []
mylist = [[]]
wordCount = 0

file = open(filePath, 'rU')

for line in file:
	myl = []	
	words = nltk.word_tokenize(line)
	for i in words:
			
		word = preprocess(i)
		print(word[0][0])
		print(word)
		if 'NN' in word[0][1] or 'VB' in word[0][1]:
			myl.append(word[0][0])
		elif 'CD' in word[0][1]:
			mystrd.append(word[0][0])

		
	#print(ner_tagger.tag(myl))
	wordList = ner_tagger.tag(myl)
	print(wordList)
	mylist.append(wordList)
	#results = ne_chunk(sent)
	#print(results)
	

for item1 in mylist:
	print(item1)
	for item in item1:
		if item[1] == 'MEDICINE':
				mystr.append(item[0])
		elif item[1] == 'NAME':
				mystr2.append(item[0])
		elif item[1] == 'DOSAGE':
				mystr3.append(item[0])
		elif item[1] == 'PROCEDURE':
				mystr4.append(item[0])
		elif item[1] == 'DIAGNOSIS':
				mystr5.append(item[0])
		elif item[1] == 'HABITS':
				mystr6.append(item[0])
		elif item[1] == 'VITALS':
				mystr7.append(item[0])


print("\n\n\n\n\nFINAL OUTPUT:\n\n")
print("MEDICINES:\n")
print(mystr)
print("\n")
print("NAMES:\n")
print(mystr2)
print("\n")
print("DOSAGE:\n")
print(mystr3)
print("\n")
print("PROCEDURE:\n")
print(mystr4)
print("\n")
print("DIAGNOSIS:\n")
print(mystr5)
print("\n")
print("HABITS:\n")
print(mystr6)
print("\n")
print("VITALS:\n")
print(mystr7)
print("\n")
print("NUMBERS:\n")
print(mystrd)
print("\n")


file1.write("\n\\"+"title\\Large\\bf{" + mystr2[0] + "}\n" )	

file1.write("\\section{MEDICINES}\n")
for i in range(0,len(mystr)):
	file1.write(str(mystr[i]))
	if i < len(mystrd):
		file1.write("\\begin{flushright}"+ str(mystrd[i]) +"\\end{flushright}")

file1.write("\n\\section{PROCEDURES}\n")
for i in range(0,len(mystr4)):
	file1.write(str(mystr4[i])+ "\n")


file1.write("\\end{document}")
file1.close() 


        
