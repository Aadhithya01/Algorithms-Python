"""
The typical scenario of the Knapsack Problem involves a knapsack (or backpack) with a limited carrying capacity and a set of items,
each associated with a weight and a value. The objective is to determine the most valuable combination of items that can be accommodated
within the knapsack without exceeding its weight limit.
"""


# Given weights of items
weights = [8, 16, 32, 40]

# Given values of items
values = [50, 100, 150, 200]

# Knapsack capacity
w = 64

# Calculate value-to-weight ratios for each item
r = [values[i] / weights[i] for i in range(len(weights))]
print("Value-to-Weight Ratios:", r)

# Sort items based on value-to-weight ratio in descending order
index = list(range(len(weights)))
index.sort(key=lambda i: r[i], reverse=True)
print("Sorted Indices:", index)

# Initialize total value
val = 0

# Fill the knapsack using a greedy approach
for i in index:
    if weights[i] <= w:
        val += values[i]
        w -= weights[i]
    else:
        # Fractional part of item can be taken
        temp = w / weights[i]
        val += (temp * values[i])

# Print the maximum value that can be obtained
print("Maximum Value in Knapsack:", val)
