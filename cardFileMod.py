import json

def printAllInDict(dictToBePrinted):
    for each_item in dictToBePrinted:
        print(each_item + ': ' + dictToBePrinted[each_item])

def doSomething(cardFile):
    # Initializes cardsDict with all cards from cardFile
    cardsDict = {}
    with open(cardFile, 'r') as cards:
        cardsDict = json.load(cards)

    # Asks the user what they want to do
    whatYouWouldLikeToDo = input('What would you like to do?\nOptions:\n\t(0) Print all cards\n\t(1) Add a card\n\t(2) Remove a card\n\t(3) Switch card color\n\t(Anything Else) Exit\n')

    # What the user tells it is done here
    if whatYouWouldLikeToDo == '0':
        printAllInDict(cardsDict)
        print(str(cardsDict.__len__())+" Cards in all")
        print("---------------------------")
        doSomething(cardFile)
    elif whatYouWouldLikeToDo == '1':
        newCardTitle = input('Type the name of the card that you would like to add: ')
        newCardDesc = input('Type the description of the card you wish to add: ')
        with open(cardFile, 'w') as cards:
            cardsDict[newCardTitle] = newCardDesc
            json.dump(cardsDict, cards)
        print("---------------------------")
        doSomething(cardFile)
    elif whatYouWouldLikeToDo == '2':
        cardToBeRemovedTitle = input('Type the name of the card you wish to remove or type 0986 if you don\'t: ')
        if cardToBeRemovedTitle != '0986':
            areYouSureRemove = input('Are you sure you want to remove ' + cardToBeRemovedTitle + ' from the file? Type the name of the card to confirm: ')
            if areYouSureRemove == cardToBeRemovedTitle:
                cardToBeRemoved = cardsDict.pop(cardToBeRemovedTitle)
                with open(cardFile, 'w') as cards:
                    json.dump(cardsDict, cards)
                print('Just removed ' + cardToBeRemovedTitle + ' from the file.')
                print("---------------------------")
                doSomething(cardFile)
            else:
                print("---------------------------")
                doSomething(cardFile)
        else:
            print("---------------------------")
            doSomething(cardFile)
    elif whatYouWouldLikeToDo == '3':
        chooseColor()
    else:
        print('You said something different. I don\'t like that. Good bye!')

def chooseColor():
    color = input("Which color of cards would you like to use (red or green, default red)? ")
    print("---------------------------")
    if color != "":
        doSomething(color+"Cards.json")
    else:
        doSomething("redCards.json")
    
# Executes the program
chooseColor()
