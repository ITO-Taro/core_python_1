"""
Exercise: download USA_Housing.csv and perform the following tasks
1. Create a new column 'zip_code' use the zipcodes found in values under the column address
2. Calculate the sum of all 'avg. area income' for every state
"""

import pandas as pd
from IPython.display import display

PATH = "/Users/taro/Desktop/Code_Immersives/PY131/core_python/us_housing"
with open(PATH+'/us_housing.csv', 'r', encoding="utf8") as file:
    line = file.readline()
    line = line.replace(".", "").replace(" ", "_").lower()
    cols = line.strip("\n").split(",")

df = pd.read_csv(
    PATH+'/us_housing.csv',
    index_col=False,
    names=cols
    )
df = df.loc[1:, :]

for col in df.columns:
    if col == 'address':
        df[col] = df[col].apply(lambda x: x.replace("\n", " "))
    elif col == "area_population":
        df[col] = df[col].apply(lambda x: round(float(x)))
    else:
        df[col] = df[col].apply(lambda x: round(float(x), 2))

for num in df.index:
    addresses = df.loc[num, 'address'].split(" ")
    df.loc[num, 'state'] = addresses[-2]
    df.loc[num, 'zip_code'] = addresses[-1]

mean_income_per_state = {}
for state in df.state.unique():
    incomes = df[df.state == state].avg_area_income
    mean_income_per_state[state] = incomes.mean().round(2)

# sorted(mean_income_per_state.items(), key=lambda kv: kv[1], reverse=True)
test = max(mean_income_per_state, key=mean_income_per_state.get)
display(test)
