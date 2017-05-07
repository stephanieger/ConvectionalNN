import pickle

# file names
file_num = range(99, 10099, 100)
ingredientLines = []

for i in file_num:
    print(i)
    file = pickle.load(open('./pkl_recipe_info/recipeInfo_'+str(i)+'.pkl', 'rb'))
    for recipe in file:
        ingredientLines += [recipe['ingredientLines']]

pickle.dump(ingredientLines, open('ingredientLines_15k.pkl', 'wb'))
