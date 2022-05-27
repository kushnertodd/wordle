'''
wordle.py - produce possible wordle words after having guessed some words

usage:
    python wordle.py possible required exact excluded
where:
    possible  all the letters that could be in the word
              all the letters that aren't dark grey on the keyboard
    required  all the letters that must be in the word
              all the letters that are green or yellow on the keyboard
    exact     the letters that are known to be in an exact position
              the form is "ccccc" where "c" is:
                   the letter is green at that position
                   "." if the letter is yellow to grey at that position
                   so t-green r-green i-yellow a-yellow l-grey
                       is coded as "tr..."
    excluded  the letters known not to be at a position, in the form
                  lll-lll-lll--lll
requirements:
    a dictionary file must be in "dict5.txt"
'''

import sys
import re
def check_dictionary_word(dictionary_word, possible, required, exact_chars, excluded_chars):
    debug = True
    #print(f'check_dictionary_word({dictionary_word}, {possible}, {required}, {exact_chars}, {excluded_chars}')
    # check that all possible characters are in the dictionary word
    for c in dictionary_word:
        if not c in possible:
            return False
    # check that all dictionary characters are in the required letters
    for c in required:
        if not c in dictionary_word:
            return False
    # check that excluded characters are not matched
    for i in range(5):
        x = excluded_chars[i]
        c = dictionary_word[i]
        if c in x:
            #print(f'{dictionary_word} failing "{c}" at "{i}" in "{x}" of "{excluded_chars}"')
            return False
    # check that the dictionary word matches the letters in the exact position
    if re.search(exact_chars, dictionary_word):
        return True
    else:
        return False

# main program
if len(sys.argv) < 4:
    print(f'usage: python wordle.py possible must exact excluded"')
    print(f'    e.g, "python wordle.py qweriosdflcvn eosd ..s.. e--od-s-"')
    exit(0)
dict = "dict5.txt"
possible = sys.argv[1]
required = sys.argv[2]
exact_chars = sys.argv[3]
if len(exact_chars) != 5:
    print(f'exact characters must have 5 letters: "{exact_chars}"')
excluded = sys.argv[4]
excluded_chars = excluded.split("-")
if len(excluded_chars) != 5:
    print(f'excluded characters must have 5 "-"-delimitedfields: "{excluded_chars}"')
f = open(dict)
for next_line in f:
    dictionary_word = next_line.strip()  # remove newline
    if check_dictionary_word(dictionary_word, possible, required, exact_chars, excluded_chars):
        print(dictionary_word)
f.close()

