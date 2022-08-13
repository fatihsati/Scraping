import pandas as pd


df = pd.read_csv('LearningPandas/LearningPandas.csv', encoding='utf-8')
print(df)
# change specific column in a specific row
# temp = df.loc[df['brand'] == 'mclaren']
# temp_index = temp.index[0]

# df.iloc[temp_index,1] = 'ORANGE'
# print(df)
# -----------------------------
# reading row by by
# returns first 2 columns of each row as a list items
# row_count = df.shape[0]

# for each in range(row_count):
#     row = df.iloc[each,:]
#     print(row.iloc[:2].values)
    
# print('printing is done')

# read row by row if see a ORANGE mclaren change it to PINK mclaren

# for row in range(row_count):
#     row_values = df.iloc[row, :]
    
#     if row_values['brand'] == 'mclaren' and row_values['color'] == 'ORANGE':
#         df.iloc[row,1] = 'PINK'
    
# print(df)


df = df[['color', 'has f1-team', 'brand']]
print(df)





