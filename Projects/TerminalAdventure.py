import sys

print("\n============================")
print("Adventure in HS FARM HOUSE")
print("============================")

print("\n")

print("You woke up in the midnight of 22 August 2025 and went in the Chowk of the house. Then you hear weird sounds from the backyard Of the house. And on the other side, you hear the sound of your Dada Ji calling your name again and again. Then which option will you choose?\n")
print("1) Go to the backyard to check from where the sound is coming.") 
print("2) Go to Dada Ji's room to check why he is calling again and again.")

a = int(input("\n1 or 2 ? => "))

print("\n")

if(a==1):
    print("You go to the backyard and See that there is a white shadow in the store room in the backyard. Then which option will you choose?\n") 
    print("1) Go near the shadow")
    print("2) Go inside your bedroom")
    
    b = int(input("\n1 or 2 ? => "))
    
    print("\n")
    
    if(b==1):
        print("You went near the shadow, and the shadow Is disappeared !! Now, which option will you choose?\n")
        print("1) Chant Hanuman Chalisa")
        print("2) Go to Dada Ji's room and try waking up Dada Ji.")
        
        c = int(input("\n1 or 2 ? => "))
        
        print("\n")
        
        if(c==1):
            print("You chanted Hanuman Chalisa And then you woke up and realized that it was just a dream")
            
        elif(c==2):
            print("You tried waking up Dada Ji,But dada ji is not waking up and you are not able to speak , and then suddenly your eyes opened, and you realized that it was just a dream.")
        
        else:
            print("Wrong input!!")
            print("Quitting....")
            sys.exit()
            
    elif(b==2):
        print("You are running from the gallery and then realize that the white shadow is following you. Then you ran much faster than You typically run. And when you arrived in the choke, then you saw that the white shadow is standing in the gate of the veranda. Then what will you do?\n")
        print("1) Go to dada ji's room to wake up dada ji.")
        print("2) Chant Hanuman Chalisa")
        
        d = int(input("\n1 or 2 ? => "))
        
        print("\n")
        
        if(d==1):
            print("You try to wake up Dada ji, but Dada ji is not waking up. Then you suddenly hear the Sound of Moti that he is barking loudly again and again. Then what will you do?\n")
            print("1) Keep trying, waking up Dada Ji.")
            print("2) Follow the sounds of Moti to check why he is barking again and again.")
            
            e = int(input("\n1 or 2 ? => "))
            
            print("\n")
            
            if(e==1):
                print("You were trying to wake up Dada Ji, and then suddenly your eyes opened, and you realized that it was just a dream.")
                
            elif(e==2):
                print("You went near The room of Moti, and then realize that he is not barking and he is sleeping. Then what will you do?\n")
                print("1) Go back to Dada Ji's room and again try waking up Dada Ji.")
                print("2) Chant Hanuman Chalisa")
                
                f = int(input("\n1 or 2 ? => "))
                
                print("\n")
                
                if(f==1):
                    print("You went back to Dada ji's room and tried waking up Dada ji, but suddenly your eyes opened and you realized that it was just a dream.")
                    
                elif(f==2):
                    print("You chanted Hanuman Chalisa, and suddenly your eyes opened, realizing it was just a dream.")
                    
                else:
                    print("Wrong input!!")
                    print("Quitting....")
                    sys.exit()
        
        elif(d==2):
            print("You chanted Hanuman Chalisa, and suddenly your eyes opened, realizing it was just a dream.")
            
        else:
            print("Wrong input!!")
            print("Quitting....")
            sys.exit()
            
    else:
        print("Wrong input!!")
        print("Quitting....")
        sys.exit()
        
