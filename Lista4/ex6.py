import random

# Initialize variables
min_value = 101
max_value = 0
total_sum = 0

# Generate 5 random numbers
for i in range(5):
    random_number = random.randint(0, 100)
    total_sum += random_number

    # Update minimum and maximum values
    if random_number < min_value:
        min_value = random_number
    if random_number > max_value:
        max_value = random_number

# Calculate average value
average_value = total_sum / 5

# Print results
print("Menor valor:", min_value)
print("Maior valor:", max_value)
print("Média dos valores:", average_value)
