import emoji
from random import randint

#create the variables emojis
paper = emoji.emojize(':raised_hand:')
scissors = emoji.emojize(':victory_hand:')
rock = emoji.emojize(':raised_fist:')


# Variables score´s
user_score = 0
computer_score = 0
round_count = 0

#list of emojis
emojis = [paper, scissors, rock]


#Exeption 
class Selection_error(Exception):
    pass
    

 