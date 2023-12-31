import random as r
moves = ['rock', 'paper', 'scissor']

def comp_choice():
    comp = r.choice(moves)
    print('Computer:', comp)
    return comp

def hum_choice():
    hum = None
    while hum not in moves:
        hum = input('rock, paper, scissor: ').lower()
    return hum

def who_won(comp, hum):
    if comp == hum:
        print("It's a draw!")
        h = hum_choice()
        who_won(comp_choice(), h)

    elif (comp == 'rock' and hum == 'scissor') or (comp == 'paper' and hum == 'rock') or (comp == 'scissor' and hum == 'paper'):
        print("Computer won!")
    
    else:
        print("You have won!")

while True: 
    h = hum_choice()
    who_won(comp_choice(), h)
    ans = input("Do you want to continue? y/n :").lower()
    
    if ans == 'N':
        break

print("Thank you for playing the game :)")
