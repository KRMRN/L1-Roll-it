
def yes_no(question):

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes/no")
            continue

def instructions():
    '''Prints instructions'''

    print('''
 *** Instructions ***   
    
 Roll the dice and try to win!   
    ''')


# Main routine

# ask the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")

# display instuctiosn
if want_instructions == "yes":
    instructions()

print()
print("Program continues")