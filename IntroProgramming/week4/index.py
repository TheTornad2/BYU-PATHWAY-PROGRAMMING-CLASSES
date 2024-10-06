"""

Thank you for reviewing this task. I added some ASCII images to load them in the terminal. I wanted to create something more elaborate, but I don't want to take longer. I got confused and made the average calculator application very elaborate, and then I realized that it was really supposed to be a story. We haven't had much electricity in the Dominican Republic lately, and I apologize for the delay because of that. I hope you enjoy it!

"""

input(
    r"""
    
    
    
    
  _______ _            ______                  _            __   _   _             _____                    _       
 |__   __| |          |  ____|                | |          / _| | | | |           / ____|                  | |      
    | |  | |__   ___  | |__ ___  _ __ ___  ___| |_    ___ | |_  | |_| |__   ___  | (___   ___  ___ _ __ ___| |_ ___ 
    | |  | '_ \ / _ \ |  __/ _ \| '__/ _ \/ __| __|  / _ \|  _| | __| '_ \ / _ \  \___ \ / _ \/ __| '__/ _ \ __/ __|
    | |  | | | |  __/ | | | (_) | | |  __/\__ \ |_  | (_) | |   | |_| | | |  __/  ____) |  __/ (__| | |  __/ |_\__ |
    |_|  |_| |_|\___| |_|  \___/|_|  \___||___/\__|  \___/|_|    \__|_| |_|\___| |_____/ \___|\___|_|  \___|\__|___/

                                        |---------------------------------|  
                                           Press Enter to start the game                                                                                                                  
                                        |---------------------------------|    
    
    
    
    """
)


