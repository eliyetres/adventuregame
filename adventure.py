#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
imported modules
"""
from companion import random_companion, companion_prologue
from asci import logo, dungeon_image, mountains_image, lake_image, village_image, castle_image,\
forest_image, inn_image, treasure_image, beat_game_img
from riddles import riddle_game
import random
import json
import time
import os
import sys
import getopt

"""
BASIC GAME INFO
"""
#
# Global default settings
#
NAME = ""
OUTPUT = None

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

# Info about the program and controls
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Elin Hagman"
VERSION = "1.1"
USAGE = """{program} By {author}, version {version}.

Usage:
  {program}
  """.format(program=PROGRAM, author=AUTHOR, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)

ARGUMENTS = """
Options:
-------
-h, --help          Description of the program and parameters that work.
-i, --info          Description of the game and the game idea.
-v, --version       Game version.
-a, --about         Short about the game's author.
-c, --cheat         How to cheat and beat the game in the shortest way possible.
-s, --start         Start the game!

Game controls:
-------
i, info                     Description of the current room.
l, look                     Look around and see if there is something particular to see.
b, object                   Info about your environment and available items.
l [object], look [object]   Displays a description of the object
o [object], open [object]   Opens object, if possible.
k [object], kick [object]   Kick an object making it break, if possible.
m [object], move [object]   Move the object to another place, if possible.
inv, inventory              Shows your inventory.
c, clue                     Get a clue to what you should do next.
south, north, east, west    Directions where you can move.
quit                        Quit the game.

"""

"""
Parsing options
"""
def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """
    try:
        opts, dummy_args = getopt.getopt(sys.argv[1:], "hviacs", [
            "help",
            "version",
            "info",
            "about",
            "cheat",
            "start"])
        for opt, dummy_arg in opts:
            print(opt)
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-i", "--info"):
                printInfo()

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-a", "--about"):
                printAbout()

            elif opt in ("-c", "--cheat"):
                printCheat()

            elif opt in ("-s", "--start"):
                start_game()

            else:
                assert False, "Unhandled option"
        
    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        # traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)

"""
Menu functions
"""
def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    print(ARGUMENTS)
    sys.exit(exitStatus)

def printVersion():
    """
    Print version information and exit.
    """
    print("\n") 
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)

def printInfo():
    """
    Print information about the game and the game's idea.
    """
    print(AUTHOR)
    print(PROGRAM)
    print(logo())
    print("A fantasy text-based adventure game, the Adventure Game!\
        \ntake your new found friend along on your adventure trough villages, mountains\
        \nand castles! Measue your guile against different creatures in your quest for treasure!")

def printAbout():
    """
    Short about the game's author
    """
    print(AUTHOR)
    print("Description:")
    print("25 year student, lives in Gothenburg and studies Cognition Science.")
    print("Likes rpgs' and silly games.")

def printArguments():
    """
    Game arguments and options
    """
    print(ARGUMENTS)

def printCheat():
    """
    Tells you how to beat the game by cheating
    """
    print("Type 'jump' to get to the next room without checking criteria")

"""
Random choices depending on player's choices.
Open json file
Inventory
Current room
"""
# if open object contains nothing
emptyness = ["It's empty.", "It's nothing there.", "There is nothing there you can pick up."]

# If exception in game options
loitering = ["You scatch your head. This clearly did nothing.",\
            "Nothing happened.", "Nothing happens.", "You feel like something should happen. \nBut it doesn't.",\
            "You slur something incomprehensible into the air.", "It's a time and place for everything! But not now.",\
            "You hear birds chirping. Besides that, nothing happens.", "Nope.", "Maybe ask your companion for help",\
            "Just as you reach out for something you\nforget what it was you were looking for.",\
            "Well, that clearly didnt work!", "You slur something incomprehensible",\
            "You forget what you were looking for.", "Nah.", \
            "Your eyes ponder the items. It seems unclear what to do with them.",\
            "You clearly have no idea what you are doing. \nMaybe you should ask COMPANION for help?",\
            "Hmm... no. \nMaybe you should ask COMPANION for a clue.", "You should probably ask for help.",\
            "You have absolutley no idea of what you are doing.", "You have no idea what you are doing",\
            "Maybe you should ask for a clue.", "You can use --help if you don't know how to move."
            ]

# Opens json object tree structure, includes rooms and items
json_object = json.loads(open('roomsjson.json').read())

# Room the player starts in; key pointing to json-object
currentRoomKey = "Inn"

