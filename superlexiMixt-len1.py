import csv
import string

letList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
firstCharList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

input('press enter to continue')

#  This file can be found in the "remezclemos" repository, listed under this account
#  It contains a list of practically every English word
emps = csv.reader(open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/USen/empDic-USen-unik.csv', 'r+'))


blackList = []  # filter proper names, single-letter words
whiteList = []  # make exceptions to some words
pureNamesFile = open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/pureNames.txt', 'r+')
twoLetters = open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/twoLetterWhiteList.txt', 'r+')

for line in twoLetters:
    whiteList.append(line[:-1])
    print(line[:-1])
for line in pureNamesFile:
    blackList.append(line[:-2])
for all in letList:
    if (len(all) == 1) and ((all != 'a') or (all != 'i')):
        blackList.append(all)

for all in emps:
    if '(' in all[0]:  #  This takes care of words with more than one pronunciation
        pWord = all[0][:-3]
    else:  #  These are single-pronunciation words
        pWord = all[0]
    #print(pWord)
    try:
        letIndex = letList.index(pWord[0])
        if (pWord not in blackList) and ('.' not in pWord):
            if (len(pWord) != 2) or (pWord in whiteList):
                firstCharList[letIndex].append(pWord)
    except ValueError:
        continue

insertedLetters = str('a')
print('insertedLetters:', insertedLetters)
while len(insertedLetters) == 1:  # try up to 5 letters
    for each in firstCharList:
        for all in each:
            wordI = int(0)
            allLen = len(all)
            while wordI <= allLen:
                augmentWord = all[:wordI]+insertedLetters+all[wordI:]  #  Test if the extra string will create another valid word anywhere within the test-word
                firstCharChk = letList.index(augmentWord[0])
                #print('checking list:', firstCharList[firstCharChk])
                if (augmentWord in firstCharList[firstCharChk]):# and (len(augmentWord) == (len(insertedLetters) + eachLen)):
                    superlexiDic[all+'+'+augmentWord] = all[:wordI]+'('+insertedLetters+')'+all[wordI:]
                    print(all+'+'+insertedLetters+'='+augmentWord, all[:wordI]+'('+insertedLetters+')'+all[wordI:])
                wordI+=1
    oldLettersLen = len(insertedLetters)
    zCt = insertedLetters.count('z')
    if zCt == oldLettersLen:
        # after all letters hit 'z', augment string by one, all of them "a"
        insertedLetters = ''
        while len(insertedLetters) < oldLettersLen:
            insertedLetters+='a'
        insertedLetters+='a'
    else:  #  advance a letter earlier in the string by 1, then convert everything to the right to "a"
        if insertedLetters[-1] != 'z':
            letCheck = letList.index(insertedLetters[-1])
            insertedLetters = insertedLetters[:-1]+letList[letCheck+1]
        else:
            zPoints = oldLettersLen - 1
            while insertedLetters[zPoints] == 'z':
                zPoints-=1
            letCheck = letList.index(insertedLetters[zPoints])  # This letter is no longer 'z'
            insertedLetters = insertedLetters[:zPoints]+letList[letCheck+1]
            while len(insertedLetters)!=oldLettersLen:
                insertedLetters+='a'
    print('insertedLetters:', insertedLetters)

print(len(superlexiDic))
input('press enter to write to file')

superlexiFile = csv.writer(open('/home/tqastro/projects/skrypts/GitLib/superlexi/superlexiDic.csv', 'w+'))
for key, val in superlexiDic.items():
    superlexiFile.writerow([key, val])
    
