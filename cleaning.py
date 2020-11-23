import pandas
import numpy
from openpyxl.workbook import Workbook

dataframe = pandas.read_csv('data/Names.csv', header=None)
dataframe.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

dataframe.drop(columns='Address', inplace=True)

dataframe = dataframe.set_index('Area Code')

# print(dataframe)
# print(dataframe.loc[8074])
# print(dataframe.iloc[1])

dataframe.First = dataframe.First.str.split(expand=True)
dataframe = dataframe.replace(numpy.nan, 'N/A', regex=True)

print(dataframe)
