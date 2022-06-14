import random 

def move(choose):

    options = {"R": "Rock", "P":"Paper", "S":"Scissors"}

    for i in options:
        if i == choose:
            return (options[i])
while True:

    moves=['R', 'P', 'S']
    user_input=input('Choose one of these; R,P,S: ')
    cpu=random.choice(moves)
    print(f"player ({move(user_input)}) : CPU ({move(cpu)})")

    if cpu==user_input:
        print("It's a tie! Try again")
    elif user_input in moves:
        if user_input=='R' and cpu=="P":
            print('Computer wins!')
        elif user_input=='P' and cpu=='R':
            print('You win!')
        elif user_input=='S' and cpu=='R':
            print('Computer wins!')
        elif user_input=='R' and cpu=='S':
            print('You win!')
        elif user_input=='P' and cpu=='S':
            print('Computer wins!')
        elif user_input=='S' and cpu=='P':
            print('You win!')
        break

    else:
        print('Error! Make a valid move')
     
