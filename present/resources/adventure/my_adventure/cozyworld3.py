from game_engine import * 
import cozyworld
import random
import time

# ===== 

STATE = "INIT"

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

COMPILATION_COMPLETION_AMOUNT=10
@Action("Check computer", "c")
def check_computer(player, room):
    global ROTIMATIC_INITIALIZED
    global COMPILATION_COMPLETION_AMOUNT
    print("""
        Your computer merrily boops, indicating
        that compilation is {}% complete.
        """.format(COMPILATION_COMPLETION_AMOUNT))
    if COMPILATION_COMPLETION_AMOUNT >= 100:
        ROTIMATIC_INITIALIZED = True
        print("""
        INITIALIZING PROGRAM TRANSFER!!!!!!
        ...
        PROGRAM TRANSFER COMPLETE!!!!
        """)
        delete_action(check_computer)

register_action(cozy_cabin, check_computer)

@Action("Check the door", "cd")
def check_door(player, room):
    global STATE
    print("""
        You peek through the peep hole, and observe
        a baby polar bear in a sweater.
        """)
    delete_action(check_door)
    register_action(cozy_cabin, answer_door)
    STATE = "KNOCK_COMPLETE"

@Action("Answer Door", "ad")
def answer_door(player, room):
    print("""
        "HELLO, MISTAH!"
        "DELIVERY!!! SIGN HERE!"

        You sign there, and the baby polar bear
        promptly unloads a large box into your
        house before lifting off in its miniature
        mail dirigible.

        You faintly hear a distant
        "MEWWY CHRISMUSS!!!" as the airship
        floats off into the stratosphere.
        """)
    delete_action(answer_door)
    register_action(cozy_cabin, open_package)

@Action("Open package", "o")
def open_package(player, room):
    print("""
        You open the package......


        AND REVEALED IS
        A MIGHTY
        ROTIMATIC!!!!!!!!!!!
        """)
    global COMPILATION_COMPLETION_AMOUNT
    COMPILATION_COMPLETION_AMOUNT = 50
    delete_action(open_package)
    link_rooms(cozy_cabin, rotimatic, "Right next to you", ("r", "cc"),
               "...")

NUM_DANCES = 0
@Action("Dance to pass time", "d")
def dance_to_pass_time(player, room):
    global NUM_DANCES
    global COMPILATION_COMPLETION_AMOUNT
    if NUM_DANCES >= 2:
        print("""
        WHOO!!! That was some good dancin!!!
        Surely that must be enough waiting, now!
        """)
        COMPILATION_COMPLETION_AMOUNT = 100
        delete_action(dance_to_pass_time)
    else:
        print("""
        You boogie furiously
        """)
        COMPILATION_COMPLETION_AMOUNT += 20
        NUM_DANCES += 1

# ===== 

rotimatic = Room("The Rotimatic", """
        The Rotimatic, that marvel of engineering, gleams
        before you, enigmatic and majestic- in it lies
        the infinite possibilities of the act of creation.
        """,
        "the Rotimatic gleams",
        noop)

ROTIMATIC_INITIALIZED = False
ROTIMATIC_FIRST_TIME = True
@Action("Activate Rotimatic", "a")
def activate_rotimatic(player, room):
    global ROTIMATIC_INITIALIZED
    global ROTIMATIC_FIRST_TIME
    if not ROTIMATIC_INITIALIZED:
        print("""
        ERROR! NO PROGRAM LOADED!
        """)
        if ROTIMATIC_FIRST_TIME:
            register_action(cozy_cabin, dance_to_pass_time)
    else:
        print("""
        ACTIVATING!!! RUNNING PROGRAM: MAKE COOKIES FOR SANTA!

        The Rotimatic springs into action, using its advanced
        bakery circuits to lovingly whip up a batch of
        chocolate chip cookies!

        In no time at all, a freshly baked and delicious
        batch of homemade chocolate chip cookies slides out
        of the Rotimatic's dispensing slot.
        """)
        register_action(rotimatic, prepare_offering_for_santa)
        delete_action(activate_rotimatic)

register_action(rotimatic, activate_rotimatic)

@Action("Prepare offering for santa", "cp")
def prepare_offering_for_santa(player, room):
    global STATE
    print("""
        With great care, you lovingly lay out
        the cookies in offering for santa.

        What an eventful evening! You
        feel sleepy!
        """)
    STATE = "sleepy"
    delete_action(prepare_offering_for_santa)


# ===== 

def show_pantry(player):
    print("""
        You are in the cake pantry, filled with
        rows and rows of sachertorte-filled
        shelfs. The shelves themselves are
        made of a handsome walnut wood, worn
        smooth and dark from years of use.
        """)
    global STATE
    if STATE == "INIT":
        STATE = "TIME4KNOCK"
        global COMPILATION_COMPLETION_AMOUNT
        COMPILATION_COMPLETION_AMOUNT = 20

cake_pantry = Room("The Cake Pantry", "",
        "a delicious aroma wafts...",
        show_pantry)

@Action("Check cake port", "cp")
def check_cake_port(player, room):
    print("""
        You take a quick peek at the cake port.
        It's empty. You consult the schedule, and it
        looks like you're smack-dab in the middle
        of the holiday cake hiatus. Luckily,
        however, you are well stocked as it is!
        """)

register_action(cake_pantry, check_cake_port)

@Action("Eat cake", "eat")
def eat(player, room):
    print("""
        NOM NOM NOM NOM NOM""")
    increment_stat(player, "coziness", 1)
    increment_stat(player, "satiety", 1)
    sachertorte_piece.delete()
sachertorte_piece = Thingy("A piece of sachertorte", "sc",
        make_print_action("""
        You put the piece of cake in your pocket for later."""),
        make_print_action("""
        You gently fish the cake our of your pocket
        and lay it down on a napkin."""),
        [],
        [eat])
register_action(cake_pantry, sachertorte_piece.grab)

# ===== 

bedroom = Room("The bedroom", """
        A cozy bed, piled up with blankets sits in the corner,
        surrounded by stuffed animals of various shapes and sizes.
        """,
        "a restful aura emanates",
        noop)

@Action("Go to bed", "gb")
def go_to_bed(player, room):
    global STATE
    if STATE == "sleepy":
        print("""
        You enter snooze town...

        "Hi booper!" says booper groggily, as you enter the cozy zone.
        Did you make cookies for santa?

        "Yup!" you answer affirmatively.

        "Good, good", says booper, drifting back to sleep.

        ZZzzzZZZzzzzzz

        MERRY CRIMMAS! <3
        I LOVE YOU BOOPY!!!
        <3 <3 <3 <3 <3 <3
        """)
        exit(0)
    else:
        print("""
        You can't go to bed! You aren't sleepy yet!
        """)

register_action(bedroom, go_to_bed)

# ===== LINK ROOMS
        
link_rooms(cozy_cabin, cake_pantry, "Through a little wooden door", ("pp", "cc"),
           "You amble through the door...")
link_rooms(cozy_cabin, bedroom, "Through a rounded arch", ("bd", "cc"),
           "You slip through the arch...")

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
