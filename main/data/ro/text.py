STR_GAME_TITLE = "Nothing Left"

# Start scene
STR_NEW_GAME = "Joc nou"
STR_LOAD_GAME = "Incarcare salvare"
STR_OPTIONS = "Optiuni"
STR_EXIT_GAME = "Iesi din joc"

# Close button
STR_CLOSE = "Inchidere"

# Load game menu
STR_LOAD_GAME_MENU = "Incarcare salvare"


def f_SAVE_NUMBER(serial_number: int):
    return f"Arhiva {serial_number}"


# Options menu
STR_OPTIONS_MENU = "Optiuni"
STR_LANGUAGE_ = "Limba:"
STR_LANGUAGE = "Limba"
STR_CHOOSE_LANGUAGE = "Alege o limba"
STR_MOVE_SPEED_ = "Viteza de miscare:"
STR_SCREEN_MODE_ = "Mod ecran:"
STR_NORMAL = "Normal"
STR_FAST = "Rapid"
STR_SLOW = "Lent"
STR_WINDOW = "Fereastra"
STR_FULL = "Ecran complet"

# Save game menu
STR_SAVE_GAME_MENU = "Salveaza jocul"


# Level loading scene
def f_CHAPTER_NUMBER(number: int):
    return f"Nr {number} Capitol"


def f_LEVEL_NUMBER_AND_NAME(number: int, name: str):
    return f"Nr {number} Închide: {name}"


# Main menu
STR_MAIN_MENU = "Meniu principal"
STR_SAVE = "Salveaza jocul"
STR_SUSPEND = "Pauza"
STR_START = "Start"
STR_DIARY = "Jurnal"
STR_END_TURN = "Urmatoarea miscare"
STR_DEFAULT_DIARY_BODY_CONTENT = "Niciun event nu a fost inregistrat"


# Reward menu
STR_REWARD_CONGRATULATIONS = "Felicitari! Obiectivul misiunii a fost indeplinit!"


def f_EARNED_GOLD(gold: int):
    return f"Obtineti monede de aur: {gold} (Toate personajele)"


def f_EARNED_ITEMS(item):
    return f"Obtineti lucruri: {item}"


# Player menu
STR_INVENTORY = "Inventar"
STR_EQUIPMENT = "Echipament"
STR_STATUS = "Status"
STR_WAIT = "Asteapta"
STR_VISIT = "Viziteaza"
STR_TRADE = "Troc"
STR_OPEN_CHEST = "Deschide cufarul"
STR_PICK_LOCK = "Sparge lacatul"
STR_OPEN_DOOR = "Deschide usa"
STR_USE_PORTAL = "Intra în portal"
STR_DRINK = "Bea"
STR_TALK = "Vorbeste"
STR_TAKE = "Ia"
STR_ATTACK = "Ataca"
STR_SELECT_AN_ACTION = "Alege o actiune"

# Inventory menu
STR_SHOPPING_SELLING = "Vinde - Cumpara"  # "Shop - Selling"


def f_UR_GOLD(gold):
    return f"Aurul tau: {gold}"  # f"Your gold: {gold}"

def f_SHOP_GOLD(shop_balance):
    return f"Negustor de aur: {shop_balance}"


# Trade menu
STR_50G_TO_RIGHT = "50 monede de aur ->"  # "50G ->"
STR_200G_TO_RIGHT = "200 monede de aur ->"
STR_ALL_TO_RIGHT = "Toate monedele de aur ->"
STR_50G_TO_LEFT = "<- 50 aur"
STR_200G_TO_LEFT = "<- 200 aur"
STR_ALL_TO_LEFT = "<- Toate monedele de aur"


def f_GOLD_AT_END(player, gold):
    return f"{player} monede de aur: {gold}"  # f"{player}'s gold: {gold}"


