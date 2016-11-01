#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the Troll's riddle game.
"""
import random

riddles = {"You will always find me in the past.\nI can be created in the present,\
            \nbut the future can never taint me." : 'history',\
            "Feed me and I live,\nyet give me a drink and I die" : 'fire',\
            "The more of them you take,\nthe more you leave behind." : 'footsteps',\
            "I don't have eyes, but once I did see.\nOnce I had thoughts, but now I'm white and empty." : 'skull',\
            "It can be cracked,\nit can be made,\nit can be told,\nit can be played.": 'joke',\
            "What gets broken without getting hold?" : 'promise',\
            "Everyone has it. \nThose who have it least don’t know that they have it.\
            \nThose who have it most wish they had less of it; \nbut never too little or none at all." : 'age',\
            "Poor people have it.\nRich people need it.\nIf you eat it you die." : 'nothing',\
            "What disappears the moment you say it's name?" : 'silence',\
            "What has no beginning,\nno end, nor middle?" : 'circle',\
            "I can run, but never walk.\nI have a mouth, but I never talk.\nI have a head, but I never weep.\
            \nI have a bed, but I never sleep." : 'river',\
            "What doesn't get any wetter, \no matter how much rain falls on it?" : 'water',\
            "We hurt without moving.\nWe poison without touching. \nWe bear the truth and the lies.\
            \nWe are not to be judged by our size." : 'words',\
            "What part of the ocean is the deepest?" : 'bottom',\
            "I have a head but no body, a heart but no blood.\
            \nJust leaves and no branches, I grow without wood." : 'lettuce',\
            "I run forever, but never move at all.\
            \nI have not lungs nor throat, but still a mighty roaring call." : 'waterfall',\
            "If you have it, you can share it.\nIf you share it, you will lose it." : 'secret',\
            "What is always coming but never arrives?" : 'tomorrow',\
            "Alive without breath, as cold as death.\nNever thirsty, ever drinking,\
            \nall in mail never clinking." : 'fish',\
            "Voiceless it cries, wingless it flutters.\nToothless it bites, mouthless it mutters." : 'wind',\
            "I am light as a feather, but the world’s strongest man\
            \ncouldn’t hold me for more than five minutes" : 'breath',\
            "What type of tree can you carry in your hand?" : 'palm',\
            "What has an eye, but cannot see?" : 'needle',\
            "They come out at night without being called.\nThey are lost in the day without being stolen." : 'stars',\
            "It lives without a body, hears without ears,\
            \nspeaks without a mouth, to which the air alone gives birth." : 'echo',\
            "You hear it speak, for it has a hard tongue.\nBut it cannot breathe, for it has no lung." : 'bell',\
            "Thousands build walls of gold within this house,\nbut no man made it.\
            \nSpears past counting guard this house,\nbut no man wards it." : 'beehive',\
            "A thousand colored folds stretch toward the sky\nAtop a tender strand, rising from the land,\
            \nuntil picked one by humans' hand, perhaps a token of love,\nperhaps to say goodbye." : 'flower',\
            "I fly when I am born,\nlie when I am alive, \nand run when I am dead." : 'snowflake',\
            "Thirty white horses on a red hill.\nFirst they champ, then they stamp,\nthen they stand still." : 'teeth',\
            "It cannot be seen nor be felt,\ncannot be heard nor smelt.\nIt lies behind stars and under hills,\
            \nAnd empty holes it fills.\nIt comes first and follows after. \nEnds life, kills laughter." : 'darkness',\
            "This thing all things devours: \nBirds, beasts, trees, flowers\
            \nGnaws iron, bites steel, grinds hard stones to meal.\
            \nSlays king, ruins town, and beats high mountains down." : 'time',\
            "I am always hungry,\nI must always be fed.\nThe hand I touch, will soon turn red" : 'fire',\
            "Half-way up the hill, I see thee at last, lying beneath me with thy sounds and sights.\
            \nA city in the twilight, dim and vast, with smoking roofs, soft bells, and gleaming lights." : 'past',\
            "Until I am measured I am not known,\nYet how you miss me when I have flown." : 'time',\
            "Each morning I appear to lie at your feet,\nAll day I will follow no matter how fast you run,\
            \nYet I nearly perish in the midday sun." : 'shadow',\
            "Glittering points that downward thrust,\nsparkling spears that never rust." : 'icicles',\
            "What does man love more than life\nFear more than death or mortal strife\
            \nWhat the poor have, the rich require,\nand what contented men desire.\
            \nWhat the miser spends and the spendthrift saves\nAnd all men carry to their graves" : 'nothing',\
            "It cannot be seen, it weighs nothing,\nbut when put into a barrel and it makes it lighter." : 'hole',\
            "Kings and queens may cling to power \nand the jesters may have their call.\
            \nI am the most common but I rule them all." : 'ace',\
            "Flat as a leaf, round as a ring;\nHas two or four eyes, can't see a thing." : 'button',\
            "You feel me but you cannot see me.\nI am always with you, but I never get heavy.\
            \nYou shiver when I come, and are relieved when I pass." : 'fear',\
            "I am in the beginning of eternity,\nat the end of time and space" :'e',\
            "What is the difference between yesterday and tomorrow?" : 'today',\
            "My step is slow, the snow's my breath\nI give the ground a grinding death\
            \nMy marching makes an end of me\nSlain by sun or drowned in sea." :'glacier',\
            "A slow, solemn square-dance\nof warriors feinting.\nOne by one they fall,\
            \nWarriors fainting,\nthirty-two on sixty-four." : 'chess',\
            "I have split the one into five.\nI am the circle that some will spy.\nI am the path that breaks and gives.\
            \nI am the bow no man may bend." : 'rainbow',\
            "Dipping, glinting, gliding by,\nRainbow-fretted, wrought of breath.\nI live only while I fly.\
            \nEarth's rough kiss my sudden death." : 'bubble',\
            "I'm simple for a few people\nbut hard for them to hear \
            \nI live inside of secrets\nI bring people's worst fears" : 'truth',\
            "Never resting, never still. \nMoving silently from hill to hill.\nIt does not walk, run or trot.\
            \nAll is cool where it is not." : 'sunshine',\
            "It turns everything around,\nbut does not move." : 'mirror',\
            "It has a head, a tail,\nbut no arms nor legs" : 'coin',\
            "With a halo of water and a tongue of wood,\nstone as skin long I stood." : 'castle',\
            "I beam, I shine, I sparkle white. \nI’ll brighten the day with a single light.\
            \nI’ll charm and enchant all.\nI’ll bring the best in you all." :'smile',\
            "I go from house to house,\na messenger small and tight.\
            \nWeather it rains or snows.\nI sleep outside at night." : 'road',\
            "I have cities with no people,\nforests with no trees,\nand oceans with no water.": 'map',\
            "I only exist when you are here.\nWhere you never were,\nI can never be." : 'reflection',\
            "If a man carried my burden\nHe would break his back.\nI am not rich,\
            \nBut leave silver in my track." :'snail',\
            "We are five little objects of an everyday sort\nyou will find us all in the ladies’ court." : 'vowels',\
            "Weight in my belly,\nTrees on my back,\nNails in my ribs,\nFeet I do lack." : 'ship',\
            "You heard me before,\nYet you hear me again,\nThen I die,\n‘Till you call me again." : 'echo',\
            "To unravel me you need a simple key,\nNo key that was made by locksmith’s hand,\
            \nBut a key that only I will understand." :'cipher',\
            "When there is fire in me then I am still cold.\nWhen I own your true love’s face then you will not see me.\
            \nTo all things I give no more than I am given.\
            \nIn time I may have all things, and yet I can keep nothing." : 'mirror',\
            "I make you weak at the worst of all times.\nI keep you safe, I keep you fine.\
            \nI make your hands sweat, and your heart grow cold,\nI visit the weak, but seldom the bold." : 'fear',\
            "I am the hole in the night,\nthe ever watchful eye.\nI return in a cycle,\
            \nto enlighten the sky." : 'moon',\
            "You can see nothing else\nWhen you look in my face,\nI will look you in the eye\
            \nAnd I will never lie." : 'reflection',\
            "Something wholly unreal, yet seems real to I\nThink my friend, tell me where do I lie?" : 'mind',\
            "A precious stone, as clear as diamond.\nSeek it out whilst the sun’s near the horizon.\
            \nThough you can walk on water with its power,\nTry to keep it, and it’ll vanish ere an hour." : 'ice',\
            "I’m pleasing to the eye\nA tool for many absent of mind\nA tapestry of fickle lies\
            \nBlind to even the most pensive spies\nI’m often the breeder of fervent lust\
            \nBut I am by far one you shouldn’t trust" : 'apperance',\
            "What is put on a table, cut, but never eaten?" : 'cards'}

def clue_riddles():
    """
    Ask COMPANION for help
    """
    print("Your companion wiggles its ear and admits to not\
    \nbeing any good at riddles itself, your companion\
    \nis able to recite a chapter from the book\
    \n\n[Mountain Trolls and Other Creatures fond of Rhymes and Poetry]:\
    \n===============================================================\
    \n1. Trolls like their answers in lower case letters without any spaces.\
    \n2. The answer should never be more that one word,\
    \n(Trolls easily mix words togeather).\
    \n3. Answers are always just a word, without articles.\
    \n4. If the riddle describes something in singular or plural,\
    \nthe answer will most likely have the same inflexion.\
    \n===============================================================\n")
    input("Press Enter to continue...")
    print("\nYour companion scurries back onto your shoulder and it firmly\
    \nreminds you that using the Internet to look for answers\
    \nwould be cheating.")
    input("Press Enter to continue...")
    print("\nThankful it knew more about riddles than you did,\
    \nyou go back to the riddle game.\n\n")
    print("\nTroll says: Tell me your answer.\n")

def riddle_game():
    """
    This is the riddle game function.
    """
    guessesTaken = 0
    fails = 0
    riddle, answer = random.choice(list(riddles.items()))

    #You get a second chance
    print("\nYou kick the huge rock!\n\nIt's a mountain troll!\nApparently you woke it from it's nap.\
        It looks very angry.\
        \nIt tells you to answer it's riddle in order\nto gain passage trough the Mountains.\
        \nThe troll is blocking the way and it seems you have no other choice...\n")
    input("Press Enter to continue...")
    while fails < 2:
        print("\nTroll says:")
        print("=================================================")
        print(riddle)
        print("=================================================")
        print("\nTell me your answer.\n")
        while guessesTaken < 3:
                   
            guess = input()
            guess = str(guess).lower()

            #get a clue
            if guess == "clue":
                guessesTaken = guessesTaken - 1
                clue_riddles()

            # try to get away
            elif guess == "north" or guess == "south" or guess == "west" or guess == "east":
                print("You can't get away!")

            #guess corrext
            elif guess == answer:
                guessesTaken = guessesTaken + 1
                print("The Troll grumbles. You guessed the riddle in {0} guesses!\
                    \nYour companion is very proud of you.".format(guessesTaken))
                print("\nYou have aquired a riddle pass!\nNow you're able to travel trough the Mountains.")
                print("The riddle pass was added to your inventory.")
                return
            
            #guess wrong
            else:
                guessesTaken = guessesTaken + 1
                print("\nTroll says:")
                print("Your answer is wrong.\nYou have {0} guesses left.\n".format(3 - guessesTaken))
                       
        if guessesTaken >= 3:
            fails = fails + 1
            if fails == 1:
                print("\nTroll says:")
                print("You have lost.\nI will give you a second chance.\nThis will be your last.\n")
                #resets guesses
                guessesTaken = 0
                #removes the first riddle from the dict
                del riddles[riddle]
                riddle, answer = random.choice(list(riddles.items()))

    input("Press Enter to continue...")
    print("\nYou fail the troll's game.")
    #Game resets fails and guesses
    guessesTaken = 0
    fails = 0
    print("The angry Troll smashes you into a bloody puddle.\nYou die!")
    exit()