#inventory, empty
inventory = []


################################## FUNCTIONS ####################################

"""
Game prologue and companion functions
"""
def prologue():
    """
    Starting prologue
    """
    print("\nYou wake up to the sun shining trough the window.")
    time.sleep(2)
    print("You don't remember a lot from the day before,\
    \nand you seem to have misplaced all of your clothes.")
    time.sleep(2)
    print("You'd better take a look around.\n")

"""
Functions for INFO, INVENTORY, OPEN, KICK, LOOK and MOVE.
"""

def currentRoom():
    """
    Current room player is in
    """
    #global currentRoomKey
    return json_object[currentRoomKey]

def roomInfo(room):
    """
    Print info about the current room
    """
    print("---------------------------------")
    print(room["description"])
    print("---------------------------------")
    room_images()

def room_images():
    """
    ascii images for all rooms
    """
    if currentRoomKey == "Inn":
        print(inn_image())
    elif currentRoomKey == "Village":
        print(village_image())
    elif currentRoomKey == "Mountains":
        print(mountains_image())
    elif currentRoomKey == "Lake":
        print(lake_image())
    elif currentRoomKey == "Forest":
        print(forest_image())
    elif currentRoomKey == "Dungeon":
        print(dungeon_image())
    elif currentRoomKey == "Castle":
        print(castle_image())
    else:
        print("No picture yet! Boo!")

def look(room):
    """
    Look option
    """
    look_around = room["Look"]
    print("You look around.\n")
    print(look_around)

def roomObjects(room):
    """
    Use --OBJECT. Check current room for objects (and directions).
    """
    #check items
    items = room["items"]
    print("\nYou look around and see: ",)
    for item in items:
        print(item,)
    print("")
    #check possible directions
    directions = room["ConnectingRooms"]
    for move in directions:
        print("To the {0} is the {1}.".format(move, directions[move]))

def lookObject(room, obj):
    """
    Use --LOOK + OBJECT. Look at an object.
    """
    try:
        all_items = room["items"]
        the_item = all_items[obj]
        obj_description = the_item["description"]
        print(obj_description)
        try:
            #check if item is kickable
            status = the_item["kickable"]["status"]
            print("It's {0}.".format(status))
        except Exception:
            print("")
    except Exception:
        print("\nThere is no such object here.")

def goToRoom(new_room):
    """
    Move to a new room
    """
    global currentRoomKey
    room_help = json_object[currentRoomKey]["Help"]
    room_criteria = json_object[new_room]["RoomCriteria"]
    #if criteria item(s) is in inventory:
    ok = True
    for it in room_criteria:
        ok = ok & (it in inventory)
    if ok:
        #go to new room
        currentRoomKey = new_room
        print("You go to the {0}.".format(new_room))
        roomInfo(currentRoom())
    else: print("You can't go there yet!\n{0}".format(room_help))

def openObject(obj):
    """
    OPEN an object
    """
    try:
        global inventory
        room = currentRoom()
        item = room["items"][obj]
        print("\nYou check the {0}".format(obj))
        item_found = item["contains"]
        #remove item from json
        json_object[currentRoomKey]["items"][obj]["contains"] = ""
        if item_found != "":
            print("\nYou found {0}! That's nice.".format(item_found))
            #put item in your inventory
            inventory = inventory + [item_found]
        else: print("\nThere is nothing here you can pick up.")
    except Exception:
        print(random.choice(emptyness))

def kickObject(obj):
    """
    KICK an object
    """
    try:
        #try to find item in json-ojbect
        global inventory
        room = currentRoom()
        item = room["items"][obj]
        print("\nYou try to kick the {0}.".format(obj))
        try:
            #if item is breakable 
            kick_status = item["kickable"]["status"]
            #if it's already broken
            if kick_status == "broken":
                print("It's already broken!")
                return
            #change item status to broken
            json_object[currentRoomKey]["items"][obj]["kickable"]["status"] = "broken"
            broken_item = item["kickable"]["contains"]
            #add broken item to inventory
            inventory = inventory + [broken_item]
            print("You break the {0}!\nPicked up {1}.".format(obj, broken_item))

        except Exception:
            print("It doesen't break.")
    #if not found in json-object
    except Exception:
        print("You can't kick that.")

def change_status(obj, key):
    """
    Changes status of an item
    """
    obj[key] = "broken"
    print("Now it's {0}.".format(obj[key]))

