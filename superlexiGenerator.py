import datetime
import csv
import string
import random

print(str(datetime.datetime.now())[11:], 'start')

alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
firstList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

emps = csv.reader(open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/USen/empDic-USen-unik.csv', 'r+'))
superlexiFile = csv.writer(open('/home/tqastro/projects/skrypts/GitLib/superlexi/superlexiDic.csv', 'w+'))

blackList = []  # filter proper names, single-letter words
whiteList = []  # make exceptions to some words
pureNamesFile = open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/pureNames.txt', 'r+')
twoLetters = open('/home/tqastro/projects/skrypts/GitLib/wemyx/eng/data/twoLetterWhiteList.txt', 'r+')

for line in twoLetters:
    whiteList.append(line[:-1])
    #print(line[:-1])
for line in pureNamesFile:
    blackList.append(line[:-2])
for all in alphaList:
    if (len(all) == 1) and ((all != 'a') or (all != 'i')):
        blackList.append(all)

for all in emps:
    if '(' in all[0]:  #  This takes care of words with more than one pronunciation
        pWord = all[0][:-3]
    else:  #  These are single-pronunciation words
        pWord = all[0]
    #print(pWord)

    try:
        letIndex = alphaList.index(pWord[0])
        if (pWord not in blackList) and ('.' not in pWord):
            if (len(pWord) != 2) or (pWord in whiteList):
                firstList[letIndex].append(pWord)
    except ValueError:
        continue

while len(firstList) > 0:
    while len(firstList[0]) > 0:
        pWord = firstList[0].pop(0)
        for each in firstList:
            for all in each:
                if len(all) != len(pWord):
                    if len(all) > len(pWord):
                        longword = all
                        shortword = pWord
                    elif len(all) < len(pWord):
                        longword = pWord
                        shortword = all
                    cutIndex = 0
                    shortwordLen = len(shortword)
                    while cutIndex <= shortwordLen:
                        #print('trying:', shortword, longword, shortword[:cutIndex], '|', longword[:cutIndex], '|', longword[-(shortwordLen-cutIndex):], '|', shortword[-(shortwordLen-cutIndex):])
                        if (shortword[:cutIndex] == longword[:cutIndex]) and (longword[-(shortwordLen-cutIndex):] == shortword[-(shortwordLen-cutIndex):]):
                            #print('PROPHOUND:', shortword, longword, longword[:cutIndex]+'('+longword[cutIndex:-(shortwordLen-cutIndex)]+')'+longword[-(shortwordLen-cutIndex):])
                            superlexiFile.writerow([shortword+'+'+longword, longword[:cutIndex]+'('+longword[cutIndex:-(shortwordLen-cutIndex)]+')'+longword[-(shortwordLen-cutIndex):]])
                        cutIndex+=1

    deadAlpha = alphaList.pop(0)
    print(str(datetime.datetime.now())[11:], '| firstList minus "'+deadAlpha+'"')
    firstList = firstList[1:]    
    
print(str(datetime.datetime.now())[11:], 'finished')    
