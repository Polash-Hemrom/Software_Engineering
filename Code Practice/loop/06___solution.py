# Factorial Calculator

numbers = int(input('Enter a numbers: '))
factorial = 1

while numbers > 0:
    factorial *= numbers
    numbers -= 1

print('Factorial Numbers: ', factorial)