# Experiment 2: Complexity Drill (Operation Counting)
# Time complexity measures how the running time of an algorithm increases with input size.
# Time Complexity = O(n)
# Space Complexity:
# Space complexity measures how much memory an algorithm uses.



# -----------------------------
# 1. Single Loop -> O(n)
#A single loop runs n times.
# -----------------------------
def single_loop(n):
    count = 0 
    for i in range(n):
        count += 1
    print("Single Loop Operations:", count)
    print("Complexity: O(n)")
    print("Reason: Loop runs n times\n")


# -----------------------------
# 2. Nested Loop -> O(n^2)
# Two loops each running n times.
# Total operations = n × n
# Time Complexity = O(n²)
# -----------------------------
def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("Nested Loop Operations:", count)
    print("Complexity: O(n^2)")
    print("Reason: n * n operations\n")

# -----------------------------
# 3. Triangular Loop -> O(n^2)
#The outer loop runs n times and the inner loop runs (i+1) times.
# It counts total operations: n(n+1)/2.
# Hence, the time complexity is O(n^2)
# -----------------------------
def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
    print("Triangular Loop Operations:", count)
    print("Complexity: O(n^2)")
    print("Reason: n(n+1)/2 ≈ n^2/2 → O(n^2)\n")


# -----------------------------
# 4. Halving Loop -> O(log n)
# The value is divided by 2 in every step.
# Number of steps = log n
# Time Complexity = O(log n)
# -----------------------------
def halving_loop(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    print("Halving Loop Operations:", count)
    print("Complexity: O(log n)")
    print("Reason: Value reduces by half each time\n")


# -----------------------------
# Linear Search
#It checks each element one by one until the key is found.
# Best case: O(1) when the first element matches.
# Worst case: O(n) when the key is last or not present.
# It counts the number of operations performed.
# -----------------------------
def linear_search(arr, key):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == key:
            print("Linear Search Found at index:", i)
            print("Operations:", count)
            return
    print("Linear Search Not Found")
    print("Operations:", count)


# -----------------------------
# Binary Search
#It repeatedly divides the search space into half.
# Best case: O(1) when the middle element matches.
# Worst and average case: O(log n).
# It counts the number of operations performed.
# -----------------------------
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Binary Search Found at index:", mid)
            print("Operations:", count)
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Binary Search Not Found")
    print("Operations:", count)

# Main Execution
n = int(input("Enter value of n: "))
print(f"--- Complexity Snippets ---")

single_loop(n)
nested_loop(n)
triangular_loop(n)
halving_loop(n)

print(f"--- Search Comparisons ---")

arr = list(range(1, n+1))  # Sorted array

key = int(input("Enter key to search: "))

print("\nLinear Search:")
linear_search(arr, key)

print("\nBinary Search:")
binary_search(arr, key)