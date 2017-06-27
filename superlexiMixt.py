import csv
import string

emps = csv.reader(open('~/remezclemos/eng/data/USen/empDic-USen-unik.csv', 'r+'))
#  This file can be found in the "remezclemos" repository, listed under this account
#  It contains a list of practically every English word

words = []
for all in emps:
    if '(' in all[0]:  #  This takes care of words with more than one pronunciation
        words.append(all[0][:-3])
    else:  #  These are single-pronunciation words
        words.append(all[0])

insertedLetters = chr(96)  #  This is the char number before 'a', given that we start the loop by adding 1 to this number

while len(insertedLetters) < 5:  # try up to 5 letters
    while insertedLetters[-1] != chr(123):  #  'z' is 122
        insertedLetters = insertedLetters[:-1]+chr(ord(insertedLetters[-1])+1)

        for each in words:
            wordI = int(0)
            eachLen = len(each)
            while wordI <= eachLen:
                augmentWord = each[:wordI]+insertedLetters+each[wordI:]  #  Test if the extra string will create another valid word anywhere within the test-word
                if (augmentWord in words):# and (len(augmentWord) == (len(insertedLetters) + eachLen)):
                    print('PROPHOUND:', each, '|', insertedLetters, '|', each[:wordI]+'('+insertedLetters+')'+each[wordI:])
                wordI+=1
                
        if insertedLetters[-1] == 'z':
            break
    oldLettersLen = len(insertedLetters)
    if insertedLetters[0] == 'z':        
        # after all letters hit 'z', augment string by one, all of them "a"
        oldLettersLen = len(insertedLetters)
        insertedLetters = ''
        while len(insertedLetters) < oldLettersLen:
            insertedLetters+='a'
        insertedLetters+='a'
    else:  #  advance a letter earlier in the string by 1, then convert everything to the right to "a" 
        zPoint = insertedLetters.index('z')
        insertedLetters = insertedLetters[:zPoint-1]+chr(ord(insertedLetters[zPoint-1])+1)
        while len(insertedLetters)!=oldLettersLen:
            insertedLetters+='a'
            print(insertedLetters)
    
        
