import pickle

'''
This code takes the pickle files produced by the get_recipe output code to extract the ingredient lines'
'''
# file names
'''
change this to however many files you have. eg if you have 15k to 40k youd want to change it to range(15099, 45099,100)
'''
file_num = range(99, 15099, 100)
ingredientLines = []
recipeName = []
notCookie = []

for i in file_num:
    'change the file location to wherever you stored the recipeInfo files'
    file = pickle.load(open('./pkl_recipe_info/recipeInfo_'+str(i)+'.pkl', 'rb'))
    for recipe in file:
        if recipe['name'].lower().find('cookie') != -1:
            ingredientLines += [recipe['ingredientLines']]
            recipeName += [recipe['name']]
        else:
            notCookie += [recipe['name']]

# change the name of the pickle file you want to save to in order to reflect the range of items you have
pickle.dump(ingredientLines, open('ingredientLines_15k.pkl', 'wb'))
pickle.dump(recipeName, open('recipeName_15k.pkl', 'wb'))
pickle.dump(notCookie, open('notCookie.pkl', 'wb'))