def moveObject(obj):
    """
    MOVE an object
    """
    try:
        room = currentRoom()
        item = room["items"][obj]
        room = currentRoom()
        print("\nYou try to move the {0}.".format(obj))
        try:
            move_status = item["moveable"]["status"]
            if move_status == "You have moved it aside":
                print("You have already moved it.")
                return
            #change item status to moved    
            json_object[currentRoomKey]["items"][obj]["moveable"]["status"] = "You have moved it aside"
            print("You move the {0} aside.".format(obj))
            return
        except Exception:
            print("You can't move that!")

    except Exception:
        print("You couldn't move it.")

def inventory_print():
    """
    Inventory
    """
    print("Items in your inventory:")
    print("------------------------")
    print(inventory)

def cheat_game():
    """
    Cheat "jump". Skips to the next room without checkig for criteria
    """
    global currentRoomKey
    if currentRoomKey == "Inn":
        print("\nYou sprint outside! Who needs clothes anyway!\nYou pay no attention to the villagers staring at you.")
        currentRoomKey = "Village"
        roomInfo(currentRoom())
        return

    if currentRoomKey == "Village":
        print("\nYou dash to the Forest! You probably won't be needing any food after all.")
        currentRoomKey = "Forest"
        roomInfo(currentRoom())
        return
    
    if currentRoomKey == "Forest":
        print("\nYou tell yourself you're not afraid of the dark and run trough the Forest with your eyes closed.\
            \nAs you run info the pine and fir trees you wish you had put your clothes on.")
        currentRoomKey = "Lake"
        roomInfo(currentRoom())
        return
    
    if currentRoomKey == "Lake":
        print("\nYou sprint around the lake. No time for swimming!\nNor eating!")
        currentRoomKey = "Mountains"
        roomInfo(currentRoom())
        return
    
    if currentRoomKey == "Mountains":
        print("\nYou walk very quietly through the Mountain pass.")
        currentRoomKey = "Dungeon"
        roomInfo(currentRoom())
        return
    
    if currentRoomKey == "Dungeon":
        print("\nWhich way should we go? 'Eenie meenie miney mo...' Probably straight ahead!\
            \nWell, it seemed straight ahead was correct! Didn't need that map after all.")
        currentRoomKey = "Castle"
        roomInfo(currentRoom())
        return

    if currentRoomKey == "Castle":
        print("Wow, treasure already!")
        beat_game()

def beat_game():
    """
    When player beats the game
    """
    print(treasure_image())
    print("You beat the game! Yay!")
    print(beat_game_img())
    print(logo())
    exit()

def companion_help():
    """
    Gives you a clue on what to do next
    """
    #global currentRoomKey
    room_clue = json_object[currentRoomKey]["clue"]
    print(random.choice(random_companion)())
    print("Companion says:")
    print(room_clue)

"""
Minigames
"""
# Labyrith "game"
def labyrinth_game():
    """
    Labyrinth game
    """
    print("---------------------------------")
    print("You have walked into what looks like a labyrith. It's very dark.\
        \nUse the directions north, south, west and east to aimlessly wander the Dungeon.\
        \nLight is shining from the exit behind you, leading back to the Mountains.\
        \n\nType exit to go back to the entrance.")
    print("---------------------------------")
    
    #loop for labyrinth game
    while True:
        global inventory
        #random generated rooms and descriptions
        labyrinth_rooms = ["You walk into a very dark room.", "You walk into a tunnel.", "You come upon an archway.",\
        "It's an oubliette. Labyrinth's full of 'em, apparently."]
        labyrinth_description = ["It's very large.", "You find an increably small note saying \
        \n'- straight ahead to the Castle'.", "There is a skeleton lying in the corner beside you.\
        \nYou wonder how long it was since someone was here.", "There are some big rocks in this room."\
        "You hear some bats schrieking.", "You can barley see anything.", "It feels very cold.", \
        "A crystal ball lies shattered on the ground.", "You're wondering if you'll ever find a way forward.",\
        "Everything here looks the same.", "It somehow feels familiar.",\
        "Someone has painted 'HANNA MADE IT UP' on one of the walls.", "A voice whispers 'Don't go on...'",\
        "A voice whispers 'Go back, while you still can...This is not the way...'",\
        "A voice whispers 'Take heed, and go no further...'",\
        "A voice whispers 'Beware, beware... Soon it will be too late...'",\
        "You come upon two locked doors.\nThe first one says 'to the castle at the end of the labyrinth'\
        \nand the other one says 'leads to certain death'."]

        action = input().lower().split(' ', 1)

        if "exit" in action:
            print("You go back to the Dungeon's entrance.")
            break

        elif "clue" in action:
            print("Use the directions north, south, west and east to aimlessly wander the Dungeon.\
                \nSince you don't have a map you should probably be careful.\n Type exit to go back to the entrance.\n")

        elif "info" in action:
            print("You are in what looks like a labyrith.\
                \nLight is shining from the exit behind you, leading back to the Mountains.\n")

        elif 'south' in action or \
        'east' in action or \
        'west' in action or \
        'north' in action:
            print(random.choice(labyrinth_rooms))
            print(random.choice(labyrinth_description))
            print("\n")
            get_item = (random.randint(0, 5))
            if get_item == 1:
                print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●")
                print("You found a map lying on the ground!\nIt shows you the way in which to solve the labyrith.\n")
                print("A map of the labyrinth has been added to your inventory.\n")
                inventory = inventory + ["map"]
                break

        else:
            print("This dark place gives you chills.\nType 'exit' if you want to leave.\n")