# Status menu
STR_NAME_ = "Nume:"  # "Name :"
STR_SKILLS = "Skill:"  # "SKILLS"
STR_CLASS_ = "Tip:"  # "Class :"
STR_RACE_ = "Rasa:"  # "Race :"
STR_LEVEL_ = "Nivel:"  # "Level :"
STR_XP_ = "Experientă:"  # "  XP :"
STR_STATS = "Statistici:"  # "STATS"
STR_HP_ = "Viata:"  # "HP :"
STR_MOVE_ = "Miscare:"  # "MOVE :"
STR_CONSTITUTION_ = "Constitutie:"  # "CONSTITUTION :"
STR_ATTACK_ = "Atac:"  # "ATTACK :"
STR_DEFENSE_ = "Aparare:"  # "DEFENSE :"
STR_MAGICAL_RES_ = "Rezistenta la magie:"  # "MAGICAL RES :"
STR_ALTERATIONS = "Alteratii:"  # "ALTERATIONS"
STR_NONE = "Niciuna"  # "None"


def f_DIV(partial, maximum):
    return f"{partial} / {maximum}"


# Item shop menu
STR_BUY = "Cumpara"
STR_INFO = "Informatii"

# Item buy menu
STR_SHOP_BUYING = "Magazin - Cumpara"


def f_PRICE_NUMBER(price):
    return f"Pret: {price}"  # f"Price: {price}"


def f_QUANTITY_NUMBER(quantity):
    return f"Cantitate:{quantity}"


# Item sell menu
STR_SELL = "Vinde"  # "Sell"

# Item menu
STR_THROW = "Arunca"  # Throw
STR_USE = "Foloseste"  # Use
STR_UNEQUIP = "Dezechipeaza"
STR_EQUIP = "Echipeaza"


# Item description stat
def f_STAT_NAME_(stat_name):
    return f"{stat_name}:"  # f"{stat_name}: "


# Item description menu
STR_RESERVED_TO = "Rezervat"  # "RESERVED TO"
STR_POWER = "Putere"  # "POWER"
STR_DEFENSE = "Aparare"  # "DEFENSE"
STR_MAGICAL_RES = "Rezistentă la magie"  # "MAGICAL RES"
STR_TYPE_OF_DAMAGE = "Tipul de damage"  # "TYPE OF DAMAGE"
STR_REACH = "Distanta de atac"  # "REACH"
STR_EFFECT = "Efect"  # "EFFECT"
STR_STRONG_AGAINST = "Puternic impotriva"  # "STRONG AGAINST"
STR_PARRY_RATE = "Rata de blocare"  # "PARRY RATE"
STR_DURABILITY = "Durabilitate"  # "DURABILITY"
STR_WEIGHT = "Masa"  # "WEIGHT"

# Status entity menu
STR_LOOT = "Loot"  # "LOOT"
STR_TYPE_ = "Tip:"  # "TYPE :"
STR_REACH_ = "Distanta de atac:"  # "REACH :"


def f_LEVEL_NUMBER_ENTITY(level):
    return f"Nota:{level}"  # f"LEVEL : {level}"


# Sidebar
STR_FOE = "Inamic"  # "FOE"
STR_PLAYER = "Jucator"  # "PLAYER"
STR_ALLY = "Aliat"  # "ALLY"
STR_UNLIVING_ENTITY = "Entitate neinsufletita"  # "UNLIVING ENTITY"
STR_NAME_SIDEBAR_ = "Nume:"  # "NAME : "
STR_ALTERATIONS_ = "Schimbare:"  # "ALTERATIONS : "


def f_TURN_NUMBER_SIDEBAR(number_turns):
    return f"Nr {number_turns} miscari"  # f"TURN {number_turns}"


def f_LEVEL_NUMBER_SIDEBAR(level_id):
    return f"Nr {level_id} Inchide"  # f"LEVEL {level_id}"


# Chest menu
STR_CHEST = "Cufar"  # "Chest"


# Alternation info menu
def f_TURNS_LEFT_NUMBER(turns_left):
    return f"Numarul de miscari ramase:{turns_left}"


# Ask save menu
STR_SAVE_THE_GAME_ = "Salvezi jocul?"
STR_YES = "Da"
STR_NO = "Nu"


