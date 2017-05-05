from yummly import Client
import pickle
import sys


def main():

    start = sys.argv[1]
    stop = sys.argv[2]

    # parameters
    TIMEOUT = 5.0
    RETRIES = 0
    API_ID = 'fill this in'
    API_KEY = 'fill this in'

    client = Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)

    recipeID = pickle.open('recipeID.pkl', 'rb')

    recipeInfo = []

    for i in range(start,stop):
        recipeInfo += [client.recipe(recipeID[i])]

    pickle.dump(recipeInfo, open('recipeInfo'+str(stop)+'.pkl', 'wb'))

if __name__ == '__main__':
    main()


