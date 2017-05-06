from yummly import Client
import pickle
import sys

def main():
    '''
    This code loops through recipe IDs and uses "get recipe" to call the recipe info for each recipe. It saves the 
    recipes called periodically just in case an API call fails for some reason in order to minimize the number of wasted
    API calls. 
    :param: start - the index at which to start pulling recipe information
    :param: stop: - the index at which to stop pulling recipe information
    :return: pkl files with recipe info
    
    HOW TO RUN CODE:
    - fill in your API_ID
    - fill in you API_KEY
    - python get_ingredients.py start stop
    '''

    start = int(sys.argv[1])
    stop = int(sys.argv[2])

    # parameters
    TIMEOUT = 10.0
    RETRIES = 0
    API_ID = 'fill this in!'
    API_KEY = 'fill this in!'

    client = Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)

    recipeID = pickle.load(open('recipeID.pkl', 'rb'))

    recipeInfo = []

    for i in range(start, stop):
        print(i)
        recipeInfo += [client.recipe(recipeID[i])]
        if (i+1)%50 == 0:
            pickle.dump(recipeInfo, open('recipeInfo_'+str(i)+'.pkl', 'wb'))
            recipeInfo = []

if __name__ == '__main__':
    main()


