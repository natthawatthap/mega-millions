import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('clean_lottery_result.csv')

# Remove the "Date" column
df = df.drop(columns=['Date'])

# Flatten the dataframe into a single column
flat_df = df.values.flatten()

# Concatenate all values into a single string
all_values = ''.join(map(str, flat_df))

# Count the occurrence of each digit
digit_counts = {}
for digit in range(10):
    digit_counts[str(digit)] = all_values.count(str(digit))

# Convert the dictionary to a DataFrame
digit_counts_df = pd.DataFrame.from_dict(digit_counts, orient='index', columns=['Count'])
digit_counts_df.index.name = 'Digits'

# Calculate the percentage of each digit
digit_percentages = (digit_counts_df['Count'] / digit_counts_df['Count'].sum()) * 100

# Find the digit with the largest percentage
largest_digit = digit_percentages.idxmax()

# Plot the graph
plt.bar(digit_percentages.index, digit_percentages)
plt.xlabel('Digits')
plt.ylabel('Percentage')
plt.title('Percentage of Digits in Lottery Results')

# Display the exact percentage values on top of each bar
for i, v in enumerate(digit_percentages):
    plt.text(i, v + 0.5, f'{v:.2f}%', ha='center')

# Highlight the bar with the largest percentage
largest_index = digit_percentages.index.get_loc(largest_digit)
plt.bar(largest_index, digit_percentages[largest_index], color='red')

plt.xticks(range(10))
plt.show()