# src.game_entities.building
def f_YOU_RECEIVED_NUMBER_GOLD(gold):
    return f"[Ai{gold}aur]"


def f_YOU_RECEIVED_ITEM(item):
    return f"[Ai {item}]"


# Messages
STR_ERROR_NOT_ENOUGH_TILES_TO_SET_PLAYERS = (
    "Eroare! Nu este suficient spatiu pe harta pentru a plasa jucatorii..."  # "Error ! Not enough free tiles to set players..."
)
STR_GAME_HAS_BEEN_SAVED = "Jocul a fost salvat"  # "Game has been saved"
STR_ITEM_HAS_BEEN_ADDED_TO_UR_INVENTORY = (
    "Obiectul a fost pus in rucsac"  # "Item has been added to your inventory"
)
STR_YOU_FOUND_IN_THE_CHEST = "Ai gasit in cutie"  # "You found in the chest"
STR_DOOR_HAS_BEEN_OPENED = "Usa a fost deschisa"  # "Door has been opened"
STR_YOU_HAVE_NO_FREE_SPACE_IN_YOUR_INVENTORY = (
    "Nu mai ai loc în inventar"  # "You have no free space in your inventory"
)
STR_STARTED_PICKING_ONE_MORE_TURN_TO_GO = (
    "Ai inceput sa spargi lacatul, inca o runda si se termina"  # "Started picking, one more turn to go"
)
STR_THERE_IS_NO_FREE_SQUARE_AROUND_THE_OTHER_PORTAL = (
    "Cealalta parte a portalului este blocata"  # "There is no free square around the other portal"
)
STR_BUT_THERE_IS_NOT_ENOUGH_SPACE_IN_INVENTORY_TO_TAKE_IT = (
    "Dar nu este suficient loc in inventar pentru asta!"  # But there is not enough space in inventory to take it!"
)
STR_YOU_HAVE_NO_KEY_TO_OPEN_A_DOOR = "Nu ai cheia de la usa"  # "You have no key to open a door"
STR_YOU_HAVE_NO_KEY_TO_OPEN_A_CHEST = "Nu ai cheia de la cufar"  # "You have no key to open a chest"
STR_ITEM_HAS_BEEN_TRADED = "Obiectul a fost schimbat"  # "Item has been traded"
STR_ITEM_HAS_BEEN_THROWN_AWAY = "Obiectul a fost aruncat"  # "Item has been thrown away"
STR_THE_ITEM_CANNOT_BE_UNEQUIPPED_NOT_ENOUGH_SPACE_IN_UR_INVENTORY = "Nu se poate elimina obiectul, nu ai suficient spațiu în inventar"  # "The item can't be unequipped : Not enough space in your inventory."
STR_THE_ITEM_HAS_BEEN_UNEQUIPPED = "Obiectul a fost eliminat"  # "The item has been unequipped"
STR_THE_ITEM_HAS_BEEN_EQUIPPED = "Articolul este echipat"  # "The item has been equipped"
STR_PREVIOUS_EQUIPPED_ITEM_HAS_BEEN_ADDED_TO_YOUR_INVENTORY = (
    "Obiectul echipat anterior a fost pus in inventar"  # "Previous equipped item has been added to your inventory"
)
STR_THE_ITEM_HAS_BEEN_BOUGHT = "Obiectul a fost cumparat"
STR_NOT_ENOUGH_SPACE_IN_INVENTORY_TO_BUY_THIS_ITEM = "Nu exista suficient spatiu in inventar pentru a cumpara acest obiect"
STR_NOT_ENOUGH_GOLD_TO_BY_THIS_ITEM = "Nu exista suficient aur pentru a cumpara acest obiect"
STR_THE_ITEM_HAS_BEEN_SOLD = "Obiectul a fost vandut"
STR_THIS_ITEM_CANT_BE_SOLD = "Acest obiect nu poate fi vandut"
STR_THIS_HOUSE_SEEMS_CLOSED = "Aceasta casa pare inchisa"


