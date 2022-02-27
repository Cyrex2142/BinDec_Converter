#global variables for functionality.
decimal_result = 0
decNumSave = 0
#function to output author details
def display_details():
    print("File     : Allby005_inbetween.py")
    print("Author   : Bradley Allison")
    print("Stud ID  : 110130836")
    print("Email ID : allby005")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    
#decimal to binary conversion.
def convert_to_binary(decimal_number):
    #variable list to stare modulo values.
    calcNum = []
    #check that decimal number is greater than zero and divisible.
    while decimal_number != 0:
        #divide decimal by 2 to step through conversion.
        quotient = int(decimal_number / 2)
        #append the remainder (1 or 0) to the calculation list.
        calcNum.append(int(decimal_number % 2))
        #update the decimal with the next conversion step.
        decimal_number = int(quotient)
    #set up variables for reversing the calculated remainders to print accurate binary.    
    binLength = len(calcNum)
    #set up list for final output number and index to reverse entries.
    swap = binLength
    binNum =[]
    #for loop to swap the orer of the binary signals.
    for val in calcNum:
        binNum.append(val)
    for val in calcNum:
        swap = swap - 1
        binNum[swap] = val
        
    #Strip list formatting from the binary result
    binPrint = ''
    for x in binNum:
        binPrint += str(x)

    return binPrint


def convert_to_decimal(binary_number):
    binary_number = str(binary_number)
    global decimal_result
    binary_digits = []
    decimal_conversion_list = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8]
    index = 0
    for x in binary_number:
        binary_digits.append(int(x))
    for val in binary_digits:
        if val == 1:
            decimal_result = decimal_result + decimal_conversion_list[index]    
        index += 1
    decimal_result = decimal_result * 2
    return decimal_result


def binary_count(count_number):
    stop = 1
    while stop <= int(count_number):
        bin_count = convert_to_binary(stop)
        print("Decimal = " + str(stop) + " " + "Binary = " + str(bin_count))
        bin_index = ''
        bin_final = ''
        for y in bin_count:
            bin_index = y
            bin_final = bin_final + bin_index
        stop += 1
    return stop


print("*** Menu ***")
print()
print("1. Convert to binary.")
print("2. Convert to decimal.")
print("3. Binary Counting.")
print("4. Quit.")
print()
menu_choice = input("What would you like to do [1, 2, 3, 4]? ")
while menu_choice.isdigit() != True:
    menu_choice = input("Invlaid choice, Please enter either: '1', '2', '3' or '4': ")
    
else:
    menu_choice = int(menu_choice)
    
    while menu_choice < 1 or menu_choice > 4:
        menu_choice = int(input("Invlaid choice, Please enter either: '1', '2', '3' or '4': "))
    else:
        if menu_choice == 1:
            print()
            print("In command 1 - Convert to Binary.")
            print()
            decimal_number = input("Please enter a decimal number: ")
            #validation loop so make sure user input is a number.
            while decimal_number.isdigit() != True:
                decimal_number = input("Please make sure you're number contains the digits 1-9 only: ")
            else:
                #converting user string to integer for further validation and calculation.
                decimal_number = int(decimal_number)
                #ensureing user input is a divisible number.
                while decimal_number <= 0:
                    if decimal_number <= 0: 
                        decimal_number = int(input("Please enter a number greater than 0: "))
                else:
                    if decimal_number > 0:
                        decimal_number = int(decimal_number)
                        Bin_num = convert_to_binary(decimal_number)
                        convert_to_binary(decimal_number)
                        print("Binary: " + str(Bin_num))
            
        if menu_choice == 2:
            print()
            print("In command 2 - Convert to Decimal.")
            print()
            binary_number = input("Please enter a binary number: ")
            #validation loop to enure input is a number.
            while binary_number.isdigit() != True:
                binary_number = input("Please make sure you're number contains the digits 1-0 only: ")
            else:
                #converting to int for validation and calc again.
                binary_number = int(binary_number)
                #ensuring the value is binary i.e. only 1 or 0 values.
                while binary_number <= 0 or binary_number < 2:
                    binary_number = input("Please make sure your number contains the digits 0-1 only: ")
                    binary_numer = int(binary_number)
                else:
                    binNumSave = binary_number
                    decimal_result = convert_to_decimal(binary_number)
                print("Decimal number: " + str(decimal_result))
            
        elif menu_choice == 3:
            print()
            print("In command 3 - Binary Counting")
            count_number = input("What number would you like to count up to? ")
            
            binary = binary_count(count_number)

            
        elif menu_choice == 4:
            print()
            print("Command 4 - Quit.")
            print()
            display_details()
            print()
            print("*** Goodybe! ***")




    
