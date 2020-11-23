import pandas
from openpyxl.workbook import Workbook

dataframe = pandas.read_csv('data/Names.csv', header=None)
dataframe.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Foo']

wanted_values = ['First', 'Last', 'State']
dataframe[wanted_values].to_excel('output/test.xlsx')
