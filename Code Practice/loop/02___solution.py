# 2. Sum of Even Numbers

n = 20
sum_even = 0

for i in range (1, n + 1):
    if i % 2 == 0:
        sum_even += 1

print('Sum even number: ', sum_even)