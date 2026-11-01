import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

print("*****WELCOME TO THE GAME OF GAMBLING*****")

game=input("Do you want to play a game of blackjack? Type 'y'  or  'n'  :: ")

if game=="y":
    
    user_cards=[]
    
    user_cards=[random.choice(cards),random.choice(cards)]
    
    print(f"The user cards are {user_cards}")
    
    current_score=user_cards[0]+user_cards[1]
    
    if current_score==21:
        print("You won")
        
    if current_score>21:
        
        aces=input("Are there any Aces ? 'y' or 'n' :: ")
        
        if aces=="y":
            
            all_one=input("Do you want to make 2 aces consider as 1 ? 'y' or 'n' :: ")
            
            if all_one=="y":
                
                user_cards=[1,1]
                
                print(f"The user cards are {user_cards}")

            if all_one=="n":
                
                user_cards=[1,11]
                
                print(f"The user cards are {user_cards}")


    computer_1st_card=random.choice(cards)

    print(f"computer's 1st card is {computer_1st_card}")
    
    print(f"Current score is {current_score}")
    
    choice=input("Type 'y' to get another card or 'n' to pass :: ")
    
    if choice=="y":
        
        user_cards.append(random.choice(cards))
        
        print(f"User all cards are {user_cards}")
        
        current_score=user_cards[0]+user_cards[1]+user_cards[2]
        
        print(f"Current score is {current_score}")
        
        if current_score>21:
            print("You Lose")
            
        if current_score==21:
            print("You won")
            
        if current_score<21:
            computer_2nd_card=random.choice(cards)
        
            print(f"Computer 2nd card is {computer_2nd_card}")
            
            computer_score=computer_1st_card+computer_2nd_card
            
            print(f"Computer score is {computer_score}")
            
            if computer_score<16:
                
                print("Hence the computer score is less than 16 , Computer will choose anothher card.")
                
                computer_3rd_card=random.choice(cards)
                
                print(f"Computer 3rd card is {computer_3rd_card}")
                
                computer_score=computer_1st_card+computer_2nd_card+computer_3rd_card
                
                print(f"Now the computer score is {computer_score}")
                
            if computer_score>21:
                print("You win")
            
            if computer_score<21 and computer_score>current_score:
                print("You Lose")
                
            if computer_score==21:
                print("You Lose")
                
            if computer_score==current_score:
                print("Draw")
            
            if current_score<21 and current_score>computer_score:
                print("You won")
                

    if choice=="n":
        
        computer_2nd_card=random.choice(cards)
        
        print(f"Computer 2nd card is {computer_2nd_card}")
        
        computer_score=computer_1st_card+computer_2nd_card
        
        print(f"Computer score is {computer_score}")
        
        if computer_score<16:
            
            print("Hence the computer score is less than 16 , Computer will choose anothher card.")

            computer_3rd_card=random.choice(cards)
                
            print(f"Computer 3rd card is {computer_3rd_card}")
                
            computer_score=computer_1st_card+computer_2nd_card+computer_3rd_card
            
            print(f"Now the computer score is {computer_score}")

        if computer_score>21:
            print("You win")
            
        if computer_score<21 and computer_score>current_score:
            print("You Lose")
            
        if computer_score==21:
            print("You Lose")
            
        if computer_score==current_score:
            print("Draw")
        
        if current_score<21 and current_score>computer_score:
            print("You won")

if game=="n":
    print("\n")
    print("BRING A HARD HEART THE COME ")
    print("\n")
    

    