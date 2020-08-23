import pandas as pd

data_df = pd.read_csv('../modelmaker/HTRU_2.csv')

data_df.columns = ['1','2','3','4','5','6','7','8','9']

#print(data_df)

htmlData = data_df.to_html()
#print(htmlData)

data_df.to_html('table.html')