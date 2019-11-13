import requests
import json

headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "AddYourKey"
}

def httpRequest(pathname, params=()):
    url = "https://the-cocktail-db.p.rapidapi.com" + pathname
    response = requests.request("GET", url, headers=headers, params=params)

    return json.loads(response.text)

def getRandomCocktail():
    return httpRequest('/random.php')

def getIngredients():
    params = {"i": 'list'}
    return httpRequest('/list.php?i=list', params=params)

def getCocktailByIngredient(ingredient):
    params = {"i":ingredient}
    return httpRequest('/filter.php',params=params)

def getCocktailByName(name):
    params = {"s":name}
    return httpRequest('/search.php',params=params)

