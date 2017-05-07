import pickle

# change this to whatever you called the output file from process_ingredients
ing = pickle.load(open('ingredientLines_15k.pkl','rb'))

proc = []
for i in range(len(ing)):
    proc += [[ing[i][j].encode('ascii', 'ignore') for j in range(len(ing[i]))]]

for i in range(len(proc)):
    proc[i] = ','.join(proc[i])

# change this to reflect what chunk of the data you have
with open('ingredients_15k.txt', 'w') as f:
    for line in proc:
        f.write(line+'\n')


