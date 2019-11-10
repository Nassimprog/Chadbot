
import requests
import json



def recipeInfo(userMessage):
    '''retrieving user input to place into url'''
    userInput = userMessage
    userInput = userInput.replace(" ", "+") # in order to format the url with the message input
    print("User asked for: " + userInput + "\n")


    myUrl = "https://api.edamam.com/search?q=" + userInput + \
    "&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free"


    r = requests.get(myUrl)


    r_dict = r.json()
    r_hits = r_dict['hits']
    r_recipe = r_hits[0]['recipe']


    r_ingredients = r_recipe['ingredientLines']
    r_shareUrl = r_recipe['shareAs']
    r_label = r_recipe['label']
    
    

#  print URL + Label + nutrition
    
    print(r_label + "\n")
    print(r_shareUrl + "\n")
    return( r_label, r_ingredients, r_shareUrl)




def nutInfo(userMessage):
    # Getting UserInput
    userInput = userMessage
    userInput = userInput.replace(" ", "+") #  format the url with the message input
    print("User asked for: " + userInput + "\n")


    myUrl = "https://api.edamam.com/search?q=" + userInput + \
    "&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free"

    r = requests.get(myUrl)
# JSON FILE FOR REF https://api.edamam.com/search?q=beef&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free
# Access/request the part you need.
    r_dict = r.json()
    r_hits = r_dict['hits']
    
    r_recipe = r_hits[0]['recipe']
    r_label = r_recipe['label']
    r_nutrients = r_recipe['totalNutrients']
    

# nutrition key mapping
    r_shareUrl = r_recipe['shareAs']
    r_diet = r_recipe['dietLabels']
    r_calories = r_recipe['calories']
    r_health = r_recipe['healthLabels']
    r_fat = r_nutrients['FAT']['quantity']
    r_sugar = r_nutrients['SUGAR']['quantity']
    r_carb = r_nutrients['CHOCDF']['quantity']
    r_fibre = r_nutrients['FIBTG']['quantity']
    r_protein = r_nutrients['PROCNT']['quantity']



# print Label + URL
    print(r_label + "\n")
    print(str(r_diet) + "\n"  )
    print('calories: ' + str(r_calories) + " kcal" + "\n")
    print('This recipe is: ' + str(r_health) + "\n")
    print('This recipe has: ' + str(r_fat) + " grams of fat" +"\n")
    print('This recipe has: ' + str(r_sugar) + " grams of sugar" +"\n")
    print('This recipe has: ' + str(r_carb) + " grams of carb" +"\n")
    print('This recipe has: ' + str(r_protein) + " grams of protein" +"\n")
    return(r_label, r_diet,  r_calories, r_health, r_fat, r_sugar, r_carb, r_protein)