def adventure_game():
    print(
        r"""
    ┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈╱╲┈┈┈┈
    ╱╯╰╲┈┈╳╳┈┈╱╯╰╲┈┈╳╳┈┈╱╯╰╲┈┈╳╳┈┈╱╯╰╲┈┈╳╳┈┈╱╯╰╲┈┈╳╳┈┈╱╯╰╲┈┈╱╲
    ╯╯╰╰╲╱╮╰╲╱╯╯╰╰╲╱╮╰╲╱╯╯╰╰╲╱╮╰╲╱╯╯╰╰╲╱╮╰╲╱╯╯╰╰╲╱╮╰╲╱╯╯╰╰╲╱╮╰╲
    ╯╯╰╰╱╰╯╭╮╲╯╯╰╰╱╰╯╭╮╲╯╯╰╰╱╰╯╭╮╲╯╯╰╰╱╰╯╭╮╲╯╯╰╰╱╰╯╭╮╲╯╯╰╰╱╰╯╭╮╲
    ╯╯╰╱╯╭╮╰╯╭╲╯╰╰╱╯╭╮╰╯╭╲╯╰╰╱╯╭╮╰╯╭╲╯╰╰╱╯╭╮╰╯╭╲╯╰╰╱╯╭╮╰╯╭╲╯╰╰╱╯╭
    ▔▋╱╭╮╰╯╭╮╰╯╲▋▔▋╱╭╮╰╯╭╮╰╯╲▋▔▋╱╭╮╰╯╭╮╰╯╲▋▔▋╱╭╮╰╯╭╮╰╯╲▋▔▋╱╭╮╰╯╭╮╰╯
    ┈╱╮╰╯╭╮╰╯╭╮╰╲┈┈╱╮╰╯╭╮╰╯╭╮╰╯╮┈┈╱╮╰╯╭╮╰╯╭╮╰╯╮┈┈╱╮╰╯╭╮╰╯╭╮╰╯╮┈╈╭╮╰
    ▔▔▔▔▔▋▔▔▔▋▔▔▋▔▔▔▔▋▔▔▔▋▔▔▔▔▋▔▔▔▋▔▔▔▋▔▔▔▋▔▔▔▋▔▔▔▋▔▔▋▔▔▋▔▔▋▔▔▋▔▔▋

    """
    )
    print(
        "You are standing in front of a mysterious forest. You see a SWORD and a SHIELD."
    )
    choice = (
        input(
            r"""
              
              Which one do you want to pick up? (SWORD/SHIELD):  
                 
                    />____________________________________
            [########[]__________________________________/                   
                    \>
              
              
              
              
                    \_              _/      
                    ] --__________-- [
                    |       ||       |
                    \       ||       /
                     [      ||      ]      
                     |______||______|       
                     |------..------|       
                     ]      ||      [       
                      \     ||     /        
                       [    ||    ]         
                       \    ||    /         
                        [   ||   ]             
                         \__||__/           
                            --      
              """
        )
        .strip()
        .lower()
    )

    if choice == "sword":
        print("\n\nYou pick up the sword. A dragon suddenly appears!")
        next_choice = input("Do you want to FIGHT or RUN?: ").strip().lower()

        if next_choice == "fight":
            print("\n\nYou fight the dragon! It breathes fire at you.")
            final_choice = (
                input("\n\nDo you DODGE or BLOCK with your sword?: ").strip().lower()
            )

            if final_choice == "dodge":
                print(
                    "\n\nYou dodge the fire and strike the dragon down. You are victorious!"
                )
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _  | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
    """
                )

            elif final_choice == "block":
                print(
                    "\n\nYou block the fire with your sword, but it melts! The dragon defeats you."
                )
                print(
                    r"""
  _______           _ _                       _          
 |__   __|         (_) |                     (_)         
    | |_ __ _   _   _| |_    __ _  __ _  __ _ _ _ __     
    | | '__| | | | | | __|  / _` |/ _` |/ _  | | '_ \    
    | | |  | |_| | | | |_  | (_| | (_| | (_| | | | | |_  
    |_|_|   \__, | |_|\__|  \__,_|\__, |\__,_|_|_| |_(_) 
             __/ |                 __/ |                 
            |___/                 |___/
    """
                )
            else:
                print("\n\nInvalid choice. The dragon incinerates you.")

        elif next_choice == "run":
            print("\n\nYou run away from the dragon, but encounter a steep cliff!")
            final_choice = input("Do you JUMP or CLIMB down?: ").strip().lower()

            if final_choice == "jump":
                print("\n\nYou make a daring leap and land safely!")
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _  | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
    """
                )
            elif final_choice == "climb":
                print("\n\nYou carefully climb down and reach the bottom safely.")
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _  | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
    """
                )
            else:
                print("\n\nInvalid choice. You lose your grip and fall.")
                print(
                    r"""
  _______           _ _                       _          
 |__   __|         (_) |                     (_)         
    | |_ __ _   _   _| |_    __ _  __ _  __ _ _ _ __     
    | | '__| | | | | | __|  / _` |/ _` |/ _  | | '_ \    
    | | |  | |_| | | | |_  | (_| | (_| | (_| | | | | |_  
    |_|_|   \__, | |_|\__|  \__,_|\__, |\__,_|_|_| |_(_) 
             __/ |                 __/ |                 
            |___/                 |___/
    """
                )
        else:
            print("\n\nInvalid choice. The dragon catches you while you're indecisive.")
            print(
                r"""
  _______           _ _                       _          
 |__   __|         (_) |                     (_)         
    | |_ __ _   _   _| |_    __ _  __ _  __ _ _ _ __     
    | | '__| | | | | | __|  / _` |/ _` |/ _  | | '_ \    
    | | |  | |_| | | | |_  | (_| | (_| | (_| | | | | |_  
    |_|_|   \__, | |_|\__|  \__,_|\__, |\__,_|_|_| |_(_) 
             __/ |                 __/ |                 
            |___/                 |___/
    """
            )

    elif choice == "\n\nshield":
        print("\n\nYou pick up the shield. A band of goblins appears!")
        next_choice = input("Do you want to DEFEND or NEGOTIATE?: ").strip().lower()

        if next_choice == "\n\ndefend":
            print("\n\nYou block the goblins' attacks with your shield.")
            final_choice = (
                input("\n\nDo you CHARGE at them or WAIT for reinforcements?: ")
                .strip()
                .lower()
            )

            if final_choice == "charge":
                print("\n\nYou charge and scare the goblins off!")
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
    """
                )
            elif final_choice == "wait":
                print("\n\nReinforcements arrive and help you defeat the goblins.")
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
    """
                )
            else:
                print("\n\nInvalid choice. The goblins overpower you.")
        elif next_choice == "negotiate":
            print("\n\nYou negotiate with the goblins, but one of them betrays you!")
            final_choice = input("Do you FLEE or FIGHT?: ").strip().lower()

            if final_choice == "flee":
                print("\n\nYou flee and escape the goblins.")
                print(
                    r"""
  _______ _           _                              _                
 |__   __| |         | |                            | |               
    | |  | |__   __ _| |_  __      ____ _ ___    ___| | ___  ___  ___ 
    | |  | '_ \ / _` | __| \ \ /\ / / _` / __|  / __| |/ _ \/ __|/ _ \ 
    | |  | | | | (_| | |_   \ V  V / (_| \__ \ | (__| | (_) \__ \  __/
    |_|  |_| |_|\__,_|\__|   \_/\_/ \__,_|___/  \___|_|\___/|___/\___|
                                                                      
                                                                      
        """
                )
            elif final_choice == "fight":
                print("\n\nYou fight and defeat the goblins.")
                print(
                    r"""
                                  _         _       _   _                 
                                 | |       | |     | | (_)                
   ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
  / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
 | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                  
                  |___/                                                   
        """
                )
            else:
                print("\n\nInvalid choice. The goblins capture you.")
                print(
                    r"""
  _______           _ _                       _          
 |__   __|         (_) |                     (_)         
    | |_ __ _   _   _| |_    __ _  __ _  __ _ _ _ __     
    | | '__| | | | | | __|  / _` |/ _` |/ _` | | '_ \    
    | | |  | |_| | | | |_  | (_| | (_| | (_| | | | | |_  
    |_|_|   \__, | |_|\__|  \__,_|\__, |\__,_|_|_| |_(_) 
             __/ |                 __/ |                 
            |___/                 |___/                  
        """
                )
    else:
        print(
            "\n\nInvalid choice. You stand there confused and something dangerous approaches..."
        )
        print(
            r"""
  _______           _ _                       _          
 |__   __|         (_) |                     (_)         
    | |_ __ _   _   _| |_    __ _  __ _  __ _ _ _ __     
    | | '__| | | | | | __|  / _` |/ _` |/ _` | | '_ \    
    | | |  | |_| | | | |_  | (_| | (_| | (_| | | | | |_  
    |_|_|   \__, | |_|\__|  \__,_|\__, |\__,_|_|_| |_(_) 
             __/ |                 __/ |                 
            |___/                 |___/                  
    """
        )


adventure_game()
