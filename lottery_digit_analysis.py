import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('clean_lottery_result.csv')

# Remove the "Date" column
df = df.drop(columns=['Date'])

# Count the number of digits for each column
digit_counts = df.astype(str).apply(lambda x: x.str.len())

# Count the total occurrences of each digit
digit_occurrences = digit_counts.stack().value_counts()

# Calculate the percentage of each digit
digit_percentages = (digit_occurrences / digit_occurrences.sum()) * 100

# Plot the graph
plt.bar(digit_percentages.index, digit_percentages)
plt.xlabel('Digits')
plt.ylabel('Percentage')
plt.title('Percentage of Digits in Lottery Results')
plt.show()
