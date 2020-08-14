#A function to output the fibbonacci sequence of a given number
#===========
def user_enter_digit (z):
    z = input("Please enter a  number to create a fibbonacci sequence: ")  # Receive user input
    while not z.isdigit():  # If the number is not a digit, insist on getting a digit
        z = input("Please enter digits only: ")
    print("\tYour number is: ", z)
    z = int(z)  # Converted the digit string to type = int
    return z

#===============================
def fibbonacci_sequence (z,x,y):

    while y<z:
        print(y)
        x,y = y,x+y

max_digit = user_enter_digit (0)
fibbonacci_sequence (max_digit,0,1)

