import random
import os
print(os.getcwd())

def generate_dataset(size, mode):
    if mode == 'sorted':
        return list(range(1, size+1))
    elif mode == 'random':
        return [random.randint(1, size) for _ in range(size)]
    elif mode == 'reversed':
        return list(range(size, 0, -1))
    else:
        raise ValueError("Mode harus 'sorted', 'random', atau 'reversed'")

# Generate datasets
sizes = [200, 2000, 20000]
modes = ['sorted', 'random', 'reversed']

output_directory = "/Users/rafimadani/Downloads/"  # Change this to your desired output directory

for size in sizes:
    for mode in modes:
        dataset = generate_dataset(size, mode)
        with open(os.path.join(output_directory, f'dataset_{size}_{mode}.txt'), 'w') as file:
            file.write('\n'.join(map(str, dataset)))