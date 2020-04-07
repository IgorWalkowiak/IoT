import paho.mqtt.client as mqtt

broker = "127.0.0.1"

terminal_id = input("Type terminal id ")

client = mqtt.Client()
client.connect(broker)
client.publish("terminal/register", "register" + "." + terminal_id)

def call_worker(card_id):
    client.publish("terminal/closeup", "closeup" + "." + card_id + "." + terminal_id)

def handleNewCloseUp():
    print("New close-up")
    card_id = input("Type ID of card ")
    call_worker(card_id)

if __name__ == "__main__":
    while True:
        handleNewCloseUp()