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
        "You are standing in front of a mysterious cave. You see a SWORD and a SHIELD."
    )
    choice = (
        input(
            r"""
              

              \n\nWhich one do you want to pick up? (SWORD/SHIELD):  
                 

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
                    r"""\n\n
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
  _______           _                      _      _   _               
 |__   __|         | |                    | |    | | (_)              
    | |   _ __ ___ | |__    _ __  _ __ ___| |__  | |_ _  ___  _ __   
    | |  | '_ ` _ \| '_ \  | '_ \| '__/ _ \ '_ \ | __| |/ _ \| '_ \  
    | |  | | | | | | | | | | | | | | |  __/ | | || |_| | (_) | | | | 
    |_|  |_| |_| |_|_| |_| |_| |_|_|  \___|_| |_| \__|_|\___/|_| |_|                                                                                 
                """
                )

        elif next_choice == "run":
            print(
                "\n\nYou run away safely but leave the sword behind. The dragon flies away."
            )
            print(
                r""" _______           _                      _      _   _               
 |__   __|         | |                    | |    | | (_)              
    | |   _ __ ___ | |__    _ __  _ __ ___| |__  | |_ _  ___  _ __   
    | |  | '_ ` _ \| '_ \  | '_ \| '__/ _ \ '_ \ | __| |/ _ \| '_ \  
    | |  | | | | | | | | | | | | | | |  __/ | | || |_| | (_) | | | | 
    |_|  |_| |_| |_|_| |_| |_| |_|_|  \___|_| |_| \__|_|\___/|_| |_|                                                                     
                """
            )

    elif choice == "shield":
        print("\n\nYou pick up the shield. A dragon suddenly appears!")
        next_choice = input("Do you want to FIGHT or RUN?: ").strip().lower()

        if next_choice == "fight":
            print("\n\nYou fight the dragon! It breathes fire at you.")
            final_choice = (
                input("\n\nDo you DODGE or BLOCK with your shield?: ").strip().lower()
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
                print("\n\nYou block the fire with your shield. You are safe!")
                print(
                    r"""
   __  __           _      _             _    _             
  |  \/  |         | |    | |           | |  (_)            
  | \  / | ___  ___| |__  | |_ __   __ _| |_  _ _ __   __ _ 
  | |\/| |/ _ \/ __| '_ \ | | '_ \ / _` | __|| | '_ \ / _` |
  | |  | |  __/ (__| | | || | | | | (_| | |_ | | | | | (_| |
  |_|  |_|\___|\___|_| |_||_|_| |_|\__,_|\__||_|_| |_|\__, |
                                                       __/ |
                                                      |___/ 
"""
                )

        elif next_choice == "run":
            print(
                "\n\nYou run away safely but leave the shield behind. The dragon flies away."
            )
            print(
                """
   _______           _                      _      _   _               
 |__   __|         | |                    | |    | | (_)              
    | |   _ __ ___ | |__    _ __  _ __ ___| |__  | |_ _  ___  _ __   
    | |  | '_ ` _ \| '_ \  | '_ \| '__/ _ \ '_ \ | __| |/ _ \| '_ \  
    | |  | | | | | | | | | | | | | | |  __/ | | || |_| | (_) | | | | 
    |_|  |_| |_| |_|_| |_| |_| |_|_|  \___|_| |_| \__|_|\___/|_| |_|                                                                 
                """
            )


adventure_game()
