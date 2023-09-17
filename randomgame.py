# Generate a number 1-10
from random import randint

random_num = randint(1, 10)


# Ask a input from user
while True:
    try:
        user_num = int(input('Enter a number between 1-10 :'))
        if 1 <= user_num <= 10:
            if user_num == random_num:
                print('Your guess is correct')
            else:
                print(
                    f'Entered number is {user_num} and genertaed number is {random_num}')
                continue
        else:
            print('Number should between 1-10')

    except ValueError:
        print('Please enter a valid integer number')
    else:
        break


# Check that input is from 1-10


# Check whether number is right guess else ask him again
