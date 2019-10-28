import requests
import json
import cocktailProvider

def searchByIngredient(ingredient):
    '''searchs cocktailAPI for cocktails with the argument ingredient.

    ingredient: string
    '''
    results = cocktailProvider.getCocktailByIngredient(ingredient)
    for i in range(len(results['drinks'])):
       print('Cocktails: ',results['drinks'][i]['strDrink'],'\n')
  

def listIngredients():
    '''searchs cocktailAPI for the list of all ingredients available'''
    
    results = cocktailProvider.getIngredients()

    for i in range(len(results['drinks'])):
       print('All Ingredients: ',results['drinks'][i]['strIngredient1'],'\n')

 
def searchByName(name):
    '''searchs cocktailAPI for cocktails by the cocktail name using the argument name 
    
    name: string
    '''
    results = cocktailProvider.getCocktailByName(name)
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
    
    results = cocktailProvider.getRandomCocktail()

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
        print('image: ',results['drinks'][o]['strDrinkThumb'],'\n')    
    
    

