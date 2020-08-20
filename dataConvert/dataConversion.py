import pandas as pd

data_df = pd.read_csv('../modelmaker/data.csv')

#print(data_df)

htmlData = data_df.to_html()
#print(htmlData)

data_df.to_html('table.html')