def f_ATTACKER_ATTACKED_TARGET_BUT_PARRIED(attacker, target):
    return f"{attacker}Atacat{target}...dar{target}s-a ferit"  # f"{attacker} attacked {target}... But {target} parried!"


def f_ATTACKER_DEALT_DAMAGE_TO_TARGET(attacker, target, damage):
    return f"{attacker}Da{target}cauzat{damage}rani"  # f"{attacker} dealt {damage} damage to {target}"


def f_TARGET_DIED(target):
    return f"{target}a murit!"  # f"{target} died!"


def f_TARGET_DROPPED_ITEM(target, item):
    return f"{target}lasat{item}"  # f"{target} dropped {item}"


def f_TARGET_HAS_NOW_NUMBER_HP(target, hp):
    return f"{target}are{hp}HP"  # f"{target} has now {hp} HP"


def f_ATTACKER_EARNED_NUMBER_XP(attacker, experience):
    return f"{attacker}a primit{experience}experienta"  # f"{attacker} earned {experience} XP"


def f_ATTACKER_GAINED_A_LEVEL(attacker):
    return f"{attacker}a crescut cu un nivel"  # f"{attacker} gained a level!"


def f_ITEM_CANNOT_BE_TRADED_NOT_ENOUGH_PLACE_IN_RECEIVERS_INVENTORY(receiver):
    return f"Nu se poate finaliza trocul:{receiver}Nu este suficient spatiu in inventar"  # f"Item can't be traded: not enough place in {receiver}'s inventory"


def f_THIS_ITEM_CANNOT_BE_EQUIPPED_PLAYER_DOESNT_SATISFY_THE_REQUIREMENTS(
    selected_player,
):
    return f"Acest obiect nu poate fi echipat:{selected_player}nu respecta cerintele"  # f"This item can't be equipped: {selected_player} doesn't satisfy the requirements"


# Constant sprites
STR_NEW_TURN = "Mutare noua !"
STR_VICTORY = "Victorie !"
STR_DEFEAT = "Infrangere !"
STR_MAIN_MISSION = "Misiune principala"
STR_OPTIONAL_OBJECTIVES = "Misiuni secundare"


# effect.py
def f_ENTITY_RECOVERED_NUMBER_HP(entity, recovered):
    return f"{entity}a recuperat{recovered}viata"  # f"{entity} recovered {recovered} HP."


def f_ENTITY_IS_AT_FULL_HEALTH_AND_CANT_BE_HEALED(entity):
    return (
        f"{entity}este la viata maximă posibilă si nu poate fi vindecat"  # f"{entity} is at full health and can't be healed!"
    )


def f_ENTITY_EARNED_NUMBER_XP(entity, power):
    return f"{entity}A primit{power}experienta"  # f"{entity} earned {power} XP"


def f_ENTITY_GAINED_A_LEVEL(entity):
    return f"。{entity}a crescut cu un nivel"  # f". {entity} gained a level!"


def f_THE_SPEED_OF_ENTITY_HAS_BEEN_INCREASED_FOR_NUMBER_TURNS(entity, duration):
    return f"{entity}are viteza {duration}mutari"  # f"The speed of {entity} has been increased for {self.duration} turns"


def f_THE_STRENGTH_OF_ENTITY_HAS_BEEN_INCREASED_FOR_NUMBER_TURNS(entity, duration):
    return f"{entity}i-a crescut puterea cu{duration}mutari"  # f"The strength of {entity} has been increased for {self.duration} turns"


def f_THE_DEFENSE_OF_ENTITY_HAS_BEEN_INCREASED_FOR_NUMBER_TURNS(entity, duration):
    return f"Lui{entity}i-a crescut apararea cu{duration}mutari"  # f"The defense of {entity} has been increased for {self.duration} turns"


def f_ENTITY_HAS_BEEN_STUNNED_FOR_NUMBER_TURNS(entity, duration):
    return (
        f"{entity}a fost blocat pentru{duration}mutari"  # f"{entity} has been stunned for {duration} turns"
    )


