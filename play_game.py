import json
import time
from datetime import datetime
start_time = datetime.now


def main():
    game_choice = int(input("Which game would you like to play? 1. Spooky Mansion or 2. Adventure or 3. Stuck at Home?\n"))
    if game_choice == 1:
        choice = 'spooky_mansion.json'
    if game_choice == 2:
        choice = 'adventure.json'
    if game_choice == 3:
        choice = 'stuck_at_home.json'
    with open(choice) as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)
    

    
def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...', 'Marbles', 'Wallet']
    visited = {}

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        
        if current_place in visited:
            print ("...You've been in this room before...")
        visited[current_place] = True

        # TODO: print any available items in the room...
        print (' ')
        if here["items"]== []:
            print ("There is no stuff in this room.")
        else:
            print ("There is a", here["items"])
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break
        print (' ')
        visible_exits = find_visible_exits(here, stuff)
        print ('These are the exits you see: \n')
        for i, exit in enumerate(visible_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # Allow the user to choose an exit:
        print (' ')
        print ('These are the exits you are able to use: \n')
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()
        print ('You said', action)
        
        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        if action == "help":
            print_instructions()
            continue
        
        if action == "stuff":
            if stuff ==[]:
                print ("You have nothing.")
            else:
                print('you have: ', stuff) 
            continue
        
        if action == "take":
            if here["items"]== []:
                print ('there is nothing here to take')
            else:
                print ("You took", here["items"])
                stuff.extend(here["items"])
                here["items"].pop()
            continue
        
        if action == "drop":
            x = str(input("What do you want to drop? \n"))
            try:
                stuff.remove(x)
                here["items"].append(x)
                print ("You dropped", x)
                print ("You have", stuff)
            except:
                print ("You got don't have", x)
            continue
        
        if action == "search":
            for exit in here ['exits']:
                if exit.get("hidden", True):
                    print (exit)
                    exit["hidden"] = False
        
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            if 'required_key' in selected:
                if selected ['required_key'] not in stuff:
                    print ["you can't open the door because it's locked"]
                    continue
                else: print ("you unlock the door")
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
            
        
    print("")
    print("")
    print("=== GAME OVER ===")
    time_elapsed = datetime.now() - start_time 
    print("You were in this game for {} (hh:mm:ss.ms)".format(time_elapsed))

def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        if "required_key" in exit:
            if exit["required_key"] in stuff:
                usable.append(exit)
            continue
        usable.append(exit)
    return usable

def find_visible_exits(room,stuff):
    visible = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        visible.append(exit)
    return visible

def no_bridge_to_nowhere(rooms):
    list_of_rooms = []
    for room in rooms:
        list_of_rooms.append(room["name"])
    for room in rooms:
        for i in range(len(room["exits"])):
            if room["exits"][i]["destination"] not in list_of_rooms:
                print("Not in List")

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" - Type 'help' to print the instructions again.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()
