'''
Aug 31
Nic Nguyen
NicolasProject1.py
This program takes a text file and print out its unique words. Then it prompts the user to enter a word
of their choice and subsequently check if that word is in the text or not. 
'''
#Splitting into sentences and removing whitespace
def splitAndstrip(text):
	'''
	This function splits text into sentences and strip the leading and trailing whitespace from 
	each one 
    PARAMETERS:
        text = a text string 
    RETURN VALUE
        sentences = a list of sentences in the text 
	'''
	sentenceList = text.split(".")
	sentences = []
	for x in sentenceList: 
		x = x.strip()
		sentences.append(x)
	return sentences

#Building a dictionary in the format {word:[n]}, where word represents a word in the text, while n represents the position of the sentences in the text
def uniqueWords(dictionary, wordList, index):
	'''
	This function 
    PARAMETERS:
        dictionary = a dictionary 
		wordList = list of words in a sentence 
		index = setence number in the text
    RETURN VALUE
        dictionary = a dictionary 
	'''
	for word in wordList: 
		if word not in dictionary.keys():
			dictionary[word] = [index] 
		elif word in dictionary.keys(): 
			dictionary[word].append(index) 
	return dictionary  

#Main fucntion 			
def main(): 
	#Opening and reading text file 
	fileHandle = open('input.txt','r') 
	text_file = fileHandle.read()  
	fileHandle.close()  
	
	#Calling splitAndstrip function 
	sentences = splitAndstrip(text_file)

	#Creating a dictionary to store words and their appearances in the text
	wordAppearance = {} 
	for i in range(len(sentences)): 
		low_sentences = sentences[i].lower() 
		wordList = low_sentences.split() 
		wordAppearance = uniqueWords(wordAppearance, wordList, i)
	keys = list(wordAppearance.keys())
	keys.sort()			#Sorting keys alphabetically 
	print("List of words in the text:")
	for key in keys: 
		print(key)
		

	#Prompting a user for input 
	wordSearch = input("Enter a word: ")
	print(wordSearch + " appears in:")

	#Check if the word is in the text and subsequently print the sentences it appears in 
	if wordSearch in wordAppearance.keys():
		for sentenceNumber in wordAppearance[wordSearch]:
			print("\t"+ str(sentenceNumber+1) + " " + sentences[sentenceNumber])
	else: 
		print("\t" + "Sorry, this word is not found in the text!")

#Main function call 
if __name__ == '__main__':
	main() 