def f_RECOVER_NUMBER_HP(power):
    return f"Recupereaza{power}viata"  # f"Recover {power} HP"


def f_EARN_NUMBER_XP(power):
    return f"Obtine{power}experienta"  # f"Earn {power} XP"


TRANSLATIONS = {
    "items": {
        "key": "cheie",
        "bones": "oase",
        "topaz": "topaz",
        "iron_ring": "inel de fier",
        "monster_meat": "carne de monstru",
        "life_potion": "potiune de viata",
        "speed_potion": "potiune de viteza",
        "rabbit_step_potion": "potiune de picior de iepure",
        "strength_potion": "potiune de putere",
        "vigor_potion": "potiune de vigoare",
        "scroll_of_knowledge": "pergamentul cunoasterii",
        "scroll_of_cerberus": "pergamentul lui cerberus",
        "chest_key": "cheie pentru cufar",
        "door_key": "cheie pentru usa",
        "green_book": "carte verde",
        "poket_knife": "briceag",
        "dagger": "pumnal",
        "club": "bata",
        "short_sword": "sabie scurta",
        "wooden_spear": "sulita de lemn",
        "halberd": "halebarda",
        "pickaxe": "tarnacop",
        "wooden_bow": "arc de lemn",
        "basic_bow": "arc",
        "wooden_staff": "toiag din lemn",
        "necromancer_staff": "toiag de vrajitor",
        "plumed_helmet": "casca cu pene",
        "black_hood": "gluga neagra",
        "helmet": "coif",
        "horned_helmet": "coif cu coarne",
        "gold_helmet": "coif de aur",
        "chainmail": "armura de zale",
        "leather_armor": "armura de piele",
        "scale_mail": "arumura de solzi",
        "gold_armor": "armura de aur",
        "spy_outfit": "tinuta de spion",
        "barding_magenta": "armura de cal",
        "brown_boots": "ghete maro",
        "black_boots": "ghete negre",
        "gold_boots": "ghete de aur",
        "wooden_shield": "scut de lemn",
        "pocket_knife": "briceag",
        "basic_spear": "sulita",
        "basic_halberd": "halebarda",
    },
    "effects": {
        "defense_up": "mai multa aparare",
        "strength_up": "mai multa putere",
        "speed_up": "mai multa viteza",
        "stun": "blocat",
        "no_attack": "fara atacuri",
    },
    "alterations": {
        "defense_up": "mai multa aparare",
        "strength_up": "mai multa putere",
        "speed_up": "mai multa viteza",
        "stun": "blocat",
        "no_attack": "fara atacuri",
    },
    "races_and_classes": {
        # Races
        "human": "on",
        "elf": "elf",
        "dwarf": "pitic",
        "centaur": "centaur",
        "gnome": "gnom",
        # Classes
        "warrior": "razboinic",
        "ranger": "padurar",
        "spy": "spion",
    },
    "foe_keywords": {
        "undead": "strigoi",
        "large": "mare",
        "cavalry": "cavalerie",
        "mutant": "mutant",
        "fly": "zburator",
        "none": "niciunul",
    },
    "entity_names": {
        "skeleton": "schelete",
        "skeleton_cobra": "schelete cobra",
        "necrophage": "strigoi",
        "lich_boss": "stapanul lich",
        "mutant_bee": "albina mutanta",
        "mutant_lizard": "soparla mutanta",
        "mutant_cultist": "cultist mutant",
        "mutant_ant": "furnica mutanta",
        "obstacle": "obstacol",
        "shop": "magazin",
        "house": "casa",
        "chest": "cufar",
        "healer": "vindecator",
        "tavern": "taverna",
        "door": "usa",
        "altar": "altar",
        "armory": "arsenal",
        "apothecary": "farmacista",
    },
    "attack_kinds": {
        "physical": "fizic",
        "spiritual": "spiritual",
    },
}
