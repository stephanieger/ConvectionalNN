import pickle
import re
from random import sample

'''
This script writes from the ingredient te
'''

# build dictionary
fractions = {
    u'\xbc': ' 1/4',
    u'\xbd': ' 1/2',
    u'\xbe': ' 3/4',
    u'\u2153': ' 1/3',
    u'\u2154': ' 2/3',
    u'\u2155': ' 1/5',
    u'\u2156': ' 2/5',
    u'\u2157': ' 3/5',
    u'\u2158': ' 4/5',
    u'\u2159': ' 1/6',
    u'\u215a': ' 5/6',
    u'\u215b': ' 1/8',
    u'\u215c': ' 3/8',
    u'\u215d': ' 5/8',
    u'\u215e': ' 7/8'
}

# use this to determine which words to remove from the ingredient list
remove = open("remove.txt","r").read().splitlines()

# change this to whatever you called the output file from process_ingredients
ing = pickle.load(open('ingredientLines_15k.pkl', 'rb'))
nam = pickle.load(open('recipeName_15k.pkl', 'rb'))

# number of synthetic files to create for each file
num_syn = 2

# process each item to get rid of non-ascii characters
proc = []
for i in range(len(ing)):
    tmp = [re.sub("[,]", "", ing[i][j]) for j in range(len(ing[i]))]
    proc += [tmp]

    # use sample to shuffle ingredient lists to resample data and try to avoid dependencies on order of ingredients
    for j in range(num_syn):
        proc += [sample(tmp, len(tmp))]

# remove special characters from the ingredients
for i in range(len(proc)):
    tmp = ','.join(word for word in proc[i] if word not in remove)
    for key in fractions.iterkeys():
        tmp = tmp.replace(key, fractions[key])
    tmp = tmp.encode('ascii', 'ignore')
    tmp = re.sub("[\{\(\[].*?[\)\]\}]", "", tmp)
    tmp = re.sub("[~$&|!]", "", tmp)
    tmp = re.sub("[*]", "", tmp)

    proc[i] = tmp

full_proc = []

for i in range(len(ing)):

    for j in range(num_syn+1):

        tmp = nam[i].encode('ascii', 'ignore')
        tmp = re.sub("[\{\(\[].*?[\)\]\}]", "", tmp)
        tmp = re.sub("[~$&|!,]", "", tmp)
        full_proc += ['['+ tmp +'] \t '+proc[(num_syn+1)*i+j]]

# change this to reflect what chunk of the data you have
with open('ingredients_15k.txt', 'w') as f:
    for line in full_proc:
        print(line)
        f.write(line+'\n')



