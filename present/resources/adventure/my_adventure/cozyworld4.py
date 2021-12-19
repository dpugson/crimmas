from game_engine import * 
import random
import time

# ===== 

STATE="INIT"

def show_cozy_cabin(player):
    global STATE
    if STATE == "INIT":
        print("""
        You are snug in your overstuffed armchair,
        nestled in the most extremely cozy corner of your
        most extraordinarily cozy cabin.
        """)
        print("""
        Memoriabilia from your long and storied career in
        the cozy service line the walls... Assorted medals,
        photos of yourself with cozy luminaries, certificates
        of commendation, trophies, and ceremonial plaques
        cover every available surface.

        A pot-bellied stove merrily glows in the corner,
        and an old phonograph crackles soothingly as it
        plays those sweet old tunes from way back when.
        """)
    elif STATE == "MISSION":
        print("""
     .\ ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' /_
     -  RING RING RING RING RING RING RING!!!! -
      / , , , , , , , , , , , , , , , , , , , \\

        The Dedicated Line to the Cozy Presidential Palace is ringing.""")
        register_action(cozy_cabin, answer_phone)
    elif STATE == "CRASHED":
        print("""
        The COZY MOBILE lies gleaming amidst the debris
        from the collapsed roof. You'll have to have a
        word with HQ...
        """)

SNOOZE_COUNT=0
@Action("snooze", "s")
def snooze(player, room):
    global STATE
    global SNOOZE_COUNT
    if SNOOZE_COUNT > 2:
        if STATE != "INIT":
            print("""
        Sadly, it seems like you're not going to
        be able to snooze any time soon...""")
            return
        STATE="MISSION"
    else:
        print("""
        You doze off...""")
        if SNOOZE_COUNT==0:
            print("""
        You dream of cozier times...
        You return to a teddy bear tea party in Chamonix-Mont-Blanc...""")
        if SNOOZE_COUNT==1:
            print("""
        You dream of sugar plums...
        They dance mesmerizingly...""")
        if SNOOZE_COUNT==2:
            print("""
        You dream of your retirement party...
        Attends included 5 Cozy Presidents, the entire
        Comittee of the Cozy Coterie, the chief 
        Commissar of Cozy Studies...""")

        SNOOZE_COUNT += 1

cozy_cabin = Room("Your room", "",
        "the stove gloves...",
        show_cozy_cabin)

@Action("answer phone", "a")
def answer_phone(player, room):
    global STATE
    print("""
        Rousing yourself relectantly from your cozy spot,
        you slowly putter over a wooden panel on the wall.
        With a wave of your Cozy Key, the wooden panel slides
        up into the wall, exposing the Cozy Phone.
        You answer it and hear the following message:

        "BOOOOOOOOOP
        BOOP
        BOOOOOP
        BOOOOP
        BOOOOOOP
        BOOOP
        BOOOOOOOOP
        BOOOP
        BOOOOP
        
        CLICK"

        Your training clicks in immediately.
        The fact that this message is in code
        means it must be EXTREMELY SENSITIVE and
        HIGHLY CONFIDENTIAL... And the fact that
        they called you, interrupting your well-earned
        cozy retirement, means that it must be a COZY MISSION
        of the utmost importance for the COZY WORLD.

        You recognize in the pattern of boops- *something*
        differs between each boop. This *something* likely
        forms a multi-digit numeric code... A numeric code that...

        \  |  |  | /
        - CRASH!!!! -
        /  |  |  | \\

        ...Can most likely be used to unlock your
        old friend, the COZY MOBILE, which just crashed
        through your roof and is now resting in your
        living room.
    """)
    STATE="CRASHED"
    delete_action(answer_phone)
    register_action(cozy_cabin, remember_puzzle)
    register_action(cozy_cabin, enter_code)

@Action("remember puzzle", "r")
def remember_puzzle(player, room):
    global STATE
    print("""
        Activating your EIDETIC MEMORY, you remember
        the code:

        "BOOOOOOOOOP
        BOOP
        BOOOOOP
        BOOOOP
        BOOOOOOP
        BOOOP
        BOOOOOOOOP
        BOOOP
        BOOOOP
        
        CLICK"
    """)

SECRET_CODE1="925463834"

register_action(cozy_cabin, snooze)

@Action("enter code", "e")
def enter_code(player, room):
    global STATE
    text = input("ENTER CODE $")
    if text == SECRET_CODE1:
        print("""
        CODE ACCEPTED! WELCOME BACK, AGENT BOOP.

        The doors to the COZY MOBILE open noiselessly,
        raising up like the wings of a gull.
        """.format(text))
        STATE="MOBILE_OPEN"
    else:
        print("""
        INCORRECT CODE!!!!!
        """.format(text))
    delete_action(remember_puzzle)
    delete_action(enter_code)

# ===== LINK ROOMS
        

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
    set_stat(player, "coziness", 1000)
    player.appearance="""
        You are wearing the uniform that
        you are entitled to as Cozy Czar Emeritus:
        a big fuzzy blanket and cozy slippers.

        You feel real cozy!!!
    """
    return player
