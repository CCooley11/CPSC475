def write_corpus(corpus,id):
    import nltk
    import re
    if corpus == 'brown':
        from nltk.corpus import brown
        words = brown.sents(categories=id)
    if corpus == 'gutenberg':
        from nltk.corpus import gutenberg
        words = gutenberg.sents(id)
    if corpus == 'inaugural':
        from nltk.corpus import inaugural
        words = inaugural.words(id)
		
    cleanWords = []
	
    for x in range( len(words)):
        l = re.match('\W+', words[x])
        if (l == None):
		  w = tokenize(words[x])
		  cleanWords.append(w)
		  
	#words is a list of words from each inaugural address where
    #each sentence is a list of words

    #transform the corpus to a list of words
    sentLstU = [' '.join(sent) + '\n' for sent in cleanWords]

    #this line is new
    #transform the unicode encoded list of words to ascii
    sentLst = [item.encode('ascii','ignore') for item in sentLstU]

    #transform the list of words to a string
    txt = ' '.join(cleanWords)
    
    
    
    id = id.split('.')  #eliminate the final 'txt' from some corpora
    filename = str(id[0]) + '.' + str(id[1])
   
	
    #outfile = open(filename, 'w') 
    #outfile.write(txt) 
    #outfile.close()
    #print len(words)
    #print len(cleanWords)
    return cleanWords
    
    
	
def main():
	import re
	import nltk
	corpus = nltk.corpus.inaugural.fileids()
	#print corpus[1]
	#print len(corpus)
	#print write_corpus('inaugural', '2009-Obama.txt')
	prezSpeechs = []
	for x in range (len(corpus)):
		prezSpeechs.append(write_corpus('inaugural', corpus[x]))
	return prezSpeechs	

import pickle

def tokenize(string_in):
    import re
    string = re.sub('\n',' ', string_in)
     #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ')
    string = string.lower()
    new_str = ''
    for ch in string:
        if ch in good_chars:
            new_str = new_str + ch
    return new_str
	
def pickler(listPrez):
    #lsts_out = [ [i for i in range(10)] for j in range(5)]

    #print "original list"
    #for lst in lsts_out:
    #    print lst
    
    fout = open ('pickles.pkl','wb')
    pickle.dump(listPrez,fout)

    fout.close()