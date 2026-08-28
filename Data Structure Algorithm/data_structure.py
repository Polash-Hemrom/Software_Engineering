import time


data_list = list(range(1_000_000))
data_set = set(range(1_000_000))
target = 999_999

start = time.time()
found = target in data_set
list_time = time.time() - start


start = time.time()
found = target in data_set
set_time = time.time() - start


print(f'Time to search the list{list_time:.6f}s')
print(f'Time to search the list{set_time:.6f}s')
print(f'{list_time / set_time:.0f}')