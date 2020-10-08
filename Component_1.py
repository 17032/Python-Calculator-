#Component 1
#Asks the users name and
#Print the instructions for the program 
#Ask the user which shape they would like to calculate

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
        shape = int(input("Pick a shape and enter the corresponding number:"))#input message 
    except ValueError:
        print("Please enter a valid number")#if anything other than an integer is entered this message is printed 
        continue #once a number has been entered the program continues 

    if shape < 1:#if shape is less than one print the following user has entered invalid input 
        print("Your response is not valid.Please enter a valid number")
        continue #once a number has been entered the program continues 

    elif shape > 4:
        print('Please enter a valid option number')#if shape is more than 4 means the input is invalid print following
    else:
        #shape number was successfully entered and the number is correct 
        #exit the loop.
        break
