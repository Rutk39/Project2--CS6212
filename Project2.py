import heapq
import random
import time

def merge_lists(arr):
    min_heap = [(size, i) for i, size in enumerate(arr)]
    heapq.heapify(min_heap)
    
    merge_sequence = []
    total_cost = 0
    
    while len(min_heap) > 1:
        size1, index1 = heapq.heappop(min_heap)
        size2, index2 = heapq.heappop(min_heap)
        
        total_cost += size1 + size2
        merge_sequence.append((index1, index2))
        
        heapq.heappush(min_heap, (size1 + size2, index1))
    
    return merge_sequence, total_cost

# Generate a random list of sizes
random.seed(42)
list_sizes = [random.randint(1, 100) for _ in range(1000000)]

# Measure the time it takes to execute the algorithm
start_time = time.time()
merge_sequence, total_cost = merge_lists(list_sizes)
end_time = time.time()

print("Merge sequence:", merge_sequence[:1000000])  # Print the first 10 merge operations
print("Total cost:", total_cost)
print("Execution time:", end_time - start_time, "seconds")
