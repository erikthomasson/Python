def is_prime(number):
    x = 2
    while x != number + 1:
        if number > 1 and x > 1 and number == x:
            print('True')
        if number > 1 and x > 1 and number % x == 0 and number != x:
            print('False')
            break
        x += 1