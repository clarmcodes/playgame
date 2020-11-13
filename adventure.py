import json

# This global dictionary stores the name of the room as the key and the dictionary describing the room as the value.
GAME = {
    '__metadata__': {
        'title': 'Adventure',
        'start': 'classroom'
    }
}

def create_room(name, description, ends_game=False):
    """
    Create a dictionary that represents a room in our game.

    INPUTS:
     name: string used to identify the room; think of this as a variable name.
     description: string used to describe the room to the user.
     ends_game: boolean, True if arriving in this room ends the game.
    
    RETURNS:
     the dictionary describing the room; also adds it to GAME!
    """
    assert (name not in GAME)
    room = {
        'name': name,
        'description': description,
        'exits': [],
        'items': [],
    }
    # Does this end the game?
    if ends_game:
        room['ends_game'] = ends_game

    # Stick it into our big dictionary of all the rooms.
    GAME[name] = room
    return room

def create_exit(source, destination, description):
    """
    Rooms are useless if you can't get to them! This function connects source to destination (in one direction only.)

    INPUTS:
     source: which room to put this exit into (or its name)
     destination: where this exit goes (or its name)
     description: how to show this exit to the user (ex: "There is a red door.")
     required_key (optional): string of an item that is needed to open/reveal this door.
     hidden (optional): set this to True if you want this exit to be hidden initially; until the user types 'search' in the source room.
    """
    # Make sure source is our room!
    if isinstance(source, str):
        source = GAME[source]
    # Make sure destination is a room-name!
    if isinstance(destination, dict):
        destination = destination['name']
    # Create the "exit":
    exit = {
        'destination': destination,
        'description': description
    }
    source['exits'].append(exit)
    return exit

##
# Let's imagine 4 places:
# Note that earlier, in __metadata__ we said that we should start in classroom.
##
classroom = create_room("classroom", "You're in a lecture hall, for some reason.")
hallway = create_room("hallway", "This is a hallway with many locked doors.")
bathroom = create_room("bathroom", "You're in a small bathroom.")
staircase = create_room("staircase", "The staircase leads downward.")
outside = create_room("outside", "You've escaped! It's cold out.", ends_game=True)

##
# Let's connect them together.
# It's not a very fun adventure, but it's simple.
##
create_exit(hallway, bathroom, "A door on your left is open a crack.")
create_exit(bathroom, hallway, "Go back to the hallway.")
create_exit(classroom, hallway, "A door leads into the hall.")
# If you want doors to work in both directions; you have to do that yourself.
create_exit(hallway, classroom, "Go back into the classroom.")
# Note we can also refer to places by their names (same as their variables for my sanity!)
create_exit('hallway', 'staircase', "A door with the words STAIRS is stuck open.")
create_exit(staircase, hallway, "Nevermind; go back to the hallway.")

create_exit(staircase, outside, "A door at the bottom of the stairs has a red, glowing, EXIT sign.")
# we don't go back from outside, because the game ends as soon as we get there.

##
# Save our text-adventure to a file:
##
with open('adventure.json', 'w') as out:
    json.dump(GAME, out, indent=2)
    
import json

GAME = {
    '__metadata__': {
        'title': 'Adventure',
        'start': 'classroom'
    }
}

def create_room(name, description, ends_game=False):

    assert (name not in GAME)
    room = {
        'name': name,
        'description': description,
        'exits': [],
        'items': [],
    }
    
    if ends_game:
        room['ends_game'] = ends_game

    GAME[name] = room
    return room

def create_exit(source, destination, description):
    """
    Rooms are useless if you can't get to them! This function connects source to destination (in one direction only.)

    INPUTS:
     source: which room to put this exit into (or its name)
     destination: where this exit goes (or its name)
     description: how to show this exit to the user (ex: "There is a red door.")
     required_key (optional): string of an item that is needed to open/reveal this door.
     hidden (optional): set this to True if you want this exit to be hidden initially; until the user types 'search' in the source room.
    """
    if isinstance(source, str):
        source = GAME[source]
    if isinstance(destination, dict):
        destination = destination['name']
    exit = {
        'destination': destination,
        'description': description
    }
    source['exits'].append(exit)
    return exit

classroom = create_room("classroom", "You're in a lecture hall, for some reason.")
classroom["items"].append('Book')
hallway = create_room("hallway", "This is a hallway with many locked doors.")
hallway["items"].append('Pencil')
staircase = create_room("staircase", "The staircase leads downward.")
staircase["items"].append('Pen')
outside = create_room("outside", "You've escaped! It's cold out.", ends_game=True)
bathroom = create_room("bathroom","You're in the bathroom. You had to go.")
bathroom["items"].append('Toilet Paper')
basement = create_room("basement", "You've found yourself in the scary basement. Uh oh.", ends_game=True) #I MADE THIS
basement["items"].append('Death')

create_exit(classroom, hallway, "A door leads into the hall.")
create_exit(classroom, basement, "You see a light in the distance.")
create_exit(hallway, classroom, "Go back into the lecture hall.")
create_exit('hallway', 'staircase', "A door with the words STAIRS is stuck open.")
create_exit(staircase, hallway, "Nevermind; go back to the hallway.")
create_exit(hallway, bathroom, "There is a bathroom door.")
create_exit(bathroom, hallway, "Go back to the hallway.")
create_exit(bathroom, classroom, "Go back into the lecture hall.")
create_exit(staircase, outside, "A door at the bottom of the stairs has a red, glowing, EXIT sign.")

with open('adventure.json', 'w') as out:
    json.dump(GAME, out, indent=2)
