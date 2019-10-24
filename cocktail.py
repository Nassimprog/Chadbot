import requests
import json

url = "https://the-cocktail-db.p.rapidapi.com/filter.php"




headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "540add6831msh2be37097a5ac45ap187522jsn439eee457bc9"
    }




def searchByIngredient(ingredient):
    '''searchs cocktailAPI for cocktails with the argument ingredient.

    ingredient: string
    '''
    querystring = {"i":ingredient}
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    for i in range(len(results["drinks"])):
        print(results['drinks'][i]['strDrink'])
         


def listIngredients():
    '''searchs cocktailAPI for the list of all ingredients available'''
    
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php?i=list'
    querystring = {"i":'list'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    for i in range(len(results['drinks'])):
       print(results['drinks'][i]['strIngredient1'])
      
       

def searchByName(name):
    '''searchs cocktailAPI for cocktails by the cocktail name using the argument name 
    
    name: string
    '''
    
    url = "https://the-cocktail-db.p.rapidapi.com/search.php"
    querystring = {"s":name}
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    for i in range(len(results["drinks"])):
       print(results['drinks'][i]['strDrink'])

