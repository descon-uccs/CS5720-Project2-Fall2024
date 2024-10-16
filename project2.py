import random
import time
import matplotlib.pyplot as plt

# Insertion sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge function for merge sort
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

# Hybrid sort implementation
def hybrid_sort(arr, K):
    if len(arr) <= K:
        return insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left = hybrid_sort(arr[:mid], K)
        right = hybrid_sort(arr[mid:], K)
        return merge(left, right)

# Function to run time experiments
def run_time_experiment(K_values, n_values, num_trials=5, sorted_input=False):
    avg_times = {n: [] for n in n_values}
    for n in n_values:
        for K in K_values:
            total_time = 0
            for _ in range(num_trials):
                if sorted_input:
                    arr = sorted(random.sample(range(1000000), n))
                else:
                    arr = random.sample(range(1000000), n)
                start_time = time.time()
                hybrid_sort(arr, K)
                total_time += time.time() - start_time
            avg_times[n].append(total_time / num_trials)
    return avg_times

# Finding optimal K for different n values
def find_optimal_k(avg_times, K_values, n_values):
    optimal_ks = []
    for n in n_values:
        min_time = min(avg_times[n])
        optimal_k = K_values[avg_times[n].index(min_time)]
        optimal_ks.append(optimal_k)
    return optimal_ks

# Plotting functions
def plot_results(avg_times, K_values, n_values, filename, title):
    for n in n_values:
        plt.plot(K_values, avg_times[n], label=f"n={n}")
    plt.xlabel("K")
    plt.ylabel("Average Running Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_optimal_k(optimal_ks, n_values, filename):
    plt.plot(n_values, optimal_ks, marker='o')
    plt.xlabel("Array Size (n)")
    plt.ylabel("Optimal K")
    plt.title("Optimal K as a Function of Array Length")
    plt.savefig(filename)
    plt.close()

# Example experiment settings
K_values = list(range(2, 51, 5))  # K from 2 to 50 with step 5
n_values = [1000, 5000, 10000, 20000]  # Array lengths

# 1. Run experiments on random arrays
avg_times_random = run_time_experiment(K_values, n_values)

# Save the plot for random array results
plot_results(avg_times_random, K_values, n_values, "random_results.png", "Average Running Time on Random Arrays")

# 2. Identify optimal K for each n on random arrays
optimal_ks_random = find_optimal_k(avg_times_random, K_values, n_values)

# Save the plot for optimal K on random arrays
plot_optimal_k(optimal_ks_random, n_values, "optimal_k.png")

# 3. Run experiments on sorted arrays
avg_times_sorted = run_time_experiment(K_values, n_values, sorted_input=True)

# Save the plot for sorted array results
plot_results(avg_times_sorted, K_values, n_values, "sorted_results.png", "Average Running Time on Sorted Arrays")

# 4. Identify optimal K for sorted arrays
optimal_ks_sorted = find_optimal_k(avg_times_sorted, K_values, n_values)

# Save the plot for optimal K on sorted arrays
plot_optimal_k(optimal_ks_sorted, n_values, "optimal_k_sorted.png")
