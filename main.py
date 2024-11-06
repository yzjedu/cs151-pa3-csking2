# # Programmers: Cody
# # Course: CS151, Professor Zee
# # Due Date: November 7th 2024
# # Lab Assignment: PA3
# # Problem Statement: Write a program that displays ASCII art based on user input
# # Credits: Found the picture of the airplane for random online, wrote the code myself,
# # the rest I used the zybooks to help me with understanding it more




#initialize variables
choice = ""
cnumber = 0

#Name: user_choice
#Parameters: None
#Return: choice
def user_choice():
    global choice
    print('\nPurpose: Select one of the following options to create ASCII Art.')
    choice = str(input('Enter an option, Circle, Lines, or Random (enter quit to stop program): '))
    choice = choice.lower()
    while choice != 'quit':
        while choice == 'circle' or choice == 'lines' or choice == 'random':
            if choice == 'circle':
                circle()

                break
            elif choice == 'lines':
                lines()

                break
            elif choice == 'random':
                random()

                break
        choice = str(input('Enter an option, Circle, Lines, or Random (enter quit to stop program): '))
        choice = choice.lower()
    print('\nProgram Stopped')

    return choice


#Name: circle
#Parameters: None
#Return: None
def circle():
    print("    ****   ")
    print(" *       * ")
    print("*         *")
    print("*          *")
    print("*         *")
    print(" *       * ")
    print("    ****    ")


#Name: lines
#Parameters: None
#Return: None
def lines():
    num_lines = input('Enter number of lines: ')
    character = input('Enter a character/set of characters you with to be printed: ')
    times = input('Enter number of times you want your character/set of characters to be printed on each line: ' +'\n')
    if not num_lines.isdigit() or not times.isdigit():
         print('You entered an invalid number for one of the values, try again')
    if num_lines.isdigit() and times.isdigit():
        times = int(times)
        num_lines = int(num_lines)
        print(((character * times + '\n')* num_lines))



#Name: Random
#Parameters: None
#Return: None
def random():
    import random
    global cnumber
    cnumber = random.randint(1, 3)
    if cnumber == 1:
        print('\n|          |\n|          |\n|          |\n|          |\n|          |\n|__________|')
        print('     ||     \n     ||     \n     ||     \n     ||     \n     ||     \n')

    if cnumber == 2:
        print('\n        |                                               | ' * 8)
        print('_' * 19)
        print('| []  []  []  [] |                            |  []  []  []  []  []  | \n' * 14)
        print('| []  []  []  []  []  []  []  []  []  []  []  |  []  []  []  []  []  |\n' * 6)

    if cnumber == 3:
        print('       __|__')
        print('--0' * 2 + '--'+'(_)'+ '--0' * 2 + '--')

#Call main function
user_choice()