import numpy as np
import sys

def main():

    # this function uses the keyword (a recipe title) and uses it to seed the sampling program when
    # using the program to generate recipes
    keyword = sys.argv[1]
    input_file = sys.argv[2] # training data

    with open(input_file) as f:
        data = f.read()

    recipe_lines = data.split('\n') # split on recipes so we can search each recipe title for the keyword

    del data # free up some memory

    idx = []
    for i in range(len(recipe_lines)):
        if recipe_lines[i].split('\t')[0].lower().find(keyword) != -1:
            idx += [i]

    # what happens next depends on if we found the keyword or not

    if len(idx) != 0:
        # of all the recipes that have this keyword, use np.random.choice to choose one at random
        seed = recipe_lines[np.random.choice(idx, 1)[0]].split('\t')[1]
    else:
        # if that key word does not exist, then return a random seed
        print('Recipe does not exist in training data')
        seed = recipe_lines[np.random.choice(len(recipe_lines), 1)[0]].split('\t')[1]

    with open('seed.txt', 'w') as f:
        f.write(seed)

    return

if __name__ == '__main__':
    main()






