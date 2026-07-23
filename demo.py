# A very poorly written function
def calculate_sum(numbers):
    total = 0
    # Inefficient O(N^2) loop to find duplicates before summing
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                print("Found a duplicate!")
                
    # Bad variable naming and no error handling
    for x in numbers:
        total = total + x
        
    return total
