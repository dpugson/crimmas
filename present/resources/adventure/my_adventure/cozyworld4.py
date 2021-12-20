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
    elif STATE == "SUCCESS":
        print("""
        Luminaries from all around the CozySphere have gathered
        for the award ceremony, dressed up in their finest Cozy Regalia:
        beautiful sweaters and fluffy blankes abound.

        The current Cozy President itself, President Conical Robot Topped with a Star,
        bestows upon you the highest order in the cozy kingdom:

            -----------------------------------------------------
           |*~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~*|
           |                                                     |
           |                                                     |
           |          This Certificate Announces That            |
           |     The Honorable Majesty Cozy President MMCXXIV    |
           |           Has inducted AGENT BOOP into              |
           |      The Ancient Order of the Blessed Boop 2000+    |
           |       For Meritorious Service to All Booper Kind    |
           |                                                     |
           |     X CoZy PrEsIdEnT             .----.             |
           |       ''''''''''''''            //COZY\\\\            |
           |                                 ''....''            |
           |*~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~/  .  '~_~_~_~_~_~*|
            ----------------------------------r . .  '-----------
                                             / ^. .^..

        HUZZAH HUZZAH HUZZAH!!!

        I love you!!!!
        Merry Christmas!!!! 'W'

        ~ Love, Booper
        """)
        exit()

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
        "your cozy cabin beckons...",
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
    link_rooms(cozy_cabin, boop_mobile_cabin, "Through gullwing doors", ("o", "o"),
               "You pass through the Boop Mobile's precision-engineered doors...")

MISSION_STATUS="INCOMPLETE"
boop_mobile_cabin = Room("Inside the Boop Mobile", """
        The Boop Mobile - a masterpiece of vehicular design.
        The control panel of the Boop Mobile is illuminated
        before you.

         - - - - - - - - - - - - - - - - - 
        |                                 |
        |   MISSION STATUS: {}
        |                                 |
         - - - - - - - - - - - - - - - - - 

        The on-ship Computer chimes in:

        "SALUTATIONS, AGENT BOOP! WHAT ACTION WOULD YOU LIKE TO TAKE?"
        """.format(MISSION_STATUS),
        "The Boop Mobile, in your living room...",
        noop)

@Action("STATE MISSION", "sm")
def state_mission(player, room):
    print("""
        YOUR MISSION, SHOULD YOU CHOSE TO ACCEPT IT,
        IS TO RESET THE COZY PRESIDENT'S PASSWORD
        FOR BOOPCRAFT!

        THE CP (COZY PRESIDENT) CHANGED THE PASSWORD LAST WEEK
        IN RESPONSE TO A SECURITY SUGGESTION- BUT,
        IN A TRAGIC TURN OF EVENTS, PROMPTLY FORGOT
        IT. THE CP HAS NOW BEEN WITHOUT BOOPCRAFT
        FOR OVER 72 HOURS! THE CURRENT STATE OF THE
        PRESIDENT'S BOOPéMONS IS UNCERTAIN.
    """)
    delete_action(state_mission)
    register_action(boop_mobile_cabin, enumerate_assets)

register_action(boop_mobile_cabin, state_mission)

@Action("ENUMERATE ASSETS", "ea")
def enumerate_assets(player, room):
    print("""
        ASSETS:

            THE MARVEL OF ENGINEERING, the singular BOOP MOBILE
            AGENT BOOP, COZY PRESIDENT EMERITUS and LEGENDARY SEMI-RETIRED FIELD AGENT
            AGENT SWAMP A. MANYTREES, intelligence expert embedded in the FIELD
    """)
    delete_action(enumerate_assets)
    register_action(boop_mobile_cabin, inquire)

