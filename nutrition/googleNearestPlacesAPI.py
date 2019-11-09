import requests


# Google API Places key: AIzaSyD9r3ZeVFzujJrqogY_3QiY9r_gdSQYm80
def NearestPlace(userMessage):

        # Change the list input into a string
        userInput = userMessage.replace(" ", "+")

        # Add if you don't want to specify where.
        # userInput += "+in+Coventry"

        # Check user input.
        print("User asked for: " + userInput + "\n")

        myUrl = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + userInput + \
                "&url,radius=1500&key=AIzaSyD9r3ZeVFzujJrqogY_3QiY9r_gdSQYm80"

        print(myUrl)

        # Access the URL and return it for display!
        r = requests.get(myUrl)
        
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


