import pandas as pd
import matplotlib.pyplot as plt
import os

data_file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
print(data_file_path)

# 1. Load the dataset
# Uses a try-except block to handle cases where data.csv might not be found
try:
    df = pd.read_csv(data_file_path)
    print(df.head())
except FileNotFoundError:
    print(f"File not found at {data_file_path}")

# 2 Perform some basic analysis
print("\n Basic statistics:")
#print(df.describe())

# Calculate the average scores for each subject
df['average_score'] = df[['Math', 'Science', 'English', 'Art']].mean(axis=1)
print(f"\n--Average scores per subject---- = \n {df['average_score']}")

df


# 3 create some visualization
# Create a figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Plot 1 :Bar chart for Average Scores of students
axes[0].bar(df['Student'], df['average_score'], color ='blue')
axes[0].set_xlabel('Student' , fontsize=20)
axes[0].set_ylabel('Average Score', fontsize=20)
axes[0].set_title('Average Score of Students', fontsize=18)
axes[0].grid(axis='y' ,linestyle='--',alpha=0.7)
axes[0].tick_params(axis='x',rotation=45) # rotate x-axis labels for readability


# # Plot 2 Bar chart for Average Scores per subject
#
#
plt.tight_layout()
plt.show()
print("\n Analysis compleet and plot is displayed" )