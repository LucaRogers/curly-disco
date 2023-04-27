import time

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Player:
    def __init__(self):
        self.inventory = []

    def take(self, item_name):
        for item in current_room.items:
            if item.name == item_name:
                current_room.items.remove(item)
                self.inventory.append(item)
                print(f"You take the {item_name}")
                return
        print("That item is not in the room")

# Define the rooms and items in the game
key = Item("key", "An old rusty key.")
chest = Item("chest", "A large wooden chest.")
treasure = Item("treasure", "A pile of glittering gold coins.")
start_room = Room("start", "You are in a dark room. There is a door to the north.")
north_room = Room("north", "You are in a room with a treasure chest.")
north_room.add_item(chest)
end_room = Room("end", "Congratulations! You have found the treasure.")
end_room.add_item(treasure)

# Set up the game
player = Player()
current_room = start_room

# Define the game loop
while True:
    # Display the current room
    print(f"You are in {current_room.name}.")
    print(current_room.description)
    for item in current_room.items:
        print(f"There is a {item.name} here.")

    # Get the player's input
    command = input("What do you want to do? ").split()

    # Process the player's input
    if command[0] == "go":
        if command[1] == "north" and current_room.name == "start" and key in player.inventory:
            current_room = north_room
            print("You unlock the door with the key and enter the next room.")
        elif command[1] == "end" and current_room.name == "north" and chest in player.inventory:
            current_room = end_room
        else:
            print("You can't go that way.")
    elif command[0] == "take":
        player.take(command[1])
    elif command[0] == "use":
        if command[1] == "key" and current_room.name == "start":
            player.inventory.remove(key)
            print("You unlock the door with the key.")
        elif command[1] == "chest" and current_room.name == "north":
            print("You open the chest.")
            current_room.items.remove(chest)
            current_room.add_item(treasure)
        else:
            print("You can't use that here.")
    elif command[0] == "inventory":
        print("You are carrying:")
        for item in player.inventory:
            print(item.name)
    elif command[0] == "quit":
        break
    else:
        print("I don't understand that command.")

    # Pause for dramatic effect
    time.sleep(1)
