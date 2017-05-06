from yummly import Client
import pickle

# parameters
TIMEOUT = 10.0
RETRIES = 0
API_ID = 'fill this in!'
API_KEY = 'fill this in!'

client = Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)
searchList = []
recipeID = []

total_files = 3500

for i in range(total_files):
    print(i)
    search = client.search('cookie', maxResults=40, start=i*40)
    searchList += [search]
    for match in search.matches:
        recipeID += [match.id]
    if (i+1)%10 == 0:
        pickle.dump(searchList, open('searchList_'+str(i)+'.pkl', 'wb'))
        pickle.dump(recipeID, open('recipeID_'+str(i)+'.pkl', 'wb'))
