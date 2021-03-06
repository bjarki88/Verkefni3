pass_word = input('Enter a new password: ')

incorrect = 0
valid = 0

while pass_word != 'q': # Create a constant so that if the user presses q it ends the loop
    upper_case = False
    lower_case = False
    number = False
    if 6 <= len(pass_word) <= 20: # Create the range that the string must fall under
        for i in pass_word:            # Create a for loop so that we can find what is missing or not missing in the input
            if i.isupper():
                upper_case = True      # True if not q so that the loop continues 
            elif i.islower():
                lower_case = True
            elif i.isdigit():
                number = True

        if not lower_case:
            print('At least one lower case letter needed')
        if not upper_case:
            print('At least one upper case letter needed')
        if not number:
            print('At least one number needed')
        if number and lower_case and upper_case:
            valid = valid + 1                # Create a correct count
            print('Valid password of length', len(pass_word))
        else:
            incorrect = incorrect + 1     # Create an incorrect count
    else:
        print('Invalid length')
        incorrect = incorrect + 1
    pass_word = input('Enter a new password: ')

print('You tried {} passwords, {} valid, {} invalid'.format((valid + incorrect), valid, incorrect))