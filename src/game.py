from variables_module import user_score, computer_score, round_count, emojis, Selection_error
from random import randint


#Loop 5 times 
while  (user_score < 3 and computer_score < 3) and round_count < 5:
    
    #computer selection
    computer_selection = randint(1, 3)
    
    #Ask user option and check valid input 
    try:
        user_selection = int(input('Please select one option in number :\n 1.Paper.\n 2.Sicssors.\n 3.Rock: '))
        if user_selection < 1 or user_selection > 3:
            raise Selection_error (f'Please enter a valid number between 1 to 3')
            

        #Chek if both option are the same
        if user_selection == computer_selection:
        
            print(f'User: {emojis[user_selection - 1]}, Computer: {emojis[computer_selection - 1]} = draw')
        
        #check if user win
        elif (user_selection == 1 and computer_selection == 3) or \
             (user_selection == 2 and computer_selection == 1)or \
             (user_selection == 3 and computer_selection == 2):
        
            user_score += 1
            print(f'User: {emojis[user_selection - 1]}, Computer: {emojis[computer_selection - 1]} = You win!')

        #check if computer win
        else:
            
            computer_score += 1
            print(f'User: {emojis[user_selection - 1]}, Computer: {emojis[computer_selection - 1 ]} = Computer win!')

        round_count += 1
    except Selection_error as e:
        print(f'Error : {e}')
    except ValueError:
        print('Error: please enter  a valid numeric value.')


#Final results
if user_score == computer_score:
    
    print(f'User: {user_score} Computer: {computer_score} Round: {round_count} result = Draw')
    
elif user_score > computer_score:
    
    print(f'User: {user_score} Computer: {computer_score} Round: {round_count} result = You win!')

else:
    print(f'User: {user_score} Computer: {computer_score} Round: {round_count} result = Computer win!')