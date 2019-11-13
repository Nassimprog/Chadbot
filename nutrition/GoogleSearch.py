import requests

def Search(userMessage):
    userInput = userMessage.replace(" ", "+")
    print("User asked for: " + userInput + "\n")

    # Set the URL
    myUrl = 'https://www.googleapis.com/customsearch/v1?key=UseYourKey=003476000010048778020:ucsazjp5fku&q=' + userInput

    # Test url
    r = requests.get(myUrl)

    # Access/request the part you need.
    r_dict = r.json()
    item = r_dict['items']

    snippet = item[0]['snippet']
    linkToWeb = item[0]['link']

    return([snippet, linkToWeb])