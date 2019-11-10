import requests  # <<<<< Module use was inspired from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"


def foodRecipe(userMessage):

    ########## Editing User Message for url link ############

    # Change the list input into a string
    userInput = ''
    for i in userMessage:
            userInput += i
            userInput += ' '
    userInput = userInput.replace(' ', '+')

    # Check if the First Letter is '+' and exclude it.
   # if userInput[0] == '+':
     #   userInput = userInput[1:len(userInput)]

    # Check if the last letter is '+' and exclude it.
    #if userInput[len(userInput)-1] == '+':
     #   userInput = userInput[0:len(userInput)-1]

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
