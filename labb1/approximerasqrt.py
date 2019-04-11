
    # iterations = 0 
    # while guess != 0:
    #     guess = guess - ((guess**2 - k)/(2 * guess))
    #     if guess / (guess + ((guess**2 - k)/(2 * guess))) < 0.000005:
    #         print('Nr of iterations:', iterations)
    #         print(guess)
    #         break
    #     iterations += 1
    # print('Error: Divide by zero is illegal!')
    # return 0    
    
def sqrt_Newton(k, guess):
    iterations = 0
    while guess != 0:
        if k**0.5 == guess:
            print('Nr of iterations:', iterations)
            break
        if  abs(guess - (guess + (guess**2 - k)/(2 * guess))) < 0.000005:
            iterations += 1
            print('Nr of iterations:', iterations)
            break
        guess = guess - ((guess**2 - k)/(2 * guess))
        iterations += 1
    if guess == 0:
        print('Error: Divide by zero is illegal!')
    return guess