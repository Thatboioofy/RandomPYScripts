import random

# Initialize the list to keep track of counts
counts = [0] * 11

# Simulate rolling two dice 200 times
for i in range(200):
    num = random.randint(1, 6) + random.randint(1, 6)
    get = num - 2
    counts[get] += 1

# Print the results
for i in range(11):
    print(i + 2, counts[i])

# Find and print the sum with the highest count
max_count = max(counts)
max_index = counts.index(max_count)
print(f"The sum with the highest count is {max_index + 2} with {max_count} occurrences.")
