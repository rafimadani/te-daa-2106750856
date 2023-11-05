import time
def clustered_binary_insertion_sort(input_list):
    """
    Sorts the given input list using the Clustered Binary Insertion Sort algorithm.

    Args:
        input_list: A list of elements to be sorted.

    Returns:
        A sorted list.
    """

    # Initialize the position pointer.
    pop = 0

    # Iterate over the input list.
    for i in range(1, len(input_list)):
        # Set the current element pointer.
        cop = i

        # Get the key of the current element.
        key = input_list[cop]

        # Determine whether the key is greater than or equal to the key at position POP.
        if key >= input_list[pop]:
            # Find the correct insertion position for the key using the binary_loc_finder() function.
            place = binary_loc_finder(input_list, pop + 1, cop, key)
        else:
            # Find the correct insertion position for the key using the binary_loc_finder() function, but with the start position of the search range set to 0 and the end position set to POP - 1.
            place = binary_loc_finder(input_list, 0, pop - 1, key)

        # Update the POP variable.
        pop = place

        # Insert the key at the insertion position.
        input_list = place_inserter(input_list, place, cop)

    # Merge the sorted clusters into a single sorted list.
    merged_list = []
    for i in range(len(input_list)):
        merged_list.append(input_list[i])

    return merged_list


def binary_loc_finder(input_list, start, end, key):
    """
    Finds the correct insertion position for the given key in the given input list using the binary search algorithm.

    Args:
        input_list: A list of elements to search.
        start: The start index of the search range.
        end: The end index of the search range.
        key: The key to search for.

    Returns:
        The index of the correct insertion position for the key.
    """

    while start <= end:
        middle = (start + end) // 2

        if input_list[middle] == key:
            return middle
        elif input_list[middle] < key:
            start = middle + 1
        else:
            end = middle - 1

    return start


def place_inserter(input_list, position, cop):
    """
    Inserts the element at the given cop position in the given input list at the given position.

    Args:
        input_list: A list of elements to insert the element at.
        position: The index of the position to insert the element at.
        cop: The index of the element to be inserted.

    Returns:
        A list with the element inserted at the given position.
    """

    temp = input_list[cop]
    for j in range(cop, position, -1):
        input_list[j] = input_list[j - 1]
    input_list[position] = temp

    return input_list



def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

file_path = ['dataset_200_random.txt', 'dataset_2000_random.txt', 'dataset_20000_random.txt',
             'dataset_200_sorted.txt', 'dataset_2000_sorted.txt', 'dataset_20000_sorted.txt',
             'dataset_200_reversed.txt', 'dataset_2000_reversed.txt', 'dataset_20000_reversed.txt'
             ] # Replace with the actual path of your file

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
        sorted_list = clustered_binary_insertion_sort(input_list)
        end_time = time.time()
        execution_time_cbis = (end_time - start_time) * 1000  # Konversi ke milliseconds
        if i%3 == 0 : jumlah_data = 200
        elif i%3 == 1 : jumlah_data = 2000
        if i%3 == 2 : jumlah_data = 20000
        print(f"Execution time (CBIS) {status} {jumlah_data} angka : {execution_time_cbis} ms")
