#Component 3
#From the users input calculate the area and perimeter

import math #import math module to be able to do calculuations for example: the vaue of pi

print('*****Welcome to the area and perimeter calculator!*****')

name = input('What is your name?') #program stores name and name is a variable 
print ('Hello,',name) #Then prints then welcomes the user (letters the user has entered) 

print('The shape options which can be calculated are:')
print('1) Sauare')
print('2) Rectangle') 
print('3) Triangle') 
print('4) Circle')

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
        shape = int(input("Pick a shape and enter the corresponding number:"))
    except ValueError:#
        print("Please enter a valid shape option")#if anything other than an integer is entered this message is printed 
        continue #once a number has been entered the program continues 
 

    if shape == 1:#user has inputted 1 
        print("You have choosen square!")
        length = get_input("Enter the length of a side: ")
        area = length * length #takes the numbers entered and multiplys them to give area and perimeter 
        perimeter = 4 * length
        print("The area of the square is", area) #prints area and perimeter is statement instead of just the value 
        print("The perimeter of the square is", perimeter)
        break #the code breaks an the program ends 

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
        area = ( math.pi * radius * radius) #for the circle the value of pi is taken from the math import to calculate 
        perimeter = (2 * math.pi * radius)

        print("The area of the circle is", area)
        print("The circumference of the circle is", perimeter)
        break


#the function at the start of the program is mure more efficent than having the "isnumeric" line in component
#and it reduces the need to repeat the same code more than once 