# rocks game
def rocks_game():
    """
    Rocks game
    """
    global inventory
    print("You throw a rock at the hole.")
    time.sleep(2)
    hit = random.randint(0, 4)
    if hit == 1:
        #hit by random, gets sword
        print("You hit it!")
        if "sword" not in inventory:
            print("A small slight creature with long blonde hair peeks behind the rock formation.\
                  it tells you it is a woodland spirit that wants to help you on your journey.")
            print("\nYou got a sword!")
            inventory = inventory + ["sword"]
    else:
        print("You missed! Try again")

def villagers_conv():
    """
    Random NPC conversation
    """
    f = open('dialogue.txt') 
    lines = f.readlines()
    print("")
    print("You listen to the villagers conversation.")
    print("---------------------------------") 
    print(random.choice(lines))
    print(random.choice(lines))
    print(random.choice(lines))
    print("Enjoy the cookies!")
    print("---------------------------------")

"""
Game controls
"""

def game_options():
    """
    Loop that controls everything
    """
    while True:
        try:            
            #Player input
            action = input().lower().split(' ', 1)

            #All items in a room
            room = currentRoom()
            #all directions
            directions = ['north', 'south', 'west', 'east']
            global inventory
            #global currentRoomKey
            if "quit" in action:
                break

            elif action[0] in directions:
                if action[0] in room["ConnectingRooms"]:
                    goToRoom(room["ConnectingRooms"][action[0]])
        
            elif action[0] == "info" or action[0] == "i":
                roomInfo(room)              

            elif "inv" in action[0] or "inventory" in action[0]:
                inventory_print()

            elif action[0] == "object" or action[0] == "b":
                roomObjects(room)

            elif action[0] == "look" or action[0] == "l":
                if len(action) == 1:
                    look(room)
                else:
                    lookObject(room, action[1])

            elif action[0] == "open" or action[0] == "o":
                if action[1] == "labyrinth" and room["key"] == "Dungeon":
                    labyrinth_game()

                elif action[1] == "very round hole" and room["key"] == "Lake":
                    if "some stones" in inventory:
                        rocks_game()
                else:
                    if action[1] == "conversation with villagers":
                        villagers_conv()
                    openObject(action[1])

            elif action[0] == "kick" or action[0] == "k":
                if action[1] == "huge rock" and room["key"] == "Mountains":
                    if "riddle pass" not in inventory:
                        riddle_game()
                        roomInfo(room)
                        inventory = inventory + ["riddle pass"]
                else:
                    kickObject(action[1])

            elif action[0] == "move" or action[0] == "m":
                moveObject(action[1])

            elif "h" in action[0] or "help" in action[0]:
                printArguments()          

            elif action[0] == "clue":
                companion_help()

            elif action[0] == "jump":
                cheat_game()

            elif "100000000000000000 gold coins" in inventory:
                beat_game()

            else:
                print("You can't do that.")

        except Exception:
            print(random.choice(loitering))

def start_game():
    """
    Game start
    """
    global inventory
    print(logo())
    input("                       Press Enter to start the game!\n")
    prologue()
    input("Press Enter to continue...")
    roomInfo(currentRoom())
    input("Press Enter to continue...")
    print("")
    companion_prologue()
    inventory = inventory + ["companion"]
    printArguments()
    print("--------- GAME HAS STARTED ---------")
    game_options()


def main():
    """
    #Main function to carry out the work.
    """
    parseOptions()

    sys.exit(EXIT_SUCCESS)

if __name__ == "__main__":
    main()
