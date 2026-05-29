# This file explains what Pandas is and how to create a 1-dimensional array called a Series.

import pandas as pd

data_list = [10, 20, 30, 40, 50]
my_series = pd.Series(data_list)

print("--- my First Pandas Series ---")
print(my_series)