import requests


def foodRecipe(userMessage):

    ########## Editing User Message for url link ############

    # Change the list input into a string
    userInput = ''
    for i in userMessage:
            userInput += i
            userInput += ' '
    userInput = userInput.replace(' ', '+')

    # Check if the First Letter is '+' and exclude it.
    if userInput[0] == '+':
        userInput = userInput[1:len(userInput)]

    # Check if the last letter is '+' and exclude it.
    if userInput[len(userInput)-1] == '+':
        userInput = userInput[0:len(userInput)-1]

    # Display users request.
    print("User asked for: " + userInput + "\n")

    # Set the URL
    myUrl = "https://api.edamam.com/search?q=" + userInput + \
        "&app_id=$55554362&app_key=$65a9ee67bc50f65260eeb2b7b0705164&from=0&to=3&calories=591-722&health=alcohol-free"


    ########## Getting info #########

    # Access url data.
    r = requests.get(myUrl)

    # Access/request the part you need.
    r_dict = r.json()
    r_hits = r_dict['hits']
    r_recipe = r_hits[0]['recipe']

    # Ingredients
    r_ingredients = r_recipe['ingredientLines']
    r_shareUrl = r_recipe['shareAs']
    r_label = r_recipe['label']


    return[r_label, r_ingredients, r_shareUrl]
    
