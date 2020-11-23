import pandas

dataframe = pandas.read_csv('data/Names.csv', header=None, skip_blank_lines=True)
dataframe.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

# print(dataframe.loc[(dataframe['City'] == 'Riverside') & (dataframe['First'] == 'John')])

dataframe['Tax %'] = dataframe['Income'].apply(lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25)
dataframe['foobar'] = 'heiiiilooo'
dataframe['Taxes Owed'] = dataframe['Income'] * dataframe['Tax %']

to_drop = ['Area Code', 'First', 'Address']
dataframe.drop(columns=to_drop, inplace=True)

dataframe['Test Col'] = False
dataframe.loc[dataframe['Income'] < 60000, 'Test Col'] = True

print(dataframe)
