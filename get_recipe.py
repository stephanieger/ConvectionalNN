from yummly import Client
import pickle

# parameters
TIMEOUT = 5.0
RETRIES = 0
API_ID = 'fill this in'
API_KEY = 'fill this in'

client = Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)

search = client.search('cookie', maxResults=172471)

pickle.dump(search, open('get_recipe_ID.pkl', 'wb'))

recipeID = []
for match in search.matches:
    recipeID += [match.id]

pickle.dump(recipeID, open('recipeID.pkl', 'wb'))