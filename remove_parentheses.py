import re

# use the output from ingredients_to_txt.py
ingredient_list = open('ingredients.txt', 'r')

# removes any phrases enclosed in either () or []
with open('ingredients_noparentheses.txt', 'w') as f:
    for line in ingredient_list.readlines():
        new_line = re.sub("[\(\[].*?[\)\]]", "", line)
        f.write(new_line)