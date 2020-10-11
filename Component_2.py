#Component 2
#Ask the user to enter the correct measurements for the shape length,width etc..
#Check the number inputted is a whole number, no negative numbers

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

while True:#creates a loop for the input from the user 
    try:
        shape = int(input("Pick a shape and enter the corresponding number:"))
    except ValueError:#
        print("Please enter a valid number")#if anything other than an integer is entered this message is printed 
        continue #once a number has been entered the program continues 

    if shape == 1:#user has inputted 1 
       print("You have choosen square!")
       side = input("Enter the length of a side: ")
       while not side.isnumeric():#allows for inputs which are only whole numbers 
           side = input("Please enter a valid number for the length: ")#this error mesages shows
           #the user must enter a vlaid number for the program to continue
       break
       
    elif shape == 2:#user has inputted 2
       print("You have choosen rectangle!")
       side = input("Enter the length of a side: ")
       while not side.isnumeric():#allows for inputs which are only whole numbers 
           side = input("Please enter a valid number for the length: ")
           
       side = input("Enter the value of the width: ")
       while not side.isnumeric():
           side = input("Please enter a valid number for the width: ")
       break
 
    elif shape == 3:#user has inputted 3
         print("You have choosen triangle!")
         side = input("Enter the length of the base: ")  
         while not side.isnumeric():#allows for inputs which are only whole numbers 
           side = input("Please enter a valid number for the base: ")
           
         side = input("Enter the value of the height: ")
         while not side.isnumeric():#allows for inputs which are only whole numbers 
           side = input("Please enter a valid number for the height: ")
         break

    elif shape == 4:#user has inputted 4 
         print("You have choosen circle!")
         side = input("Enter the length of the radius: ")
         while not side.isnumeric():#allows for inputs which are only whole numbers 
           side = input("Please enter a valid number for the length: ")
         break


#break means to exit the loop so the length/s have been entered correctly 




