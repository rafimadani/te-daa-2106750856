# Python implementation QuickSort using 
# Lomuto's partition Scheme.
import random
import time
'''
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
def quicksort(arr, start , stop):
	if(start < stop):
		
		# pivotindex is the index where 
		# the pivot lies in the array
		pivotindex = partitionrand(arr,\
							start, stop)
		
		# At this stage the array is 
		# partially sorted around the pivot. 
		# Separately sorting the 
		# left half of the array and the
		# right half of the array.
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

# This function generates random pivot,
# swaps the first element with the pivot 
# and calls the partition function.
def partitionrand(arr , start, stop):

	# Generating a random number between the 
	# starting index of the array and the
	# ending index of the array.
	randpivot = random.randrange(start, stop)

	# Swapping the starting element of
	# the array and the pivot
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)

'''
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
	pivot = start # pivot
	
	# a variable to memorize where the 
	i = start + 1
	
	# partition in the array starts from.
	for j in range(start + 1, stop + 1):
		
		# if the current element is smaller
		# or equal to pivot, shift it to the
		# left side of the partition.
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
        execution_time_cbis = (end_time - start_time) * 1000  # Konversi ke milliseconds
        if i%3 == 0 : jumlah_data = 200
        elif i%3 == 1 : jumlah_data = 2000
        if i%3 == 2 : jumlah_data = 20000
        print(f"Execution time (R.Quicksort) {status} {jumlah_data} angka : {execution_time_cbis} ms")

# This code is contributed by soumyasaurav
