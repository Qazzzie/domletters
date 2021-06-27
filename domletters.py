#!/usr/bin/python3
"""
    Zach Santangelo
    CS461P HW1
"""
import sys
import os.path

def is_valid_word(word):
    for letter in word:
        print(word) 
        if(letter.isalpha() == False):
            return False
       
    return True


def count_dom_letters(sentence):
    alphabet=[]
    for i in range(97,123):
        alphabet.append(chr(i))
    #print(alphabet)

    dom_letters_total = 0

    for word in sentence:
                #print("\n" + word + "\n")
        dom_letter_count_in_word = 0
        if(is_valid_word(word)):
            for char in alphabet:     
                char_counts = 0        #for each character in the alphabetbet, check how many times it appears. 
                for letter in word:
                    if(letter.lower() == char):
                        char_counts += 1
                    if(char_counts > dom_letter_count_in_word):
                        dom_letter_count_in_word = char_counts
        
        dom_letters_total += dom_letter_count_in_word

    print("Total dom letters: " + str(dom_letters_total))
        


if __name__ == "__main__": #to Call in CLI: $ ./domletters.py sentence.txt 
    #process file passed in as argument
    file = str(sys.argv[1])
    print(file)

    with open(file) as path: #https://pythonspot.com/read-file/
        sentence = path.read()

    words = sentence.split()
    print(words)

    count_dom_letters(words)