import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('clean_lottery_result.csv')

# Remove the "Date" column
df = df.drop(columns=['Date'])

# Initialize an empty dictionary to store the count of repeating numbers for each column
repeating_counts = {}

# Iterate over each column (except the Date column)
for column in df.columns:
    # Count the occurrence of each number in the column
    number_counts = df[column].value_counts()
    
    # Check if there are any repeating numbers in the column
    repeating_numbers = number_counts[number_counts > 1]
    
    # Calculate the count of repeating numbers in the column
    repeating_count = repeating_numbers.sum()
    
    # Add the count to the repeating_counts dictionary
    repeating_counts[column] = repeating_count

# Calculate the total count of numbers in all columns
total_count = sum(repeating_counts.values())

# Calculate the percentage of repeating numbers in each column
percentages = {column: (count / total_count) * 100 for column, count in repeating_counts.items()}

# Display the percentage of repeating numbers in each column in log
print(f"Total Count: {total_count}")
print("Percentage of Repeating Numbers in Each Column:")
for column, percentage in percentages.items():
    print(f"{column}: {percentage:.2f}%")
    
# Plot the graph
plt.bar(percentages.keys(), percentages.values())
plt.xlabel('Columns')
plt.ylabel('Percentage')
plt.title('Percentage of Repeating Numbers in Each Column')

# Display the percentage values on top of each bar
for column, percentage in percentages.items():
    plt.text(column, percentage + 0.5, f'{percentage:.2f}%', ha='center')

plt.show()


