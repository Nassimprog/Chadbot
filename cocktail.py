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
    for i in range(len(results['drinks'])):
       print('Cocktails: ',results['drinks'][i]['strDrink'],'\n')
            
        
          
         


def listIngredients():
    '''searchs cocktailAPI for the list of all ingredients available'''
    
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php?i=list'
    querystring = {"i":'list'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    for i in range(len(results['drinks'])):
       print('All Ingredients: ',results['drinks'][i]['strIngredient1'],'\n')
     
       
      
       

def searchByName(name):
    '''searchs cocktailAPI for cocktails by the cocktail name using the argument name 
    
    name: string
    '''
    
    url = "https://the-cocktail-db.p.rapidapi.com/search.php"
    querystring = {"s":name}
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    for i in range(len(results["drinks"])):
        print("Name: ",results['drinks'][i]['strDrink'],'\n')
    for i in range(len(results["drinks"])):
        print("filter: ",results['drinks'][i]['strAlcoholic'],'\n')
    for a in range(len(results['drinks'])):
        print('Instructions: ',results['drinks'][a]['strInstructions'],'\n')
    for u in range(len(results['drinks'])):
        print('Ingredients: ','\n')
        print(results['drinks'][u]['strIngredient1'])  
        print(results['drinks'][u]['strIngredient2'])
        print(results['drinks'][u]['strIngredient3']) 
        print(results['drinks'][u]['strIngredient4']) 
        print(results['drinks'][u]['strIngredient5'])
        print(results['drinks'][u]['strIngredient6'])
        print(results['drinks'][u]['strIngredient7'])
        print(results['drinks'][u]['strIngredient8'])
        print(results['drinks'][u]['strIngredient9'])
    for o in range(len(results['drinks'])):
        print('image: ',results['drinks'][o]['strDrinkThumb'],'\n')    


def randomCocktail():
    '''searchs CocktailAPI for a random cocktail'''
    
    url = "https://the-cocktail-db.p.rapidapi.com/random.php"
    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.text)
    for p in range(len(results['drinks'])):
        print('name: ',results['drinks'][p]['strDrink'],'\n')
    for i in range(len(results["drinks"])):
        print("filter: ",results['drinks'][i]['strAlcoholic'],'\n')
    for a in range(len(results['drinks'])):
        print('Instructions: ',results['drinks'][a]['strInstructions'],'\n')
    for u in range(len(results['drinks'])):
        print('Ingredients: ','\n')
        print(results['drinks'][u]['strIngredient1'])  
        print(results['drinks'][u]['strIngredient2'])
        print(results['drinks'][u]['strIngredient3']) 
        print(results['drinks'][u]['strIngredient4']) 
        print(results['drinks'][u]['strIngredient5'])
        print(results['drinks'][u]['strIngredient6'])
        print(results['drinks'][u]['strIngredient7'])
        print(results['drinks'][u]['strIngredient8'])
        print(results['drinks'][u]['strIngredient9'])
    for o in range(len(results['drinks'])):
        print('image: ',results['drinks'][o]['strDrinkThumb'],'\n' )    
randomCocktail()      

    



