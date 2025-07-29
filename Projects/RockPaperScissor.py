# -*- coding: utf-8 -*-
import random

print("\n====================")
print("Rock Paper Scissors")
print("====================")

print("\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

num = int(input("Pick a number: "))

cpu = random.randint(1,3)

match num:
    case 1:
        if cpu == 1:
            print("You chose: ✊")
            print("CPU chose ✊")
            
            print("\nTie!!")
           
        elif cpu == 2:
            print("You chose: ✊")
            print("CPU chose ✋")
            
            print("\nCPU won!!")
            
        else:
            print("You chose: ✊")
            print("CPU chose ✌️")
            
            print("\nYou won!!")
    
    case 2:
        if cpu == 1:
            print("You chose: ✋")
            print("CPU chose: ✊")
            
            print("\nYou won!!")
            
        elif cpu == 2:
            print("You chose: ✋")
            print("CPU chose: ✋")
            
            print("\nTie!!")
            
        else:
            print("You chose: ✋")
            print("CPU chose: ✌️")
            
            print("\nCPU won!!")
                
    case 3:
        if cpu == 1:
            print("You chose: ✌️")
            print("CPU chose: ✊")
            
            print("\nCPU won!!")
        
        elif cpu == 2:
            print("You chose: ✌️")
            print("CPU chose: ✋")
            
            print("\nYou won!!")
            
        else:
            print("You chose: ✌️")
            print("CPU chose: ✌️")
            
            print("\nTie!!")