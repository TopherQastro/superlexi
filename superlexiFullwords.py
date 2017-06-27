import csv

emps = csv.reader(open('~/remezclemos/eng/data/USen/empDic-USen-unik.csv', 'r+'))
#  This file can be found in the "remezclemos" repository, listed under this account
#  It contains a list of practically every English word

words = []
qWords = []

words = []
for all in emps:
    if '(' in all[0]:  #  This takes care of words with more than one pronunciation
        words.append(all[0][:-3])
    else:  #  These are single-pronunciation words
        words.append(all[0])

print('words:', len(words))

for each in words:
    for all in words:
        if (len(each) > 3) and (each in all) and (len(each) != len(all)):
            wordI = all.index(each)
            print(each, all+'\n'+all[:wordI]+'('+each+')'+all[wordI+len(each):])