if(a==2):
    print("You get to know that Dada Ji is sleeping, but the voices are still coming in the voice of Dada Ji. Then what will you do?\n")
    print("1) Try to wake up Dada Ji.")
    print("2) Follow the sounds again To check from where the voices are coming.")
    
    b = int(input("\n1 or 2 ? => "))
    
    print("\n")
    
    if(b==1):
        print("Dadaji is not waking.up And then you Hear loud sounds of cats Like they are fighting aggressively in the chauk of sushant's home.Then what will you do?\n")
        print("1) Keep trying, waking up Dada Ji.")
        print("2) Follow the sounds of the cats.")
        
        c = int(input("\n1 or 2 ? => "))
        
        print("\n")
        
        if(c==1):
            print("You are trying to wake up Dada ji, but suddenly realize that Moti came inside the dadaji's room, and his eyes are red,And he is coming towards you slowly. Then what will you do?\n")
            print("1) Keep trying, waking up dada ji.")
            print("2) Run from the room of the Dada ji.")
        
            d = int(input("\n1 or 2 ? => "))
            
            print("\n")
        
            if(d==1):
                print("You tried waking up Dada ji, but Dada ji is still not waking up. Suddenly, your eyes opened, and you realized that it was just a dream.")
            
            elif(d==2):
                print("You are running from the room of Dadaji, and Moti is following you with aggressive anger in his eyes. Then what will you do?\n")
                print("1) Go to the bedroom")
                print("2) Go back to dadaji's room and try waking up dadaji again.")
            
                e = int(input("\n1 or 2 ? => "))
                
                print("\n")

                if(e==1):
                    print("You went to your bedroom and locked the room. And then again you started hearing the sound Of Moti barking loudly.Then what will you do?\n")
                    print("1) Open the door again and check what happened to Moti.")
                    print("2) Chant Hanuman Chalisa")
                
                    f = int(input("\n1 or 2 ? => "))
                    
                    print("\n")
                
                    if(f==1):
                        print("You opened the door, and then suddenly your eyes opened, and you realized that it was just a dream.")
                    
                    elif(f==2):
                        print("You chanted Hanuman Chalisa, and your eyes opened, realizing that it was just a dream.")
                
                    else:
                        print("Invalid input!!")
                        print("Quitting...")
                        sys.exit()
            
                elif(e==2):
                    print("You went back to Dada Ji's room and tried waking up Dada Ji again and again, but Dada Ji is still not waking up. Suddenly, your eyes opened, and you realized that it was just a dream.")
            
                else:
                    print("Invalid input!!")
                    print("Quitting...")
                    sys.exit()
            
            else:
                print("Invalid input!!")
                print("Quitting...")
                sys.exit()
        
        elif(c==2):
            print("You followed the sound of cats and went to chauk of Sushant's home, And then you realize that there are no cats Fighting in the chauk. Then what will you do?\n") 
            print("1) Go inside the Sushant's bedroom.")     
            print("2) Go back to Dada Ji's room and try waking up Dada ji.") 
            
            d = int(input("\n1 or 2 ? => "))
            
            print("\n")
            
            if(d==1):
                print("You went to Sushant's bedroom, but the door is not getting opened. It is jammed. Then what will you do?\n")
                print("1) Go back to Dada Ji's room and try waking up Dada Ji again and again.")
                print("2) Chant Hanuman Chalisa")
                
                e = int(input("\n1 or 2 ? => "))
                
                print("\n")
                
                if(e==1):
                    print("You went to Dadaji's room again and tried waking up Dadaji. Suddenly, your eyes opened, and you realized that it was just a dream.")
                
                elif(e==2):
                    print("You started chanting Hanuman Chalisa, and then suddenly your eyes opened, and you realized that it was just a dream.")
                
                else:
                    print("Invalid input!!")
                    print("Quitting...")
                    sys.exit()
                
            elif(d==2):
                print("You went back to Dada Ji's room and tried waking up Dada Ji. Suddenly, your eyes opened, and you realized that it was just a dream.")
            
            else:
                print("Invalid input!!")
                print("Quitting...")
                sys.exit()
                
        else:
            print("Invalid input!!")
            print("Quitting...")
            sys.exit()
            
    elif(b==2):
        print("When you follow the sounds, the sounds are moving far from you. Then what will you do?\n")
        print("1) Don't follow the sounds and go to Dadaji's room. And try waking up Dada Ji")
        print("2) Follow the sounds")
        
        c = int(input("\n1 or 2 ? => "))
        
        print("\n")
        
        if(c==1):
            print("You came back to Dada ji's room and tried waking up Dada ji again and again, but Dada ji is still not waking up. And then suddenly your eyes opened and you realized that it was just a dream.")
            
        elif(c==2):
            print("You followed the sounds, and the sounds are not stopping, And getting louder and louder and moving far from you, then what will you do?")
            print("1) Go back to Dada Ji's room and try waking up Dada Ji.")
            print("2) Chant Hanuman Chalisa")
            
            d = int(input("\n1 or 2 ? => "))
            
            print("\n")
            
            if(d==1):
                print("You came back to Dada ji's room and tried waking up Dada ji again and again, but Dada ji is still not waking up. And then suddenly your eyes opened and you realized that it was just a dream.")
                
            elif(d==2):
                print("You started chanting Hanuman Chalisa, and then suddenly your eyes opened, and you realized that it was just a dream.")
               
            else:
                print("Invalid input!!")
                print("Quitting...")
                sys.exit() 
        
        else:
            print("Invalid input!!")
            print("Quitting...")
            sys.exit()
            
    else:
        print("Invalid input!!")
        print("Quitting...")
        sys.exit()

else:
    print("Invalid input!!")
    print("Quitting...")
    sys.exit()
