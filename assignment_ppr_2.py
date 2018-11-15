#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:14:19 2018

@author: Philip
"""

"""
    Deliverables:
        
        - A working version of game in format: .py script
        
        - A game map (.pptx format), including:
            + Map of the game, including its intended user flow
            + locations of conditional statements
            + locations of loops
            + defined global variables (if any)
        
        - Working version of the game include:
            
            + An executable script including:
            + Game can be successfully completed in max 5 min
            
            …and at least:
                + 3 stages (maximum of 5 stages)
                + 2 defined variables
                + Easteregg
                + 1 loop
                + 1 nested conditional statement
                + 1 fail() function (whenever user loses the game)
                + A docstring at the beginning of game that:
                    + Is no more than 150 words
                    + Introduces the game and its purpose
                    + Identifies any bugs that are not yet worked out
"""

print("\f")

###################
# Introduction
###################

print("""
Introduction: 

Morpheus tells Neo about the real world, a ravaged wasteland
where most of humanity have been captured by a race of machines
who imprison their minds within an artificial reality...

...known as the MATRIX

His decision whether or not to find out about it 
is determined by the Pill(red or blue) he chooses. 

""")
    
input("< Press enter if you dare >")
print("\f")

###################
# Starting the narrative
###################

print("""
Pick wisely!

You take the blue pill—the exciting story ends,
you wake up in your bed and believe whatever you want to believe.

You take the red pill—you stay in Wonderland, 
and I show you how deep the rabbit hole goes.

""")
print("\f")

###################
# Decison timer (sec)
###################

seconds = int(input("How many seconds do you need to make a decision?\n> "))    
if seconds > 10:
    seconds = 10
    
import time

for i in range(seconds): 
    print(str(seconds - i) + " second(s) remaining")
    time.sleep(1) 
print("\f")

###################
# Choosing a Pill
###################

def choice_pill():
    
    print(""" 
Which pill are you deciding to take? 

[Input: Number min 1, max 2]
    
    1) Blue
    2) Red

""")
    input_1 = input(">  ")
    print("\f")
    
    if "1" in input_1:
        print("\nAlright, sissy, I hope you won't regret it.")
        input("< Press enter to continue your ordinary life >")
        print("\f")
       
        return choice_ord_life()
    
    elif "2" in input_1: 
        print("Oh, you are brave. Great choice. Let the journey begin.")
        
        input("< Press enter to dicovere the rabbit hole >") 
        print("\f")
        
        return matrix_1()
   
    else: 
        print("""
Please check your input. 
Valid: [Input: Number min 1, max 2]

""")
        choice_pill()  

###################
# BLUE Back to ordinary Job
###################

def choice_ord_life():
    print(""" 
You decided to step back into your normal life. 
Therefore, your ordinary 9 to 5 job continues. 

In short: 
Your boss enters your office and offers you a new project. 

[Input: Number min 1, max 3]

    1) Accept Project
    2) Reject Project 
    3) Trying to find Morpheus

""")
    input_2 = input(">  ") 
    print("\f")
    
    if "1" in input_2: 
        print("\f")
        
        print("""
You start realizing the workload exceeded your estimate
and are not able to catch up.

In order to get some clear thoughts, you leave your office
for some fresh air and you run into two mysterious looking men

    1) Man one
    2) Man two
        
""")
        
        
        while True:
            input_man = input("> [Input: Number min 1, max 2] \n ")
            if (input_man in "1" or input_man in "2"):
                break
        
        if "1" in input_man :
            print("\f")
            
            return dice()
        elif "2" in input_man:
            print("\f")
            
            print("\nWrong guy. He offers you drugs, you accept and commit suicide after years.")
            fail()

#Please check your input. 
#Valid: Numbers OR text


            
    elif "2" in input_2 : 
        print("\nCaused by your rejection, you are now unfortunately getting fired.")
        input("< Press enter to see what happens next >")
        print("\f")
        
        print("Sorry the game ends, you end up in a spiral of drugs and alcoholism.")
        fail()
    elif "3" in input_2 : 
        print("\nSmitty's Offer.")         

        return dice()        

    else:
        print("""
Please check your input. 
Valid: Numbers

""")
        choice_ord_life()
###################
# Dice Funktion
###################

def dice():
    print(""" 
          
A mysterious and suspicious looking guy names Smitty introduces himself.
He may know a way to find Morpheus.

Smitty sais:  
    
"Let's play Rolling the dice!
It will determine your fate.  Be careful tho." 

1, 2, 3 or 4        Game is Over
5 or 6              Surprise
 
Good luck.

""")
    input("< Press enter to role the dice >")
    print("\f")    
    
    import numpy as np
    np.random.seed()
    
    x = np.random.randint(1, 7)
    print("Your number is --> ", x)

    if x == 1 or x == 2:
        fail()
    
    elif x == 3 or x == 4: 
        fail()
    
    elif x == 5 or x == 6: 
        print("\nYou are lucky. Welcome to the Matrix.")
        input("< Press enter to discover the rabbit hole >")
        print("\f")
        
        return matrix_1()
    
        dice()
        
        
def matrix_1():
    print("""
