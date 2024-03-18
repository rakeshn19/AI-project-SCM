import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'X'],
    'Value': [10, 20, 15, 25, 5, 30, 40, 35],
    'Value1': [10, 20, 15, 25, 5, 30, 40, 35]
}
df = pd.DataFrame(data)

# Group by 'Category' and 'Subcategory', calculate mean, and reset index
grouped_mean = df.groupby(['Category', 'Subcategory']).mean().reset_index()

print(grouped_mean.head())
