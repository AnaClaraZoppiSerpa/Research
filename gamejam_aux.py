import sys
import time
from getkey import getkey, keys

class Colors:
    def __init__(self):
        self.Black = "\u001b[30m"
        self.Red = "\u001b[31m"
        self.Green = "\u001b[32m"
        self.Yellow = "\u001b[33m"
        self.Blue = "\u001b[34m"
        self.Magenta = "\u001b[35m"
        self.Cyan = "\u001b[36m"
        self.White = "\u001b[37m"
        self.Reset = "\u001b[0m"

colors = Colors()

caught_flies = False

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./100)

def customized_print(text, color = "", slow = False):
    string = color + text + colors.Reset
    if slow:
        slowprint(string)
    else:
        print(string)

class Creature:
    def __init__(self, name, art, color, interaction_function):
        self.name = name
        self.art = art
        self.color = color
        self.interaction_function = interaction_function
    
    def appear(self):
        customized_print(self.art, self.color, True)
    
    def interact(self):
        self.interaction_function()

def froggo_interaction():
    speech1 = [
        f"Ribbit, ribbit! {colors.Cyan}(press n to continue the conversation){colors.Reset}",
        f"Oh, hello there! Fancy seeing you here, ribbit.",
        f"I hadn't seen humans here in a while.",
        f"Actually haven't seen any other form of life.",
        f"Not even flies...",
        f"They used to taste so good. I miss them so much.",
        f"If you see any flies around, can you bring them to me?",
    ]

    curr_speech = 0
    print(speech1[curr_speech])
    while True:
        if curr_speech == len(speech1) - 1:
            break
        key = getkey()
        if key == 'n':
            curr_speech += 1
            print(speech1[curr_speech])

    print("")
    print(f"> Sorry, I haven't seen any flies either. {colors.Cyan}(enter 1){colors.Reset}")
    print(f"> I see. Sounds though. I'll try finding some. {colors.Cyan}(enter 2){colors.Reset}")
    print(f"> So that you eat them?!! No way! Never! {colors.Cyan}(enter 3){colors.Reset}")

    if caught_flies:
        print(f"> I have some with me. Here, take them. {colors.Cyan}(enter 4){colors.Reset}")

    answer = int(getkey())

    print("")

    if answer == 1:
        speech2 = [
        f"I see. {colors.Cyan}(press n to continue){colors.Reset}",
        f"Well, it's a pity. Anyways, I wish you a good journey, human.",
        ]

        curr_speech = 0
        print(speech2[curr_speech])
        while True:
            if curr_speech == len(speech2) - 1:
                break
            key = getkey()
            if key == 'n':
                curr_speech += 1
                print(speech2[curr_speech])

    if answer == 2:
        speech3 = [
        f"Oh!!! Really? {colors.Cyan}(press n to continue){colors.Reset}",
        f"{colors.Red}<3 <3 <3 <3 <3 <3 <3 <3{colors.Reset}",
        f"{colors.Red}THANK YOU SO MUCH!{colors.Reset}",
        ]

        curr_speech = 0
        print(speech3[curr_speech])
        while True:
            if curr_speech == len(speech3) - 1:
                break
            key = getkey()
            if key == 'n':
                curr_speech += 1
                print(speech3[curr_speech])

    if answer == 3:
        speech4 = [
        f"Sheesh... No need to be so rude. {colors.Cyan}(press n to continue){colors.Reset}",
        f"What if you were starving? Would you like me to deny you a piece of meat?!",
        f"It's not my fault if I need to eat flies...",
        f"Ribbit...",
        f"*sad ribbit noises*",
        ]

        curr_speech = 0
        print(speech4[curr_speech])
        while True:
            if curr_speech == len(speech4) - 1:
                break
            key = getkey()
            if key == 'n':
                curr_speech += 1
                print(speech4[curr_speech])
    
    if answer == 4:
        if caught_flies:
            speech5 = [
            f"OOOOOOOHHHHH!!!! {colors.Cyan}(press n to continue){colors.Reset}",
            f"THANKS!!!",
            f"They're... They're...",
            f"{colors.Red}DELICIOUS!!!{colors.Red}",
            f"*happy ribbit noises*",
            ]

            curr_speech = 0
            print(speech5[curr_speech])
            while True:
                if curr_speech == len(speech5) - 1:
                    break
                key = getkey()
                if key == 'n':
                    curr_speech += 1
                    print(speech5[curr_speech])
        else:
            slowprint("[You've successfully used a cheat code.]")
            slowprint("[How did you know?]")
            slowprint("[Anyways, you've hacked the game! Congratulations!]")
            slowprint("!!!!!!!!!")
            customized_print(cake_art, colors.Yellow, True)
            slowprint(f"{colors.Magenta}[Interdimensional cake added to inventory.]{colors.Reset}")
            slowprint("You majestically leave the interdimensional maze with your cake.")
            slowprint("T h e  E n d ! ! !")
            exit()

    
    print(f"{colors.Cyan}(press n to go back to the map){colors.Reset}")
    while True:
        key = getkey()
        if key == 'n':
            print("")
            break

