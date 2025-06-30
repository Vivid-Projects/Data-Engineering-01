import pandas as pd

#df = pd.read_csv('crime.csv')

import pandas as pd

try:
    df = pd.read_csv('avon-and-somerset-street.csv')
    print(df.head())
except pd.errors.EmptyDataError:
    print("The file exists but it's empty.")
