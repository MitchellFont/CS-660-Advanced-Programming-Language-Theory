# Mitchell Fontaine
# CS-660
# 03/20/2026

import time
import tracemalloc
import random
import copy
import sys

# Increase recursion depth for Quick Sort on large datasets
sys.setrecursionlimit(200000)

# Sorting Algorithms

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Benchmarking Module

def benchmark_sort(sort_func, input_data, iterations=3):
    """
    Runs a sorting function multiple times and calculates average time and peak memory.
    """
    total_time = 0
    peak_memory_overall = 0

    print(f"Benchmarking {sort_func.__name__} over {iterations} iterations...")

    for i in range(iterations):
        # Deep copy to ensure we sort a fresh, unsorted list every iteration
        data_copy = copy.deepcopy(input_data)
        
        tracemalloc.start()
        start_time = time.perf_counter()
        
        # Execute the sort
        sort_func(data_copy)
        
        end_time = time.perf_counter()
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        iteration_time = end_time - start_time
        total_time += iteration_time
        peak_memory_overall = max(peak_memory_overall, peak_mem)
        
    avg_time = total_time / iterations
    peak_mb = peak_memory_overall / (1024 * 1024)
    
    print(f"  -> Average Time: {avg_time:.4f} seconds")
    print(f"  -> Peak Memory : {peak_mb:.4f} MB\n")
    
    return avg_time, peak_mb

# Execution / Testing
if __name__ == "__main__":
    # Generate 100,000 random integers
    dataset_size = 100000
    print(f"Generating dataset of {dataset_size} random integers...\n")
    test_data = [random.randint(0, 1000000) for _ in range(dataset_size)]
    
    # Run benchmarks
    benchmark_sort(quick_sort, test_data, iterations=3)
    benchmark_sort(merge_sort, test_data, iterations=3)
    benchmark_sort(heap_sort, test_data, iterations=3)