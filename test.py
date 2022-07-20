import string
from test2 import missing_number

chars = ['a', 'b', 'c', 'd', 'f']


def find_missing_letter(chars):
    if (chars[0].islower()) == True:
        alphabets = string.ascii_lowercase
        
        alphabets_list = []
        
        for i in alphabets:
            alphabets_list.append(i)
            
        #Making a  dictionary containing letters of the alphabet and thier number equivalent using enumerate to make sure the counting starts from 1 instead of 0
        alpha_count ={alphabet: index for index,alphabet in enumerate(alphabets_list, start=1)}
        
        #User input
        letter_input = chars
        
        #list of the numbers, equivalent of alphabet_input
        for i in letter_input:
            alphabet_to_number_equ = [alpha_count[i] for i in letter_input]
            
        #Missing number in alphabet_to_number_equ list
        missing_num = missing_number(alphabet_to_number_equ)
        
        #Storing the values, letters in corresponding lists
        values = list(alpha_count.values())
        letter = list(alpha_count.keys())
        
        #Finding the missing letter by matching the indexes of letter and values lists
        missing_letter = letter[values.index(missing_num)]
        
        return missing_letter
    else:
        alphabets = string.ascii_uppercase
        
        alphabets_list = []
        
        for i in alphabets:
            alphabets_list.append(i)
            
        #Making a  dictionary containing letters of the alphabet and thier number equivalent using enumerate to make sure the counting starts from 1 instead of 0
        alpha_count ={alphabet: index for index,alphabet in enumerate(alphabets_list, start=1)}
        
        #User input
        letter_input = chars
        
        #list of the numbers, equivalent of alphabet_input
        for i in letter_input:
            alphabet_to_number_equ = [alpha_count[i] for i in letter_input]
            
        #Missing number in alphabet_to_number_equ list
        missing_num = missing_number(alphabet_to_number_equ)
        
        #Storing the values, letters in corresponding lists
        values = list(alpha_count.values())
        letter = list(alpha_count.keys())
        
        #Finding the missing letter by matching the indexes of letter and values lists
        missing_letter = letter[values.index(missing_num)]
        
        return missing_letter
