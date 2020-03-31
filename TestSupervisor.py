import Server
import MultiClient


operationSwitch = {
    "1":MultiClient.handleNewCloseUp,
    "2":Server.addUser,
    "3":Server.addTerminal,
    "4":Server.removeUser,
    "5":Server.removeTerminal
}

print("I handle these options:")
print("")
print("1. to simulate close up card to terminal")
print("2. to add new card")
print("3. to add new terminal")
print("4. to remove card (from datebase)")
print("5. to remove card (from datebase)")

while True:
    print("")
    print("")
    print("What to do now?")
    print("")
    operation = input()
    operationSwitch[operation]()