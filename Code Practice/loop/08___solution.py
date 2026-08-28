# Prime Number Checker
     # check if number is prime.

number = int(input('Enter a number: '))
is_prime = True


if number > 1:
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
            break


    if is_prime:
        print('Prime')
    else:
        print('Not prime')

else:
    print('Not prime')