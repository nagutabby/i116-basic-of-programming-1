'''
A program that calculates 5! with loop andd stores its result in
red_box when it terminates
'''
red_box: int = 1 # Used to store the result of 5!
blue_box: int = 1 # Used as a loop variable
while blue_box < 5 or blue_box == 5:
    '''
    The two assignments are done while blue_box
    is less than or equal to 5
    '''
    red_box = red_box * blue_box # Store the product in red_box
    blue_box = blue_box + 1 # Increment the loop variable
print(f'red_box: {red_box}')
print(f'blue_box: {blue_box}')
