import re
import sys

# use the output from ingredients_to_txt.py
ingredient_list = open(sys.argv[1], 'r')

# removes any phrases enclosed in either () or []
with open('ingredients_noparentheses.txt', 'w') as f:
    for line in ingredient_list.readlines():
        new_line = re.sub("[\{\(\[].*?[\)\]\}]", "", line)
        new_line = re.sub("[~$&|!]", "", new_line)
        f.write(new_line)