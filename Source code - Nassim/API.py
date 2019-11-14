
import requests
import json


############## This is code by Tom, https://github.coventry.ac.uk/rhaiemn/Chadbot #############
def recipeInfo(userMessage):
    '''retrieving user input to place into url'''
    userInput = userMessage
    userInput = userInput.replace(" ", "+") # in order to format the url with the message input
    print("User asked for: " + userInput + "\n")


    myUrl = "https://api.edamam.com/search?q=" + userInput + \
    "&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free"


    r = requests.get(myUrl)


    r_dict = r.json()
    r_recipe = r_dict['hits'][0]['recipe'] # I edited the json path using less variables
  


    r_ingredients = r_recipe['ingredientLines']
    r_shareUrl = r_recipe['shareAs']
    r_label = r_recipe['label']
    
    return(r_label, r_ingredients, r_shareUrl) 

##aaa######################## End of reference ################


def nutInfo(userMessage):
    # Getting UserInput
    userInput = userMessage
    userInput = userInput.replace(" ", "+") #  format the message suitable for input into the url
    print("User asked for: " + userInput + "\n")

# used Edamam documentation for the parameters to create the url including parameters of query, q, https://developer.edamam.com/edamam-docs-recipe-api
    myUrl = "https://api.edamam.com/search?q=" + userInput + \
    "&app_id=### APP ID ### &app_key=### API KEY ###&from=0&to=3&calories=400-700&health=alcohol-free"

    r = requests.get(myUrl)
# JSON FILE FOR REF https://api.edamam.com/search?q=beef&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free

    r_dict = r.json()
    r_recipe = r_dict['hits'][0]['recipe']
    
    
    
    

# nutrition key mapping
    r_label = r_recipe['label']
    r_nutrients = r_recipe['totalNutrients']
    r_shareUrl = r_recipe['shareAs']
    r_diet = r_recipe['dietLabels']
    r_calories = r_recipe['calories']
    r_health = r_recipe['healthLabels']
    r_fat = r_nutrients['FAT']['quantity']
    r_sugar = r_nutrients['SUGAR']['quantity']
    r_carb = r_nutrients['CHOCDF']['quantity']
    r_protein = r_nutrients['PROCNT']['quantity']




    return(r_label, r_diet,  r_calories, r_health, r_fat, r_sugar, r_carb, r_protein)
