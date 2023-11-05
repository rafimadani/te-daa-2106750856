import resource
import random
import time
import psutil
def quicksort(arr, start , stop):
	if(start < stop):
		

		pivotindex = partitionrand(arr,\
							start, stop)
		
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):
	randpivot = random.randrange(start, stop)
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)

def partition(arr,start,stop):
	pivot = start # pivot
	
	i = start + 1
	
	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =\
			arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

file_path = ['dataset_200_random.txt', 'dataset_2000_random.txt', 'dataset_20000_random.txt',
             'dataset_200_sorted.txt', 'dataset_2000_sorted.txt', 'dataset_20000_sorted.txt',
             'dataset_200_reversed.txt', 'dataset_2000_reversed.txt', 'dataset_20000_reversed.txt'
             ]

# Read numbers from the file
for i in range(len(file_path)):
    if i == 0 : status = "random"
    if i == 3 : status = "sorted"
    if i == 6 : status = "reversed"
    input_list = read_numbers_from_file(file_path[i])
    if __name__ == '__main__':
        # Create a test list.
        # Sort the list using the CBIS algorithm.
        start_time = time.time()
        quicksort(input_list, 0, len(input_list) - 1)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Konversi ke milliseconds
        memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024 
        if i%3 == 0 : jumlah_data = 200
        elif i%3 == 1 : jumlah_data = 2000
        if i%3 == 2 : jumlah_data = 20000
        print(f"Execution time (R.Quicksort) {status} {jumlah_data} angka : {execution_time} ms")
        print(f"Memory usage (R.Quicksort) {status} {jumlah_data} angka : {memory_usage} ")

