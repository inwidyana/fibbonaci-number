def fib(userInput):
    if(userInput == 0):
        return 0
    elif(userInput == 1):
        return 1
    return fib(userInput - 1) + fib(userInput - 2)

userInput = input('Please enter a number: ')
print('The ' + str(userInput) + 'th fibbonaci number is: ' + str(fib(int(userInput))))