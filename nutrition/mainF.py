import requests
import json
import cocktailProviders



def searchByIngredient(ingredient):
    '''searchs cocktailAPI for cocktails with the argument ingredient.

    ingredient: string
    '''
    results = cocktailProviders.getCocktailByIngredient(ingredient)

    myList = ['','']
    myList[0] = results['drinks'][0]['strDrink']
    myList[1] = results['drinks'][0]['strDrinkThumb']


    return(myList)
    

def listIngredients():
    '''searchs cocktailAPI for the list of all ingredients available'''
    
    results = cocktailProviders.getIngredients()

    for i in range(len(results['drinks'])):
       print('All Ingredients: ',results['drinks'][i]['strIngredient1'],'\n')

 
def searchByName(name):
    '''searchs cocktailAPI for cocktails by the cocktail name using the argument name 
    
    name: string
    '''
    results = cocktailProviders.getCocktailByName(name)

    myList = ['', '', '', '', '', '']

    myList[0] = results['drinks'][0]['strDrink']
    myList[1] = results['drinks'][0]['strAlcoholic']
    myList[2] = results['drinks'][0]['strInstructions']
    myList[3] = results['drinks'][0]['strIngredient1']
    myList[4] = results['drinks'][0]['strIngredient2']
    myList[5] = results['drinks'][0]['strDrinkThumb']

    return myList


def randomCocktail():
    '''searchs CocktailAPI for a random cocktail'''

    results = cocktailProviders.getRandomCocktail()

    cocktail = results['drinks'][0]['strDrink']

    return cocktail

