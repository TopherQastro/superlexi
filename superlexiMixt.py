import csv
import string

letList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
firstCharList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

emps = csv.reader(open('/home/tqastro/skrypts/GitLib/remezclemos/eng/data/USen/empDic-USen-unik.csv', 'r+'))
namePasses = ['mark', 'hope', 'perry', 'will', 'bill', 'faith', 'tom', 'rob', 'bob', 'tanner', 'smith']
blackList = []

#  This file can be found in the "remezclemos" repository, listed under this account
#  It contains a list of practically every English word



for all in emps:
    if '(' in all[0]:  #  This takes care of words with more than one pronunciation
        pWord = all[0][:-3]
    else:  #  These are single-pronunciation words
        pWord = all[0]
    #print(pWord)
    try:
        letIndex = letList.index(pWord[0])
        firstCharList[letIndex].append(pWord)
    except ValueError:
        continue

insertedLetters = str('a')

while len(insertedLetters) < 5:  # try up to 5 letters
    for each in firstCharList:
        for all in each:
            wordI = int(0)
            allLen = len(all)
            while wordI <= allLen:
                augmentWord = all[:wordI]+insertedLetters+all[wordI:]  #  Test if the extra string will create another valid word anywhere within the test-word
                firstCharChk = letList.index(augmentWord[0])
                #print('checking list:', firstCharList[firstCharChk])
                if (augmentWord in firstCharList[firstCharChk]):# and (len(augmentWord) == (len(insertedLetters) + eachLen)):
                    print('PROPHOUND:', all, '|', insertedLetters, '|', all[:wordI]+'('+insertedLetters+')'+all[wordI:])
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
        print('insertedLetters:', insertedLetters)
        if len(insertedLetters) > 1:
            zPoint = insertedLetters.index('z')
            upPoint = zPoint - 1
            nextLet = letList.index(upPoint) + 1
            insertedLetters = insertedLetters[:upPoint]+letList[nextLet]
            while len(insertedLetters)!=oldLettersLen:
                insertedLetters+='a'
                print(insertedLetters)
        else:
            letCheck = letList.index(insertedLetters)
            insertedLetters = letList[letCheck+1]