@Action("INQUIRE INTO ACTIVITIES OF AGENT S. MANYTREES", "i")
def inquire(player, room):
    print("""
        AGENT SWAMP A. MANYTREES IS CURRENTLY AT AN UNKNOWN LOCATION,
        FULLY UNTRACEABLE AND INCOGNITO TO ENSURE TOTAL SECURITY.

        THEY HAVE BEEN COMMUNICATING WITH HQ VIA A DEAD DROP
        IN THE CANARY ISLANDS.
    """)
    delete_action(inquire)
    link_rooms(boop_mobile_cabin, canary_islands, "A button press away,", ("fly", "fly"),
               "WOOSH!!!!!")


def show_canary_islands(player):
    global MISSION_STATUS
    if MISSION_STATUS == "SUCCESS":
        print("""
        YOU DID IT!

        The beautiful verdant isles and sparkling
        water below fill you with a sense of wonder.
        """)
    else:
        print("""
        The BOOP MOBILE is now over the Canary Islands
        If you look down at the islands, you notice a
        strange pattern of Giant Flowering Trees making forms
        in the canopy of the Canarian forest.
        This must be the dead drop!

        Looking close, you see a pattern in the trees...

        354S136H309L146O218H378D175W171C343E128T291O36 345S339P7B267Y47P244 337E66E22B191S228A256Y201O46S227P269A53N374P188O114T203E375 30S258E252L283T54 101S326O21 110N331N123U287M13T260L208A51 302 130R200C350 85O92K111T366W17I384D115 144S303F212T199 140E164B352R119T361 113C324 255L67C154L202D176L301E225E135C259L120H84T37S25N274D307T32R318F289N198S243G41M49A183O271 383E386S185 272A329 189P132A184U349E235A34E126E363A186S63P357E159 250C68O55C182Y230A105O209S292E27 4N262T107 245P372T308 190 166E11 285E90I293S179G193Y214P40P315S314R79T319 72M254R355I323H138N223T265S15P344I76D261 71 12S24I60S147P263H387T369D29B297O160B294 211S237E168O282 389P359T133L368R215 94S281E317O356D9O304I207R233S239D358N229P376G112A174O35D39O59 153L139N231Y204 216I103S388O220A277O1A33V290G108C6 264I377O118 116M56O20M327R348H300H242N295S342S247R276S305R149I187T224H165L129E311T341N87 19A232A61T234 163A28O14O270R340O320E117E362P162 93 62O266 86P131N373O330I18 137A241I246A210E364S95Y197I332 134 122O178D106P161E155 78N127X152I177E371S322C8O23E279A102 2G16 273N26G31E142S321A45 180E346 221R194 296T52I219E82Y251U48E325W192A268E10P42U240O236R89H73Y69D104T150 109O248T58E3E336R253A124G170A385 313E334Y205P158T298P213O299T275 328D169 98N222 195T125H226 88T143 338S99Y5T335 316 278 50K380S306S312T367O121R148 353E370 382E80I97O217 257W75I43S284H351P206H77E81T65D286 310E280R157O173N100M64 83S141L360S365S91N381P167T347T249I333M151W145T196H57D156N379 74 38T172K44T70E288A96N181 238

        There appear to be numbers *and* letters visible...
        It seems like the numbers are associated with single letters-
        AHA! They must be the *order* in which the letters appear in the
        original message! 2O1B4P3O could, for instance, be decoded as
        BOOP.
        """)

canary_islands = Room("The Canary Islands", "",
        "THE CANARY ISLANDS...",
        show_canary_islands)

PASSWORD="POTATO"
# please only tell accredited tropical orchards!

@Action("CHECK PASSWORD", "cp")
def check_password(player, room):
    global STATE
    global MISSION_STATUS
    text = input("ENTER PASSWORD $")
    if text.upper() == PASSWORD:
        print("""
        PASSWORD VALIDATED!!!!
        
        You've done it again agent boop!!!
        Return to your home for the Award Ceremony!
        """.format(text))
        MISSION_STATUS="SUCCESS"
        STATE="SUCCESS"
        delete_action(check_password)
    else:
        print("""
        INCORRECT!!!!! TRY AGAIN
        """.format(text))

register_action(canary_islands, check_password)

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
