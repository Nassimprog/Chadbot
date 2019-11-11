import requests  # <<<<< Module use was inspired from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"


def foodRecipe(userMessage):

    ########## Editing User Message for url link ############

    # Change the list input into a string
    userInput = ''
    for i in userMessage:
            userInput += i
            userInput += ' '
    userInput = userInput.replace(' ', '+')

    # Display users request.
    print("User asked for: " + userInput + "\n")

    # Set the URL
    # <<<<< Link structure obtained and modified from Edamam API documentation: "https://developer.edamam.com/edamam-docs-recipe-api"
    myUrl = "https://api.edamam.com/search?q=" + userInput + \
        "&app_id=$55554362&app_key=$65a9ee67bc50f65260eeb2b7b0705164&from=0&to=3&calories=591-722&health=alcohol-free"

    ########## Getting info #########

    # Access url data.
    # <<<<< Line inspired and modified from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"
    r = requests.get(myUrl)

    # Access/request the part you need.
    # <<<<< Accesing of json data inspiered from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"
    r_dict = r.json()
    r_hits = r_dict['hits']
    r_recipe = r_hits[0]['recipe']

    # Ingredients
    r_ingredients = r_recipe['ingredientLines']
    r_shareUrl = r_recipe['shareAs']
    r_label = r_recipe['label']

    return[r_label, r_ingredients, r_shareUrl]

# Nassim's Nutrition implementation.
def nutInfo(userMessage):

    # Getting UserInput
    userInput = userMessage

    # format the url with the message input
    userInput = userInput.replace(" ", "+")

    print("User asked for: " + userInput + "\n")

    myUrl = "https://api.edamam.com/search?q=" + userInput + \
        "&app_id=$8ff5b715&app_key=$7c743310345e454a3eb2765cc24a1c6b&from=0&to=3&calories=591-722&health=alcohol-free"

    r = requests.get(myUrl)

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
    r_protein = r_nutrients['PROCNT']['quantity']

    # Ruturning data that is later put into List.
    return(r_diet,  r_calories, r_health, r_fat, r_sugar, r_carb, r_protein)

