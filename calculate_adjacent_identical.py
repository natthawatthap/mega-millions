import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('clean_lottery_result.csv')

# Remove the "Date" column
df = df.drop(columns=['Date'])

# Flatten the dataframe into a single column
flat_df = df.values.flatten()

# Calculate the total count of numbers
total_count = len(flat_df)

# Calculate the count of adjacent identical numbers
adjacent_identical_count = 0
for i in range(1, total_count):
    if flat_df[i] == flat_df[i-1]:
        adjacent_identical_count += 1

# Calculate the percentage chance
percentage_chance = (adjacent_identical_count / total_count) * 100

# Plot the graph
labels = ['Non-adjacent Identical', 'Adjacent Identical']
counts = [total_count - adjacent_identical_count, adjacent_identical_count]
percentages = [(total_count - adjacent_identical_count) / total_count * 100,
               (adjacent_identical_count) / total_count * 100]

plt.bar(labels, percentages)
plt.xlabel('Identical Numbers')
plt.ylabel('Percentage')
plt.title('Percentage of Identical Numbers in Lottery Results')

# Display the percentage values on top of each bar
for i, v in enumerate(percentages):
    plt.text(i, v + 0.5, f'{v:.2f}%', ha='center')

plt.show()

# Display the percentage chance in log
print(f"Total Count: {total_count}")
print(f"Adjacent Identical Count: {adjacent_identical_count}")
print(f"Percentage Chance of Adjacent Identical Numbers: {percentage_chance:.2f}%")
