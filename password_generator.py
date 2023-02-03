"""

A Simple CUI password generator made using
python with the help of 'random' module

This tool contains topic about both
for loop , function , file handling
and random module usage referrence

Made by d4t4 (AKA Dini)

"""

import random

#Performs password generation operation

def operation(user_input):
    global password
    
    for x in range(user_input):
        l = random.randint(0,2)
        if l == 0:
            a = random.randint(0,25)
            password = password + upper_case[a]
        elif l == 1:
            b = random.randint(0,25)
            password = password + lower_case[b]
        else:
            c = random.randint(0,9)
            password = password + number[c]

    print("Generated password is : " + password)

    #To save password in a text file
    save_password = input("Do you want to save the password in a text file (Y/N) ? : ")
    if save_password == "Y" or save_password == "y":
        with open("password.txt","w") as file: #Edit file name if needed
            file.write(password)
            print("File created")
            print("File name : password.txt")
            
    else:
        exit(1) #Quits the program

#Initial start of an program

def main():
    global password , upper_case , lower_case , number
        
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case = list(upper_case)

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    lower_case = list(lower_case)

    number = "1234567890"
    number = list(number)

    password = ""

    user_input = int(input("Enter the lenght of the character : " ))    #Enter the length of the password needed

    operation(user_input)


main()
