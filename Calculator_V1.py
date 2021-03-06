#Final calculator version 1
#Give the user the option to quit the program at the start
#So the 5th option is a quit option 

import sys #to be able to quit the program at the end easily 
import math #import math module to be able to do calculuations for example: the vaue of pi

print('*****Welcome to the area and perimeter calculator!*****')

name = input('What is your name?') #program stores name and name is a variable 
print ('Hello,',name) #Then prints then welcomes the user (letters the user has entered) 

def main():#the main part of my code is in a function to be able to call it at the end 
    
    print('The shape options which can be calculated are:')
    print('1) Sauare')
    print('2) Rectangle') 
    print('3) Triangle') 
    print('4) Circle')
    print('5) To quit the program enter "5"')

    print('To select a shape enter the number of the corresponding shape') 
    print('For example: to choose triangle enter "3"') 

    #The program asks the user to enter which shape to calculate only accept numbers 1-4


    def get_input(msg):#function which catches all user input which is invalid (not numbers) for all the shapes 
        """Get user input as int"""
        value = None
        while not value:
            value = input(msg)
            if not value.isnumeric():#if not a valid number print the following message
                print("Please enter a valid number")
                value = None
            else:
                return int(value)#once a correct number is entered the number is returned and program contiues

    while True:#creates a loop for the input from the user
        try:
            shape = int(input("Pick a shape and enter the corresponding number or quit:"))
        except ValueError:#
            print("Please enter a valid shape option")#if anything other than an integer is entered this message is printed 
            continue #once a number has been entered the program continues 
     

        if shape == 1:#user has inputted 1 
            print("You have choosen square!")
            length = get_input("Enter the length of a side: ")
            area = length * length#takes the numbers entered and multiplys them to give area and perimeter
            perimeter = 4 * length
            print("The area of the square is", area) #prints area and perimeter is in a statement instead of just the value
            print("The perimeter of the square is", perimeter)
            break #the loop breaks 

        elif shape == 2:#user has inputted 2 
            print("You have choosen rectangle!")
            length = get_input("Enter the length of a side: ")
            width = get_input("Enter the value of the width: ")
            area = length * width
            perimeter = 2 * (width + length)
            print("The area of the rectangle is", area)
            print("The perimeter of the rectangle is", perimeter)
            break

        elif shape == 3:#user has inputted 3
            print("You have choosen triangle!")
            base = get_input("Enter the length of the base: ")
            height = get_input("Enter the value of the height: ")
            side1 = get_input("Enter the length of a side: ")
            side2 = get_input("Enter the length of the other side: ")
            area = 0.5 * base * height
            perimeter = base + side1 + side2
            print("The area of the triangle is", area)
            print("The perimeter of the triangle is", perimeter)
            break

        elif shape == 4:#user has inputted 4 
            print("You have choosen circle!")
            radius = get_input("Enter the length of the radius: ")
            area = ( math.pi * radius * radius)
            perimeter = (2 * math.pi * radius)

            print("The area of the circle is", area)
            print("The circumference of the circle is", perimeter)
            break

        elif shape == 5:#user has inputted 5
            print("Goodbye!Hope you got the information you wanted")
            print('Come back to the area and perimeter calculator anytime :)')
            sys.exit()#the program exits the loop and function to quit
        
    print("Would you like to calculate another shape?")#at the end after calculations another opiton to quit 
    restart=input('To calculate another shape press "y" or to quit press any key:')
    if restart== "y":#if the input is y then the main function is called and the program runs again 
            main()
    else:#if the input if any key/thing other than y then the program prints messages 
        print('Goodbye,have a lovely day!')
        print('Come back to the area and perimeter calculator anytime :)')
        sys.exit()#the program quits out of function and ends
              
main()#the end of the main function 







































































