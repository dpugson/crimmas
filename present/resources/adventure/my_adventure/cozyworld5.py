from game_engine import * 
import cozyworld
import cozyworld2
import cozyworld3
import random
import time

# ===== 


def show_cozy_cabin(player):
    print("""
        You are snug in your armchair,
        nestled in the coziest corner of your
        cozy cabin.

        A merry fire crackles away in the hearth
        across from you, and the walls teem
        with elaborately embroidered stockings.
        """)
    global STATE
    if STATE == "TIME4KNOCK":
        print("""
        KNOCK KNOCK KNOCK!!!!

        Someone is knocking at the door!""")
        register_action(cozy_cabin, check_door)

cozy_cabin = Room("Your room", "",
        "the fire flickers...",
        show_cozy_cabin)

def show_arcade(player):
    print("""
        You find yourself in The Arcade...
        The warm, comforting glow of game machines
        
        """)
    global STATE
    if STATE == "TIME4KNOCK":
        print("""
        KNOCK KNOCK KNOCK!!!!

        Someone is knocking at the door!""")
        register_action(cozy_cabin, check_door)

cozy_cabin = Room("Your room", "",
        "the fire flickers...",
        show_cozy_cabin)

# ===== LINK ROOMS
        

# ARCADE

link_rooms(arcade, cozyworld3.cozy_cabin, "A worn game cabinet covered in a knit cozy is labeled", ("cw3", "quit"),
           "LOADING...")
link_rooms(arcade, cozyworld2.cozy_room, "A sleek game cabinet shaped like a robot is labeled", ("cw2", "quit"),
           "LOADING...")
link_rooms(arcard, cozyworld.foyer, "A fuzzy game gabinet shaped like a teddy bear is labeled", ("cw1", "quit"),
           "LOADING...")

#========== THE WORLD

def world():
    conditions = []
    def world_action(player):
        nonlocal conditions
        for condition in conditions:
            condition.check(player)

    return World(cozy_cabin, world_action)

def player():
    player = Player();
    set_stat(player, "coziness", 5)
    return player

