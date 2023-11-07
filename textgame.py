async def textgame():
    user_input = input("what is your name?\n")
    print(f'hello {user_input}, nice to meet you.')
    user_input = input('Would you like to get this sword? (Y/N)\n')

    while user_input not in ('Y', 'N'):
        print('Please put in Y for yes or N for no!')
        user_input = input('Would you like to get this sword? (Y/N)\n')

    response = None

    if user_input == 'Y':
        response = True
    else:
        response = False
    if(response is True):
        print('You took the sword!')
    else: print('you did not that the sword!')