cake_art = '''
          *                                             *
                                               *
                    *
                                  *
                                                            *
         *
                                                  *
             *
                           *             *
                                                     *
      *                                                               *
               *
                               (             )
                       )      (*)           (*)      (
              *       (*)      |             |      (*)
                       |      |~|           |~|      |          *
                      |~|     | |           | |     |~|
                      | |     | |           | |     | |
                     ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
              ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
             a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
             ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
             ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
             ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
             ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
             ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
             ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
             ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
         ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
      .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
     .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
     %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
     %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
     `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
       `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
           `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                  """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                 `%%%%%%%'
                                  `%%%%%'
                                    %%%                 
                                   %%%%%
                                .,%%%%%%%,.
                           ,%%%%%%%%%%%%%%%%%%%,
'''

froggo_art = """
        ,-.___.-.
     ,-.(|)   (|),-.
     \_*._ ' '_.* _/
      /`-.`--' .-'\\
 ,--./    `---'    \,--.
 \   |(  )     (  )|   /
  \  | ||       || |  /
   \ | /|\     /|\ | /
   /  \-._     _,-/  \\
  //| \\  `---'  // |\\
 /,-.,-.\       /,-.,-.\\
o   o   o      o   o    o
"""
froggo = Creature("Froggo", froggo_art, colors.Green, froggo_interaction)

def draggo_interaction():
    speech = [
        f"You see the legendary white eyes blue dragon. {colors.Cyan}(press n to continue){colors.Reset}",
        f"Blue eyes white dragon, I mean.",
        f"Uh... Not sure. I'm confused now.",
        f"Anyways.",
        f"It's a D R A G O N.",
        f"...",
        f"The dragon approaches you with a meaningful look.",
        f"And, suddenly...",
        f"The game ends with no explanation at all].",
        ]

    curr_speech = 0
    print(speech[curr_speech])
    while True:
        if curr_speech == len(speech) - 1:
            break
        key = getkey()
        if key == 'n':
            curr_speech += 1
            print(speech[curr_speech])

    customized_print("T h a n k s  f o r  p l a y i n g ~ uwu", colors.Cyan, True)
    exit()

doggo_art = """
    __    __
    \/----\/
     \0  0/    WOOF!
     _\  /_
   _|  \/  |_
  | | |  | | |
 _| | |  | | |_
"---|_|--|_|---"
"""

def doggo_interaction():
    print(f"You have found a {colors.Magenta}cute interdimensional doggo{colors.Reset}.")
    print(f"(Press n to pet it, press q to leave)")

    headpats = 1

    while True:
        key = getkey()
        if key == 'n':
            headpats *= 2
            print(f"Doggo headapts so far: {headpats} (n: more headpats, q: leave)")

            if headpats == 1024:
                slowprint(f"{colors.Red}(Interdimensional Doggo is very happy!!!){colors.Reset}")
            
            if headpats == 65536:
                slowprint(f"{colors.Red}(Interdimensional Doggo loves you){colors.Reset}")

        if key == 'q':
            break

