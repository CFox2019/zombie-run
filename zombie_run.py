import time
import random

you_dead = """
          _______           _  _______  _______
|\\     /|(  ___  )|\\     /|( )(  ____ )(  ____ \\
( \\   / )| (   ) || )   ( ||/ | (    )|| (    \\/
 \\ (_) / | |   | || |   | |   | (____)|| (__
  \\   /  | |   | || |   | |   |     __)|  __)
   ) (   | |   | || |   | |   | (\\ (   | (
   | |   | (___) || (___) |   | ) \\ \\__| (____/\\
   \\_/   (_______)(_______)   |/   \\__/(_______/
 ______   _______  _______  ______   _
(  __  \\ (  ____ \\(  ___  )(  __  \\ ( )
| (  \\  )| (    \\/| (   ) || (  \\  )| |
| |   ) || (__    | (___) || |   ) || |
| |   | ||  __)   |  ___  || |   | || |
| |   ) || (      | (   ) || |   ) |(_)
| (__/  )| (____/\\| )   ( || (__/  ) _
(______/ (_______/|/     \\|(______/ (_)
"""

you_win = """
          _______                     _________ _        _
|\\     /|(  ___  )|\\     /|  |\\     /|\\__   __/( (    /|( )
( \\   / )| (   ) || )   ( |  | )   ( |   ) (   |  \\  ( || |
 \\ (_) / | |   | || |   | |  | | _ | |   | |   |   \\ | || |
  \\   /  | |   | || |   | |  | |( )| |   | |   | (\\ \\) || |
   ) (   | |   | || |   | |  | || || |   | |   | | \\   |(_)
   | |   | (___) || (___) |  | () () |___) (___| )  \\  | _
   \\_/   (_______)(_______)  (_______)\\_______/|/    )_)(_)
"""

weapons = [
    "pair of scissors",
    "safety pin",
    "pen",
    "butter knife",
    "steak knife",
    "bouncy ball",
    "pistol",
    "shot gun",
    "bazooka",
    "machete"
]

actions = [
    "serenading",
    "attacking",
    "boxing",
    "wrestling",
    "drop kicking",
    "karate chopping",
    "yelling at",
    "petting",
    "spitting on",
    "barfing on"
]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return option
        print_pause("Sorry, that's not a valid response!")


def intro():
    print_pause("You have just woken up to an "
                "eerie noise outside of your house.")
    print_pause("You decide to look outside to see if you can tell where "
                "the noise is coming from.")
    print_pause("As soon as you open your front door, you see zombies "
                "walking around in all directions!")


def stay_or_go(weapon=None):
    if weapon is None:
        continue_without_weapon()
    else:
        continue_with_weapon(weapon)


def continue_with_weapon(weapon):
    prompt = "\nWhat do you do?!?!" \
             "\nYour options are:" \
             f"\n'go' - to make a mad dash for your car with your {weapon}" \
             "\n-or-" \
             "\n'stay' - to shut the door and try to find a better weapon\n"
    response = valid_input(prompt, ["stay", "go"])
    if response == 'go' and weapon == 'machete':
        you_survived()
    else:
        if "go" in response:
            death_sequence(weapon)
        elif "stay" in response:
            print_pause("You choose to shut the front door and find a weapon.")
            room_of_choice()


def continue_without_weapon():
    prompt = "\nWhat do you do?!?!" \
             "\nYour options are:" \
             "\n'go' - to make a mad dash for your car" \
             "\n-or-" \
             "\n'stay' - to shut the door and find a weapon\n"
    response = valid_input(prompt, ["stay", "go"])
    if "go" in response:
        death_sequence()
    elif "stay" in response:
        print_pause("You choose to shut the front door and find a weapon.")
        room_of_choice()


def death_sequence(weapon=None):
    if weapon is not None:
        print_pause(f"You grab your car keys, your {weapon}, and make "
                    "a mad dash for your car, sprinting across the lawn, "
                    f"{random.choice(actions)} and "
                    f"{random.choice(actions)} zombie after zombie.")
        print_pause("You are quickly overrun by zombies and your last "
                    "dying thought is, \"I should have found a better "
                    "weapon!\"")
    else:
        print_pause("You grab your car keys and make a mad dash for your car, "
                    "sprinting across the lawn, dodging zombie after zombie.")
        print_pause("You finally make it to your car, safely.")
        print_pause("You get inside and start the engine, when SMASH!!! a "
                    "zombie breaks through the drivers side window and eats "
                    "your brains!")
    print_pause(you_dead)


def room_of_choice():
    prompt = "\nWhere do you want to go?" \
             "\nYour options are:" \
             "\n'bedroom'" \
             "\n-or-" \
             "\n'kitchen'" \
             "\n-or-" \
             "\n'garage'\n"
    response = valid_input(prompt, ["bedroom", "kitchen", "garage"])
    weapon = random.choice(weapons)
    print_pause(f"You find a {weapon} in your {response} and head for the "
                "front door.")
    print_pause("You arrive at the front door and suddenly realize you may "
                "be able to find a better weapon.")
    stay_or_go(weapon)


def you_survived():
    print_pause("You hack all the surrounding zombies in their brains and "
                "escape in your car, never seeing another zombie again!")
    print_pause(you_win)


def play_again():
    response = valid_input("Would you like to play again?\n"
                           "Please say 'yes' or 'no'.\n", ["yes", "no"])
    if "no" in response:
        print_pause("Thanks for playing!")
    elif "yes" in response:
        print_pause("Great! Good luck defeating the zombies!")
        zombie_run()


def zombie_run():
    intro()
    stay_or_go()
    play_again()


zombie_run()
