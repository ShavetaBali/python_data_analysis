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
print(df.describe())

# 3 create some visualization




