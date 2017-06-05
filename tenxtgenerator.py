# -*- coding: utf-8 -*-
#Copyright 2016 Aidan Draper and Brian Matejevich
#Text Generator
    
def run():
    file = input('Direct us to your file: ')
    infile = open(file, 'r')
    #create an array to hold every occurance of a word in the file
    words_list = []
    #read the file through and remove punctuation and leave a space between each word
    infile = ''.join([c for c in infile if c not in ('!', '?',',','.',';')])
    infile.split(",")
    infile = ''.join([c for c in infile if c not in ('!', '?',',','.',';')])
    #add each word to the Words array
    for word in infile.split():
        words_list.append(word) 
    #create a dictionary d
    d = {}
    x=0
    #loop through the words array adding two at a time as a key and the third as a value
    while x < len(words_list)-2:
        key = words_list[x]+ " " + words_list[x+1]
        if key in d: #if key is already in the dictionary
            d[key].append(words_list[x+2])
        else: #if it is not in the dictionary
            d[key]= [words_list[x+2]]
        x = x +1
    #start n at 2 because of the first two words (first key)
    n=2
    #catches the first word and then inserts it into the out print statement
    start=next(iter(d))
    out = start
    #splits the first two words up so that first is later dropped and second becomes the first word
    first, second = start.split()
    most_common = max(set(d[start]), key=d[start].count)
    #loops through for 500 words
    while n < 500:
        next_word = second + " " + most_common
        most_common = max(set(d[next_word]), key=d[next_word].count)
        first, second = next_word.split()
        out = out + " "+ most_common + " "
        #deletes the most common/previously used word
        del d[next_word][d[next_word].index(most_common)]
        n= n + 1
    print(out+ ".")

run()