
#List1 = open('dic.txt').read().splitlines()
#print(List1)
#
##%%
#
#List2 = open('all.txt').read().splitlines()
#print(List2)
#
##%%
#with open('remove.txt', 'w') as f:
#    List3 = [x for x in List2 if x not in List1]
#    for i in List3:
#        f.write("%s\n" %i)
##%%
#import re
#
#ingredient_list = open("ingredients.txt", 'r')
#
#with open('clean.txt', 'w') as f:
#    for line in ingredient_list.readlines():
#        new_line = re.sub("[~$&|!{}[]()]", "", line)
#        f.write(new_line)
#        

#%%

remove=open("remove.txt","r").read().splitlines()
ingredient_list2 = open("clean.txt", 'r')


with open('clean2.txt', 'w') as f:
    for line in ingredient_list2.readlines():
        text = ' '.join([word for word in line.split() if word not in remove])
        f.write("%s\n" %text)
