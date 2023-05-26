import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('clean_lottery_result.csv')

# Define the columns of interest
columns = ['1st', '2T', '3T', '2L', '3F3L(1)', '3F3L(2)', '3F3L(3)', '3F3L(4)']

# Iterate over each digit
for digit in range(10):
    # Create a new figure and plot the graph for the current digit
    fig, ax = plt.subplots()
    
    # Count the occurrence of the digit in each column
    digit_counts = {column: str(df[column]).count(str(digit)) for column in columns}
    
    # Calculate the total count of digits in all columns
    total_count = sum(digit_counts.values())
    
    # Calculate the percentage for each column
    column_percentages = [count / total_count * 100 for count in digit_counts.values()]
    
    # Prepare data for the graph
    column_labels = list(digit_counts.keys())
    
    # Find the index of the column with the highest percentage
    highest_percentage_index = column_percentages.index(max(column_percentages))
    
    # Plot the graph
    bars = ax.bar(column_labels, column_percentages, color=['skyblue' if i != highest_percentage_index else 'salmon' for i in range(len(column_labels))])
    ax.set_xlabel('Column')
    ax.set_ylabel('Percentage')
    ax.set_title(f'Percentage of Digit {digit} in Columns')
    ax.set_xticks(range(len(column_labels)))
    ax.set_xticklabels(column_labels)
    
    # Display the percentage values on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:.2f}%', ha='center')
    
    # Show the graph
    plt.show()

    # Display the log with the column with the highest percentage
    highest_percentage_column = column_labels[highest_percentage_index]
    print(f"For digit {digit}: Column with highest percentage is '{highest_percentage_column}'")
