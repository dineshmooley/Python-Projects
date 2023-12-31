import random as r
def comp_choice():
    moves = ['rock', 'paper', 'scissor']
    comp = r.choice(moves)
    print('Computer:', comp)
    return comp

def hum_choice():
    hum = input('rock, paper, scissor: ')
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
    ans = input("Do you want to continue? Y/N")
    
    if ans == 'N':
        break

print("Thank you for playing the game :)")
