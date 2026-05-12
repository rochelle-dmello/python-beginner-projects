print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("This is a game that depends on your actions. \nYou will be provided with several paths. \nPress '1' or '2' or '3'for the respective action.\n")
input("\nPress Enter to continue...")

input("\nRemember")
input("Every choice matters.\n")

input("\nYou find yourself stranded on an island with nothing but a paper in your hand.\nThe paper reads:\n")
print("Ahoy… lost soul. \n"
      "Ye’ve wandered far from yer path, and the sea don’t take kindly to the aimless.\n"
      "If ye long to see yer kin again, ye’ll have to earn it—by findin’ the treasure I’ve buried deep.\n"
      "Sail on ahead, and the path shall grow clearer with each step ye take\n"
      "proof that yer headin’ true."
      "but stray, and the dark will swallow ye whole. \n"
      "Mark me words,this be no gentle voyage.\n"
      "Bring me treasure ‘fore the sun rises o’er the horizon, and perhaps… just perhaps… \n"
      "I’ll spare ye, and share what spoils I see fit.\n"
      "Fail… and the sea will claim ye. Forever. \n"
      "Choose wisely… and may fortune favor ye.\n")


choice1 =int(input("\nWould you like to north (to the mountains)? or south(towards the ocean)?: "))
if choice1 == 1:
    input("You start walking towards the mountains.")
    input("As you observe your surroundings, you can't really see much ahead.\nThe forest seems to be very dense.")
    input("You hear some rustling around the area but you're too tired to investigate any further.\nYou assume it's just some animal and focus on your trail.")
    input("Soon, your legs start aching, but you persist, thinking about the treasure and a good night's sleep which you hope will come soon.")
    input("Suddenly")
    input("You feel a hand cover your mouth")
    input("Before you could realise what is going on...")
    input("Everything goes dark and you lose consciousness.")
    input("You wake up to a jabbing pain in your head")
    input("You open your eyes to see everything horizontal.")
    input("And a group of people singing and dancing.")
    input("Suddenly you feel immense heat all over.")
    input("At first you thought it was just because they kept you close to the fire, so you try to move.")
    input("Plus, you can't seem to bend your elbows or knees.")
    input("But the pain sharpened. It was hot, too hot.")
    input("The warmth suddenly turned into a biting, sharp, gnawing pain, taking control of your entire skin.")
    input("You look down and that's when it hit you.")
    input("The flames weren't near you, they were ON you.")
    input("You try to scream but realise there's an apple stuck in between your jaw.")
    input("You pray for some miracle as you're being roasted on a bonfire by a tribe that believes you were an offering from the gods for a feast.")
    input("But your prayers weren't loud enough.")
    print("GAME OVER. TRY AGAIN.")

elif choice1 ==2:
    input("You run towards the shore feeling happy about the treasure you're about to get and ofcourse, going home.")
    input("Straight ahead, You see the other end of the shore with something sparkly catching your eye. ")
    input("You hope you made the right choice.")
    input("As you look around, you can't seem to find a boat.")

    choice2=int(input("Are you confident enough to swim? or Do you wait for a boat?: "))
    if choice2 == 1:
        input("You believe that you're a pretty good swimmer and could put your muscles to use.")
        input("The first few minutes flow by like a breeze.")
        input('So you stop for a minute to locate the other end of the shore.')
        input("But to your horror, it has disappeared.")
        input("You feel your stomach drop as you realise that you made the wrong choice.")
        input("Without a second thought, you turn around to go back to the shore you came from.")
        input("But that has seemed to vanish as well.")
        input("You feel the waves grow bigger and bigger as you keep moving your arms in a pathetic attempt to survive.")
        input("Out of no where, a huge wave comes and consumes you whole.")
        input("You try your best to fight it, but it was stronger.")
        input("Your screams get engulfed by the wave and you're arms stop moving...")
        input("...As you sink in slowly.")
        print("GAME OVER")

    elif choice2 == 2:
        input("You sit under a tree to wait for a boat.")
        input("Your muscles are sore and your eyelids feel heavy")
        input("Probably from trying to survive whatever led you to the shore.")
        input("So you decide to close you're eyes and rest for a while.")
        input("...")
        input("...")
        input("...")
        input("By the time you wake up, You don't feel the heat of the sun anymore.")
        input("As you look at the stars twinkle in the sky you realise you are supposed to find the treasure by sunrise.")
        input("You look around to see if you can spot any boat.")
        input("And Aha!")
        input("You see a wooden boat right on the shore.")
        input("You assume the Lord of the Sea heard your prayers and sit in the boat to go to the other end of the shore.")
        input("You look down in the boat to see fruits and knifes around.")
        input("You also seem to hear a group of people party and yell something about a 'Big Feast'.")
        input("Even though your stomach hasn't stopped rumbling for a while,")
        input("You don't have time to waste and can eat whatever you want with the treasure you get.")
        input("And you sail away...")
        input("As you see a bit of light near the horizon, you start rowing faster.")
        input("And you soon,reach the other end.")

        print("Right on the shore, you see Three Doors.\n")
        choice3=int(input("Red, Yellow, and Blue\nWhich do you choose? "))
        if choice3 == 1:
            input("You twist the knob on the Bright Red Door, A little worried about your decision.")
            input("But as soon as you open the door, you see a pride of starving lions.")
            input("Without a second thought. You sprint for your life.")
            input("But the sand slows you down, as you hear the roars get louder.")
            input("The Lions were hungrier than your will to live.")
            print("GAME OVER.")

        elif choice3 == 2:
            input("You have a gut feeling that you mad the right decision and are ecstatic to open Yellow the door.")
            input("Without looking down you take a step and you feel your heart drop.")
            input("....")
            input("....")
            input("...?")
            input("..??")
            input("????")
            input("???!")
            input("!!!!")
            input("You're falling into what looks like a bottomless pit!?!?!?!?!?!?!")
            input("And you fall")
            input("And you fall")
            input("You can't stop falling")
            input("Not knowing what to do, you start screaming.")
            input("You don't know what your fate is.")
            input("This could either never end or you would hit the ground and bleed to death.")
            input("And you don't know what's scarier")
            input("But for now, you have no choice but to wait.")
            print("GAME OVER")

        elif choice3 == 3:
            input("A little anxious with your decision, you open the blue door.")
            input("You enter a dark room and see a huge chest twinkling, a little far away.")
            input("Overcome with happiness, you run towards it.")
            input("You try to open it but can't.")
            input("You try to find a lock, a code, a key, anything,but can't.")
            input("All of a sudden you hear a loud")
            input("THUD!")
            input("behind you.")
            input("You turn around to see another door.")
            input("At this point, you have nothing to lose so you open it.")
            input("You smell a scent that's a little too familiar.")
            input("As your eyes adjust to the brightness, you realise you are back in your room again.")
            input("Confused, You find a little note that says: ")
            input("'Did ye mighty believe a pirate would share thar hard earned treasure?\nBe grateful dat I didn' make yer me slave.\nFair winds t' ye'\n")
            print("Thank you for Playing!")
        else:
            print("Wrong input. Remember you can only press '1' or '2' or '3' to choose.Try Again.")
    else:
        print("Wrong input. Remember you can only press '1' or '2' to choose. Try again.")

else:
    print("Wrong input. Remember you can only press '1' or '2' to choose. Try again.")
