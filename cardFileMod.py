import json

def printAllInDict(dictToBePrinted):
    for each_item in dictToBePrinted:
        print(each_item + ': ' + dictToBePrinted[each_item])

def doSomething():
    # Initializes redCardsDict with all cards from redCards.json
    redCardsDict = {}
    with open("redCards.json", 'r') as redCards:
        redCardsDict = json.load(redCards)

    # Asks the user what they want to do
    whatYouWouldLikeToDo = input('What would you like to do?\nOptions:\n\t(0) Print all cards\n\t(1) Add a card\n\t(2) Remove a card\n\t(Anything Else) Exit\n')

    # What the user tells it is done here
    if whatYouWouldLikeToDo == '0':
        printAllInDict(redCardsDict)
        doSomething()
    elif whatYouWouldLikeToDo == '1':
        newCardTitle = input('Type the name of the card that you would like to add: ')
        newCardDesc = input('Type the description of the card you wish to add: ')
        with open('redCards.json', 'w') as redCards:
            redCardsDict[newCardTitle] = newCardDesc
            json.dump(redCardsDict, redCards)
        doSomething()
    elif whatYouWouldLikeToDo == '2':
        cardToBeRemovedTitle = input('Type the name of the card you wish to remove or type 0986 if you don\'t: ')
        if cardToBeRemovedTitle != '0986':
            areYouSureRemove = input('Are you sure you want to remove ' + cardToBeRemovedTitle + ' from the file? Type the name of the card to confirm: ')
            if areYouSureRemove == cardToBeRemovedTitle:
                cardToBeRemoved = redCardsDict.pop(cardToBeRemovedTitle)
                with open('redCards.json', 'w') as redCards:
                    json.dump(redCardsDict, redCards)
                print('Just removed ' + cardToBeRemovedTitle + ' from the file.')
            else:
                doSomething()
        else:
            doSomething()
    else:
        print('You said something different. I don\'t like that. Good bye!')

# Executes the program
doSomething()
