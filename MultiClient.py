import Server


def handleNewCloseUp():
    print("New close-up")
    cardId = input("type ID of card ")
    terminal = input("Type from which terminal ")
    Server.RFIDreceived(cardId, terminal)
