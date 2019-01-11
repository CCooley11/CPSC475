'''
pre: count_dict is the dictionary created in the function freq_table
post: writes the the key/value pairs of count_dict to a file
'''
def display_freq(count_dict,fout):
    word_lst = list(count_dict.keys())
    word_lst.sort()
    fout.write("CHARACTER  FREQUENCY\n")
    for word in word_lst:
        fout.write(word + '\t\t' + str(count_dict[word]) + '\n')

def depickler():
    
    fin = open('pickles.pkl', 'rb')
    lsts_in = pickle.load(fin)

    print "pickled list"
    for lst in lsts_in:
        print lst

    fin.close()	
	
listPrez = main()
pickler(listPrez)	
depickler()
#write_corpus('inaugural', '2009-Obama.txt')

'''
pre: string_in is a string
post: returns a dictionary where the key is an element of string_in and the
    value is the number of times it appears in string_in
'''
def freq_table(string_in):
    count_dict = {}
    word_lst = string_in.split()
    for word in word_lst:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return count_dict
	
	
def main():
    fin, fout = my_open()
    contents = fin.read()
    count_dict = freq_table(contents)
    display_freq(count_dict, fout)
    
    fin.close()
    fout.close()
    
    
main()