import pandas as pd

data_df = pd.read_csv('../modelmaker/HTRU_2.csv')

data_df.columns = ['1','2','3','4','5','6','7','8','9']
data_df['10'] = data_df.index

select_df = data_df['10']

data = []
d = {}
for o in select_df:
    d = dict()
    d['id'] = o
    data.append(d)

print(data)