import pandas
from openpyxl.workbook import Workbook

df_excel = pandas.read_excel('data/regions.xlsx')
df_csv = pandas.read_csv('data/Names.csv', header=None)
df_txt = pandas.read_csv('data/data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Zip code', 'Area Code']
df_csv.to_excel('output/modified.xlsx')
