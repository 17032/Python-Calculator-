# final calculator version 3
# add a unit measurement option: millimeter, centimeter, meter, kilometer
# print messages throughout the calculator to remind the user about the unit of the shape 

import sys # to be able to quit the program at the end easily 
import math # import math module to be able to do calculuations for example: the vaue of pi

print('*****Welcome to the area and perimeter calculator!*****\n')

name = input('What is your name?') # program stores name and name is a variable 
print ('Hello,',name) # then prints then welcomes the user (letters the user has entered) 
print("Instructions:")
print("- Choose a type of unit")
print("- Choose a shape")
print("- Enter the relevant lengths depending on the shape")
print("- Make sure to use the same unit when you enter the lengths\n")

def main_calculator(): # the main part of my code is in a function to be able to call it at the end

    print("Which unit of measure would you like to calculate your shape in?\n")
    
    print('Unit of measureres: ')
    print('1) Millimeter "mm" ')
    print('2) Centimeter "cm"') 
    print('3) Meter "m"') 
    print('4) Kilometer "km"\n')

    print("To select a unit enter the the number of the correspoding unit!")
    print('For example: to choose centimeter enter "cm"\n') 
        
    def unit_check(): # function to check that the input for the unit is valid 
        unit = input("Enter your choosen unit:")
        print("\n")
        allowedunits = ["km", "m", "cm", "mm"] # the user can only enter the options in the list 
        while not unit in allowedunits: # if input is not in the list 
            unit = input("Please enter a valid unit from the opitons above:")
            print("\n")
        return unit
    user_unit = unit_check() # the unit function is equal to the variable function user_unit so it can be printed in statements 
       
    print('The shape options which can be calculated are:')
    print('1) Square')
    print('2) Rectangle') 
    print('3) Triangle') 
    print('4) Circle')
    print('5) Quit the calculator \n')

    print('To select a shape enter the number of the corresponding shape!') 
    print('For example: to choose triangle enter "3"\n') 

    # the program asks the user to enter which shape to calculate only accept numbers 1-4


    def check_input(valid_number): # function which checks all user input, whether it is valid (whole positive numbers) or invalid
        """Get user input as int"""
        value = None
        while not value: # creates a loop so it will keep going till user input is valid 
            value = input(valid_number)
            if not value.isnumeric(): # if input is not a number
                print("Please enter a valid number")
                print("\n")
                value = None
            else:
                return int(value) # once a correct number is entered the number is returned and program contiues

    while True: # creates a loop for the input from the user
        try:
            shape = int(input("Pick a shape and enter the corresponding number or quit:"))
            print("\n")
        except ValueError:
            print("\n")
            print("Please enter a valid shape option\n") # if anything other than an integer is entered this message is printed 
            continue # once a number has been entered the program continues
        
        if shape == 1: # user has inputted 1
            
            print("You have choosen square!")
            length = check_input("Enter the length of a side: ")

            print("\n")
            print("Have you entered the length in", user_unit, "?" ) # check user has inputted length in the correct chosen unit at the start 
            check_length = input("For no press 'n' to enter the correct length or press any key for yes:") # to enter length again input in n or anything else 
            print("\n")

            if check_length == "n": # input was n so input length statement 
                print("Please enter the length in the correct unit of", user_unit,"!")
                length = check_input("Enter the length of a side:")
                
            else: # user input is anything else program continues 
                print("You have entered the length in the correct unit, well done!")
                           
            area = length * length # takes the numbers entered and multiplys them to give area and perimeter
            perimeter = 4 * length
            print("\n")
            print("The area of the square is", area, user_unit,'\u00b2') # prints area with the correct unit to the power of 2 
            print("The perimeter of the square is", perimeter, user_unit,'\n') # prints perimeter in a statement with the correct unit
            break # the loop breaks
        
        elif shape == 2: # user has inputted 2
            print("You have choosen rectangle!")
            length = check_input("Enter the length of a side: ")
            width = check_input("Enter the value of the width: ")

            print("\n")
            print("Have you entered the length in", user_unit, "?" )
            check_length = input("For no press 'n' to enter the correct length or press any key for yes:")
            print("\n")

            if check_length == "n":
                print("Please enter the lengths in the correct unit of", user_unit, "!")
                length = check_input("Enter the length of a side:")
                width = check_input("Enter the value of the width: ")
                
            else:
                print("You have entered the length in the correct unit, well done!")

            area = length * width
            perimeter = 2 * (width + length)
            print("\n")
            print("The area of the rectangle is", area, user_unit,'\u00b2')
            print("The perimeter of the rectangle is", perimeter, user_unit,'\n')
            break

        elif shape == 3: # user has inputted 3
            print("You have choosen triangle!")
            base = check_input("Enter the length of the base: ")
            height = check_input("Enter the value of the height: ")
            side1 = check_input("Enter the length of a side: ")
            side2 = check_input("Enter the length of the other side:")

            print("\n")
            print("Have you entered the length in", user_unit, "?" )
            check_length = input("For no press 'n' to enter the correct length or press any key for yes:")
            print("\n")

            if check_length == "n":
                print("Please enter the lengths in the correct unit of", user_unit, "!")
                base = check_input("Enter the length of the base: ")
                height = check_input("Enter the value of the height: ")
                side1 = check_input("Enter the length of a side: ")
                side2 = check_input("Enter the length of the other side:")
                
            else:
                print("You have entered the length in the correct unit, well done!")
                
            area = 0.5 * base * height
            perimeter = base + side1 + side2
            print("\n")
            print("The area of the triangle is", area, user_unit,'\u00b2')
            print("The perimeter of the triangle is", perimeter, user_unit,'\n')
            break

        elif shape == 4: # user has inputted 4 
            print("You have choosen circle!")
            radius = check_input("Enter the length of the radius: ")

            print("\n")
            print("Have you entered the length in", user_unit, "?" )
            check_length = input("For no press 'n' to enter the correct length or press any key for yes:")
            print("\n")

            if check_length == "n":
                print("Please enter the radius in the correct unit of", user_unit, "!")
                radius = check_input("Enter the length of the radius: ")
                
            else:
                print("You have entered the length in the correct unit, well done!")
                
            area = ( math.pi * radius * radius)
            perimeter = (2 * math.pi * radius)
            print("\n")
            print("The area of the circle is", str(round(area, 2)), user_unit,'\u00b2')
            print("The circumference of the circle is", str(round(perimeter, 2)), user_unit,'\n')
            break

        elif shape == 5: # user has inputted 5 
            print("\n")
            print("Goodbye!")
            print('Come back to the area and perimeter calculator anytime :)')
            sys.exit() # the program exits the loop and function to quit 
        
    print("Would you like to calculate another shape?") # at the end after calculations another opiton to quit
    restart=input('To calculate another shape press "y" or to quit press any key:')
    if restart== "y": # if the input is y then the main function is called and the program runs again 
            print("\n")
            main_calculator()
            
    else: # if the input if any key/thing other than y then the program prints messages
        print("\n")
        print('Goodbye,have a lovely day!')
        print('Come back to the area and perimeter calculator anytime :)')
        sys.exit() # the program quits out of function and ends

main_calculator() # the end of the main calculator function 








