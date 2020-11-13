import json

GAME = {
    '__metadata__': {
        'title': 'stuck_at_home',
        'start': 'mudroom',
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

    if ends_game:
        room['ends_game'] = ends_game

    GAME[name] = room
    return room

def create_exit(source, destination, description):
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

mudroom = create_room("mudroom", "You have entered your house. What now?")
mudroom["items"].append('Shoes')
basement = create_room("basement", "The basement is scary!!!", ends_game=True)
bedroom = create_room("bedroom", "You're in your bedroom. Where else could you go?")
bedroom["items"].append('Bed')
bathroom = create_room("bathroom","You're in the bathroom. You had to go.")
bathroom["items"].append('Soap')
living_room = create_room("living room", "You're in the living room. Watch some TV!")
living_room["items"].append('television')
outside = create_room("outside", "You're outside! There's COVID out here!!!", ends_game=True)
kitchen = create_room("kitchen", "Nice, you're in the kitchen for the tenth time today! Is there any food in the fridge this time?")
kitchen["items"].append('No food')
stairs = create_room("staircase", "Should you climb again?")
stairs["items"].append('Stairs')

create_exit(mudroom, stairs, "You go up the staircase to the second floor.")
create_exit(stairs, mudroom, "You go back down the stairs.")
create_exit(stairs, living_room, "You hear the TV. Sounds binge-worthy")
create_exit(living_room, stairs, "You're bored of the TV")
create_exit(stairs, bedroom, "You want to lay in your bed.")
create_exit(bedroom, stairs, "You go back to the stairs.")
create_exit(stairs, bathroom, "You go to the bathroom.")
create_exit(bathroom, stairs, "You go back to the stairs.")
create_exit(mudroom, kitchen, "You're hungry.")
create_exit(kitchen, mudroom, "Go back to mudroom.")

create_exit(bedroom, bathroom, "You have to fo to the bathroom.")
create_exit(bathroom, bedroom, "You are tired. You need a nap.")
create_exit(bathroom, living_room, "You went to the bathroom. You want to watch more TV.")
create_exit(living_room, bathroom, "You've watched a lot of TV. You have to go to the bathroom.")

create_exit(stairs, basement, "You are bored of everywhere else in your house. You decide to venture into the basement.")
create_exit(stairs, outside, "You are tired of being stuck inside.")

with open('stuck_at_home.json', 'w') as out:
    json.dump(GAME, out, indent=2)