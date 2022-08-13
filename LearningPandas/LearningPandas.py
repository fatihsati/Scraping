from asyncore import write
import csv
from operator import index
from fastapi import Header
import pandas as pd

# dictionary to dataframe

# df_dict = {'brand': ['bmw', 'audi', 'ferrari'],
#            'color': ['blue', 'black', 'red'],
#            'has f1-team': ['no', 'no', 'yes']}

# df_d = pd.DataFrame(df_dict)
# print(df_d)
# ------------------------------ selecting column-row-condition from dataframe ------------------------------------------
# selecting a column using column name

    # column = df_d['has f1-team']
    # print(list(df_d['has f1-team']))
# selecting unique elements in a column
    #print(column.drop_duplicates)

# selecting first column using index                # df.iloc lets us select rows and columns by their index's. 
# print('-------------------')                    # they need to be separated by (,)
# brand_column = df_d.iloc[:, 0]
# print(brand_column)
# print('-------------------')
# color_column = df_d.iloc[:, 1]
# print(color_column)
# print('-------------------')
# print('-------------------')
# two_columns_two_rows = df_d.iloc[:2, 1:]      #first 2 rwo, last 2 columns      color- has f1-team for bmw and audi
# print(two_columns_two_rows)
# print('-------------------')

# df_d.loc[0] # returns first row. 
#  df_d['has f1-team'] == 'no' returns each row as bool. True or False

# brand_with_loc = df_d.loc[df_d['has f1-team'] == 'no']      # returns rows which has value of true. (has f1-team = no)
# print(brand_with_loc)
# -------------------------------------------- saving an excell file --------------------------------------------

# df_d.to_csv('LearningPandas.csv', index=False, encoding='utf-8')      # standart saving format

# adding new values by creating a dataframe
    #new car data                   # To create dataframe, row values must be in list.
# car = {'brand': ['renoult', 'mclaren', 'mercedes'],
#         'color': ['yellow', 'orange', 'silver'],
#         'has f1-team': ['yes', 'yes', 'yes']}

# df_car = pd.DataFrame(car)
# print(df_car)
# df_car.to_csv('LearningPandas.csv', mode='a', index=False, header=False, encoding='utf-8')


# adding new row using writer_object
# from csv import writer
# csv_file = open('LearningPandas.csv', 'a', newline='')
# writer_obj = writer(csv_file)
# new_row = ['porsche', 'black', 'no']
# writer_obj.writerow(new_row)
# csv_file.close()


# -------------------------------------------- reading an excell file --------------------------------------------

# df = pd.read_csv('LearningPandas.csv', encoding='utf-8')       # if header is None first row of csv gonna
# print(df)                                                                   # be first row of df

# header_df = df.iloc[1:, :]                              # what we have done here is:
# header_df.columns = ['brarnd', 'color', 'has f1-team']  # removed first row because it was incorrect, then  we added column names
# print(header_df)                                        # using .columns property.


    # change a rows value
# df.loc[df['brand'] == 'renoult'] = ['renault', 'yellow', 'yes']
# df.to_csv('LearningPandas.csv', encoding='utf-8', index=False)

# file = open('LearningPandas/WriteRow.csv', mode='a', newline='')
# writer = csv.writer(file)
# writer.writerow(['Brand', 'Color', 'Year'])       # column names
# writer.writerow(['Audi', 'Black', '2021'])      # first element

# writer.writerow(['Bmw', 'Blue', '2020'])
# writer.writerow(['Ferrari', 'Red', '2022'])
# file.close()

# ------------------ read, change and save --------------------------
df = pd.read_csv('LearningPandas/WriteRow.csv')     # read old csv
print(df)
print('-------------')

df.loc[df['Brand'] == 'Bmw', 'Year'] = '2018'               # change (Year) column of the rows where Brand equal to BMW

print(df)

df.to_csv('LearningPandas/WriteRow.csv', index=False, encoding='utf-8')   # save df into same csv, old version is deleted.
#-------------------------------------------------------------------










