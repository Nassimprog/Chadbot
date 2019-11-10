import requests  # <<<<< Module use was inspired by Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"


# Google API Places key: AIzaSyD9r3ZeVFzujJrqogY_3QiY9r_gdSQYm80
def NearestPlace(userMessage):

        # Change the list input into a string
        userInput = userMessage.replace(" ", "+")

        # Check user input.
        print("User asked for: " + userInput + "\n")

        # <<<<< Link obtained from official documentation of Google Places API "https://developers.google.com/places/web-service/search"
        myUrl = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + userInput + \
                "&url,radius=1500&key=AIzaSyD9r3ZeVFzujJrqogY_3QiY9r_gdSQYm80"

        print(myUrl)

        # Access the URL and return it for display!
        # <<<<< Line inspired and modified from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"
        r = requests.get(myUrl)

        # <<<<< Accesing of json data inspiered from Youtube video: "https://www.youtube.com/watch?v=tb8gHvYlCFs&list=LLxk7l4FGLLteogNk27_nZEQ&index=46&t=264s"
        r_dict = r.json()
        r_results = r_dict['results']

        # Put the first three addresses into a list and Return it.
        myAddressList = []
        myNameList = []

        # Get the Names.
        for i in range(3):
                r_name = r_results[i]['name']
                myNameList.append(r_name)

        # Get the Adresses.
        for i in range(3):
                r_formatted_address = r_results[i]['formatted_address']
                myAddressList.append(r_formatted_address)

        # Return the Names and Addresses as a list.
        return([myNameList, myAddressList])
