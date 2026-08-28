# 7. Validate Input
    # Keep asking the user for input untill they enter a number between 1 and 10

while True:
    numbers = int(input('Enter a number: '))
    if 1 <= numbers <= 10:
        print('valid number')
        break

    else:
        print('Invalid numbers')