Now that you have made it to the matrix I want you to choose a path
that helps foster- and substantiating the hypothesis of you being
...the chosen. 

Being Neo - the chosen - is accompanied by recurring sadistic decisions.
Here is another one.


    1) Starting the practice simulation
    2) Fighting the machines
    3) Following the woman in the red dress

[Input: Number min 1, max 3]

""")

    input_matrix_1 = input(">  ")
    print("\f")
    
    if input_matrix_1 is "1":
        print("""
You start your practice simulation.

You can choose between 2 different sparring partners. 
One is more advanced, one is less. 
More advanced practice partner equals more experience,
but also contains more risk of getting injured. 

    1) Agent Smith
    2) Morpheus

[Input: Number min 1, max 2]
""")
    
        while True:
            input_fight_1 = input("> Valid input: 1 or 2 \n ")
            if (input_fight_1 in "1" or input_fight_1 in "2"):
                break
        
        if "1" in input_fight_1:
            print("""
Your opponent is Agent Smith: 

Agent Smith is too advanced for you.
You gain a lot of experience, but you ultimately die. 

""")
            
            return fail()
        
        elif "2" in input_fight_1: 
            print("""
Your opponent is Morpheus: 

Morpheus is the perfect opponent to practice with for you.
You gain a lot of experience and you ultimately become the chosen one.
 
""")
            win()
       
    elif input_matrix_1 is "2":
        print("""
Face-Off machines
You are facing the tribe leader of the machine world

The leader of the machine offers you a deal to ultimately end the war
between humans and machines. You are suspicious at the first place, 
but you have no choice. 
This war needs to end. 

    1) Accept the offer of peace 
    2) Accept the offer of peace (trying to lure him into an ambush)

[Input: Number min 1, max 2]
        
""")
        while True:
            input_machine_1 = input("> [Input: Number min 1, max 2] \n ")
            if (input_machine_1 in "1" or input_machine_1 in "2"):
                break
    
        if input_machine_1 is "1":
            print("""
You just ran into an ambush. 
five gazillion machines hid behind an edge. 
You are dead.  

""")
            fail() 
        elif input_machine_1 is "2": 
            print("""
Right decision. 
You tricked him. He never planned on having a genuine peace. 
You outsmarted him. 

You fulfill the prophecy Neo..
           
""")
            win()
    
    elif input_matrix_1 is "3":
        print("""
The Woman in the red dress!

Haha, nice choice. I knew you would follow your instinct. 
Now that you are on the edge of approaching this gorgeous woman, how do you manage the situation?  

Please choose a pickup line: 
    
    1) Are you an interior decorator? 
    Because when I saw you, the entire room became beautiful. 
    
    2) Are you Mexican? Because you're my Juan and only!
    
    3) There's only one thing I want to change about you, 
    and that's your last name.
    
[Input: Number min 1, max 3]
""")

        while True:
            input_red_1 = input(">Valid input: 1 or 2 or 3 ")
            if (input_red_1 in "1" or input_red_1 in "2" or input_red_1 in "3"):
                break
        
        if "1" in input_red_1:
            print("\nShe slapped your face....")
            return fail()
        
        elif "2" in input_red_1:
            print("\nShe smiles....but is not interested. Apparently too cheesy.")
            return fail()

        elif "3" in input_red_1:
            print("""
She fell for it. 
You live happily together until the end of days.

""")
            win()


        input("< Press enter to close the game >")
        
        print("\f")
        win()


    else:
        print("""
Please check your input. 
Valid: Numbers

""")
        matrix_1()


def win():
    print("\f")
    print("""


██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                               
███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗                
████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝                
██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝                 
██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗                 
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗                
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝                
                                                               
███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗███████╗██████╗        
██╔════╝██║████╗  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗       
█████╗  ██║██╔██╗ ██║██║███████╗███████║█████╗  ██║  ██║       
██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║██╔══╝  ██║  ██║       
██║     ██║██║ ╚████║██║███████║██║  ██║███████╗██████╔╝       
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝        
                                                               


""")
    print("Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes'or replay == "y":
        choice_pill()
        
    else:
        print("Thanks for playing!")
        exit(0)


def fail():
    print("""
You have failed, either in real life or in the Matrix. 
Thanks for playing!

 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                    
 ██████╗ ██╗   ██╗███████╗██████╗   
██╔═══██╗██║   ██║██╔════╝██╔══██╗  
██║   ██║██║   ██║█████╗  ██████╔╝  
██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  
╚██████╔╝ ╚████╔╝ ███████╗██║  ██║  
 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝  
                                    
                          

""")
    print("Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes'or replay == "y":
        choice_pill()
        
    else:
        print("Thanks for playing!")
        exit(0)

choice_pill()
