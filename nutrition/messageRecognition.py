def Recognition(userMessage):
    
    # List of foods to search.
    foodList = ['corn','beef', 'popcorn', 'pork', 'chicken', 'artichoke'
                ,'aubergine',
                'eggplant',
                'asparagus',
                'legumes',
                'alfalfa sprouts',
                'azuki beans',
                'adzuki',
                'bean sprouts',
                'bean',
                'black beans',
                'black-eyed peas',
                'borlotti bean',
                'broad beans',
                'chickpeas',
                'garbanzos',
                'ceci beans',
                'green beans',
                'kidney beans',
                'lentils',
                'lima beans'
                ,'Butter bean'
                ,'mung beans'
                ,'navy beans'
                ,'pinto beans'
                ,'runner beans'
                ,'split peas'
                ,'soy beans'
                ,'peas'
                ,'mangetout'
                ,'snap peas'
                ,'broccoflower'
                ,'broccoli'
                ,'brussels sprouts'
                ,'cabbage'
                ,'kohlrabi'
                ,'cauliflower'
                ,'celery'
                ,'endive'
                ,'fiddleheads'
                ,'frisee'
                ,'fennel'
                ,'greens'
                ,'beet'
                ,'bok choy'
                ,'chard'
                ,'collard greens'
                ,'kale'
                ,'mustard greens'
                ,'spinach'
                ,'anise'
                ,'basil'
                ,'caraway'
                ,'coriander'
                ,'chamomile'
                ,'dill'
                ,'fennel'
                ,'lavender'
                ,'lemon Grass'
                ,'marjoram'
                ,'oregano'
                ,'parsley'
                ,'rosemary'
                ,'sage'
                ,'thyme'
                ,'lettuce'
                ,'arugula'
                ,'mushrooms'
                ,'nettles'
                ,'new zealand spinach'
                ,'okra'
                ,'onions'
                ,'chives'
                ,'Garlic'
                ,'leek'
                ,'onion'
                ,'shallot'
                ,'scallion'
                ,'parsley'
                ,'peppers'
                ,'bell pepper'
                ,'chili pepper'
                ,'jalapeño'
                ,'habanero'
                ,'paprika'
                ,'tabasco pepper'
                ,'cayenne pepper'
                ,'radicchio'
                ,'rhubarb'
                ,'beetroot'
                ,'beet'
                ,'mangel-wurzel'
                ,'carrot'
                ,'celeriac'
                ,'corms'
                ,'eddoe'
                ,'konjac'
                ,'taro'
                ,'water chestnut'
                ,'ginger'
                ,'parsnip'
                ,'rutabaga'
                ,'radish'
                ,'wasabi'
                ,'horseradish'
                ,'white radish'
                ,'daikon'
                ,'tubers'
                ,'jicama'
                ,'jerusalem artichoke'
                ,'potato'
                ,'sunchokes'
                ,'sweet potato'
                ,'yam'
                ,'turnip'
                ,'salsify'
                ,'skirret'
                ,'sweetcorn'
                ,'topinambur'
                ,'squashes'
                ,'acorn squash'
                ,'bitter melon'
                ,'butternut squash'
                ,'banana squash'
                ,'courgette'
                ,'zucchini'
                ,'cucumber'
                ,'delicata'
                ,'gem squash'
                ,'hubbard squash'
                ,'marrow'
                ,'squash'
                ,'spaghetti squash'
                ,'tat soi'
                ,'tomato'
                ,'watercress'
                ,'açaí'
                ,'akee'
                ,'apple'
                ,'apricot'
                ,'avocado'
                ,'banana'
                ,'bilberry'
                ,'blackberry'
                ,'blackcurrant'
                ,'black sapote'
                ,'blueberry'
                ,'boysenberry'
                ,'buddha\'s hand'
                ,'fingered citron'
                ,'Crab apples'
                ,'Currant'
                ,'Cherry'
                ,'Cherimoya'
                ,'Custard Apple'
                ,'Chico fruit'
                ,'Cloudberry'
                ,'Coconut'
                ,'Cranberry'
                ,'Cucumber'
                ,'Damson'
                ,'Date'
                ,'Dragonfruit'
                ,'Pitaya'
                ,'Durian'
                ,'Elderberry'
                ,'Feijoa'
                ,'Fig'
                ,'Goji berry'
                ,'Gooseberry'
                ,'Grape'
                ,'Raisin'
                ,'Grapefruit'
                ,'Guava'
                ,'Honeyberry'
                ,'Huckleberry'
                ,'Jabuticaba'
                ,'Jackfruit'
                ,'Jambul'
                ,'Japanese plum'
                ,'Jostaberry'
                ,'Jujube'
                ,'Juniper berry'
                ,'Kiwano'
                ,'horned melon'
                ,'Kiwifruit'
                ,'Kumquat'
                ,'Lemon'
                ,'Lime'
                ,'Loganberry'
                ,'Loquat'
                ,'Longan'
                ,'Lychee'
                ,'Mango'
                ,'Mangosteen'
                ,'Marionberry'
                ,'Melon'
                ,'Cantaloupe'
                ,'Honeydew'
                ,'Watermelon'
                ,'Miracle fruit'
                ,'Mulberry'
                ,'Nectarine'
                ,'Nance'
                ,'Orange'
                ,'Blood orange'
                ,'Clementine'
                ,'Mandarine'
                ,'Tangerine'
                ,'Papaya'
                ,'Passionfruit'
                ,'Peach'
                ,'Pear'
                ,'Asian pear'
                ,'Chinese pear'
                ,'Nashi pear'
                ,'Asian pear'
                ,'Ya pear'
                ,'Chinese white pear'
                ,'Persimmon'
                ,'Plantain'
                ,'Plum'
                ,'Prune'
                ,'dried plum'
                ,'Pineapple'
                ,'Pineberry'
                ,'Plumcot'
                ,'Pluot'
                ,'Pomegranate'
                ,'Pomelo'
                ,'Purple mangosteen'
                ,'Quince'
                ,'Raspberry'
                ,'Salmonberry'
                ,'Rambutan'
                ,'Mamin Chino'
                ,'Redcurrant'
                ,'Salal berry'
                ,'Salak'
                ,'Satsuma'
                ,'Soursop'
                ,'Star apple'
                ,'Star fruit'
                ,'Strawberry'
                ,'Surinam cherry'
                ,'Tamarillo'
                ,'Tamarind'
                ,'Tayberry'
                ,'Ugli fruit'
                ,'White currant'
                ,'White sapote'
                ,'Yuzu'
                ,'Avocado'
                ,'Bell pepper'
                ,'Chile pepper'
                ,'Corn kernel'
                ,'Cucumber'
                ,'Eggplant'
                ,'Olive'
                ,'Pea'
                ,'Pumpkin'
                ,'Squash'
                ,'Tomato'
                ,'Zucchini']
    wordsNotList = ['n\'t', 'not', 'without', 'no']
    wordsYesList = ['want', 'need', 'should', 'could', 'must', 'have to', 'give me']
    wordsReverseList = ['but', 'altho', 'however', 'Although']

    # Checks.
    isWanted = True
    foodWant = 0

    # List of wanted food.
    edibleList = []
    nonEdibleList = []

    # Separate user Message.
    userList = userMessage.split(' ')

    # Remove duplicates from my List
    foodList = list(dict.fromkeys(foodList))
    #print(foodList)

    # Check if user message.
    for i in range(len(userList)):

        
        ###### Check the meaning of words #####

        # Check if the word is Negative.
        for y in range(len(wordsNotList)):

            if wordsNotList[y] in userList[i]:
                isWanted = False
                foodWant += 1

        # Reverse back.
        for y in range(len(wordsReverseList)):

            if wordsReverseList[y] in userList[i]:
                isWanted = not(isWanted)
                foodWant = 0

        # Check if the word is Positive.
        for y in range(len(wordsYesList)):

            if wordsYesList[y] in userList[i] and foodWant == 0:
                isWanted = True


        ###### Adding Words to the Right lists. ########

        # Add the words to their Respective Lists
        if isWanted == True:

            # Add food to Edible food list.
            for y in range(len(foodList)):

                if foodList[y].lower() in userList[i].lower():
                    edibleList.append(foodList[y].lower())

                    if foodList[y].lower() in nonEdibleList:
                        nonEdibleList.remove(foodList[y].lower())

        else:
            # Add food to Non Edible food list.
            for y in range(len(foodList)):

                if foodList[y].lower() in userList[i].lower():
                    nonEdibleList.append(foodList[y].lower())
                    foodWant = 0

                    if foodList[y].lower() in edibleList:
                        edibleList.remove(foodList[y].lower())


    # Remove duplicates form the LISTS
    edibleList = list(dict.fromkeys(edibleList))
    nonEdibleList = list(dict.fromkeys(nonEdibleList))

    return(edibleList)


#print(Recognition('.recipe Hi there, I want something with mango, chicken actually I don\'t want mango but give me lemon.'))
