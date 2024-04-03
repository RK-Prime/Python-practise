def calculator(head_msg):
    print(head_msg)

    print("\nOperators =>\nAddition : \" + \" ,\nSubtraction : \" - \" ,\nMultiplication : \" * \" ,\nDivision : \" / \" ,\nPower : \" ^ \"")

    num1 = int(input('\nEnter the first number : '))
    operator = input('Enter the operator : ')
    num2 = int(input('Enter the second number : '))

    print('\n<----> RESULT <---->\n')
    if operator == '+':
        print(f'Addition : {num1 + num2}\n')
    elif operator == '-':
        print(f'Subtraction : {num1 - num2}\n')
    elif operator == '*':
        print(f'Multiplication : {num1 * num2}\n')
    elif operator == '/':
        print(f"Division : \nQuotient : {num1 / num2}\nRemainder : {num1 % num2}\n")
    elif operator == '^':
        print(f'{num1} to the power {num2} is : {num1 ** num2}\n')
    else:
        print('\n<----><---ERROR---><---->\n')
        print('\nThere was an error encountered\nplease refresh the program')


def execution(head_msg='<----> Calculator Program <---->'):
    print(head_msg)
    
    print('\nPrompts :\nE/e = Start program execution,\nR/r = Refresh the program,\nQ/q = Quit the program')
    prompt_var = input('\nEnter your prompt : ')

    if prompt_var == 'E' or prompt_var == 'e':
        print('Starting the program execution....')
        calculator('Execution Started')
        execution()

    elif prompt_var == 'R' or prompt_var == 'r':
        print('Refreshing the program...')
        execution('Refreshed program')

    elif prompt_var == 'Q' or prompt_var == 'q':
        print('Qutting the program')
        exit()

    else:
        print('<----> ERROR <---->')
        print('Program exit')


# <------> Calling the Function <------>#
try:
    execution()
except ValueError:
    print('<---> ValueError <---->')
    print('Note : Please refresh the program\nand review the values you have entered')
except InterruptedError:
    print('<----> InterruptedError <---->')
    print('Note : Please refresh the program\nand try not to interrupt the program while execution')
