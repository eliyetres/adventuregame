#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPANION
"""
import random

def companion_image():
    """
    Your companion! Image 1 
    """
    return r"""
  _ _/|
 \'o.o', 
  (___)
    """

def companion_image2():
    """
    Your companion! Image 2
    """
    return r"""
|\_/|
`o.o'
(___)
    """

def companion_image3():
    """
    Your companion! Image 2
    """
    return r"""
   /\_/\
   'o.o',
   (___)
    """

def companion_image4():
    """
    Your companion! Image 1 
    """
    return r"""
  _ _/|
 \'-.o', 
  (___)
    """

#Functions to randomize companion image
random_companion = [companion_image4, companion_image3, companion_image2, companion_image]

def companion_prologue():
    """
    Prologue for your companion
    """
    print("\nAs you rise from the bed you feel something underneath your foot.\
    	\nYou look at what seems like a large ball of dust,\
    \nbut after a closer look you see this is a small fluffy creature.\
    \nAs it creeps out into the sunlight you notice the creature is a furry brown ball with a hint of purple.\
    \nAlthough it only seems to speak in giggles and laughter\
    \nyou understand it, and it wants to be your friend!\
    \nIt will follow you on your adventure as your companion!")
    print(random.choice(random_companion)())
    print("You added companion to your inventory!\
        \nYou can ask the companion for help by typing 'clue'.")
    input("Press Enter to continue...")
