import pyarrow.parquet as pq
import pandas as pd

# Read the Parquet file
table = pq.read_table('../child-mind-institute-detect-sleep-states/train_series.parquet')

# Convert to a Pandas DataFrame (if needed)
df = table.to_pandas()

# Save as CSV
# df.to_csv('data.csv', index=False)

df.head()

import polars as pl

pd.set_option('display.max_columns', None)  # Show all columns
