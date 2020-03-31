import Datebase
from datetime import datetime

def RFIDreceived(cardId, terminalId):
    now = datetime.now()
    recvTimestamp = datetime.timestamp(now)
    cardUser = Datebase.getUserWithCardId(cardId)
    terminal = Datebase.getTerminalWithId(terminalId)
    if cardUser is None:
        Datebase.logForbiddenAttempt(recvTimestamp, cardId, terminalId)
    elif terminal is None:
        print("Card close up to unregistered terminal")
    else:
        print("card id '{}' belong to '{}' spotted in terminal nr {} - description '{}', at {}".format(cardUser.cardId, cardUser.name ,terminal.terminalId,terminal.terminalDescription,now.strftime("%d/%m/%Y, %H::%M::%S")))
        Datebase.logDoorUsage(recvTimestamp, cardId, terminalId)

def addUser():
    name = input("type name ")
    cardId = input("type card id ")
    Datebase.addNewUser(Datebase.User(cardId,name))

def addTerminal():
    terminalId = input("type terminal ID ")
    terminalDesc = input("type terminal description ")
    Datebase.addNewTerminal(Datebase.Terminal(terminalId, terminalDesc))

def removeTerminal():
    terminalId = input("Type termina ID to delete ")
    Datebase.removeTerminalById(terminalId)

def removeUser():
    userName = input("Type user name to delete ")
    Datebase.removeUserByName(userName)