doggo = Creature("Cute Doggo", doggo_art, colors.Cyan, doggo_interaction)

draggo_art = """
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
"""

draggo = Creature("Draggo", draggo_art, colors.Blue, draggo_interaction)

octo_art = """
                                              ,
                                            ,o
                                            :o
                   _....._                  `:o
                 .'       ``-.                \o
                /  _      _   \                \o
               :  /*\    /*\   )                ;o
               |  \_/    \_/   /                ;o
               (       U      /                 ;o
                \  (\_____/) /                  /o
                 \   \_m_/  (                  /o
                  \         (                ,o:
                  )          \,           .o;o'           ,o'o'o.
                ./          /\o;o,,,,,;o;o;''         _,-o,-'''-o:o.
 .             ./o./)        \    'o'o'o''         _,-'o,o'         o
 o           ./o./ /       .o \.              __,-o o,o'
 \o.       ,/o /  /o/)     | o o'-..____,,-o'o o_o-'
 `o:o...-o,o-' ,o,/ |     \   'o.o_o_o_o,o--''
 .,  ``o-o'  ,.oo/   'o /\.o`.
 `o`o-....o'o,-'   /o /   \o \.                       ,o..         o
   ``o-o.o--      /o /      \o.o--..          ,,,o-o'o.--o:o:o,,..:o
                 (oo(          `--o.o`o---o'o'o,o,-'''        o'o'o
                  \ o\              ``-o-o''''
   ,-o;o           \o \
  /o/               )o )
 (o(               /o /                |
  \o\.       ...-o'o /             \   |
    \o`o`-o'o o,o,--'       ~~~~~~~~\~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ```o--'''                       \| /
                                       |/
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                       |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



def octo_interaction():
    print("[octopus - to be implemented]")

octo = Creature("Octo", octo_art, colors.Blue, octo_interaction)

fly_art = '''
                                  _ " _
   _ " _                         (_\|/_)
  (_\|/_)  _ " _         _ " _    (/|\)
   (/|\)  (_\|/_) " _   (_\|/_)
           (/|\)_\|/_)   (/|\)
                (/|\)

'''

def fly_interaction():
    print("You see a bunch of interdimensional flies.")
    
    print("")
    print(f"> Capture them. {colors.Cyan}(enter 1){colors.Reset}")
    print(f"> Just leave. {colors.Cyan}(enter 2){colors.Reset}")
    print(f"> Try to talk to them. {colors.Cyan}(enter 3){colors.Reset}")

    answer = int(getkey())

    print("")

    if answer == 1:
        print(f"{colors.Blue}[Interdimensional flies were added to your inventory]{colors.Reset}")
        global caught_flies
        caught_flies = True

    if answer == 2:
        print("You simply leave.")

    if answer == 3:
        speech4 = [
        f"zzdhsjkdhjksaskhjdhsjksajhdhjkdhdjhhjksadhks. {colors.Cyan}(press n to continue){colors.Reset}",
        f"dhjkashkdjashdkash euddjkashdjjksdhhcjkjashjdd dsjhdhjkhdhkjsahjkds",
        f"djhashdhsadjhkashjkdkjhaskhd hkdhask",
        f"ebhdbwqhbewjhj hdjkashhjkds",
        f"(Apparently flies don't speak human :/)",
        ]

        curr_speech = 0
        print(speech4[curr_speech])
        while True:
            if curr_speech == len(speech4) - 1:
                break
            key = getkey()
            if key == 'n':
                curr_speech += 1
                print(speech4[curr_speech])
    
    print(f"{colors.Cyan}(press n to go back to the map){colors.Reset}")
    while True:
        key = getkey()
        if key == 'n':
            print("")
            break


fly = Creature("Fly", fly_art, colors.Yellow, fly_interaction)