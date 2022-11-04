import pandas as pd

country = 'IND'
continent = 'Europe'
names = ['Charging Profiles', 'Mobility Profiles', 'Usage']

folder = 'results/' + continent + '/' + country + '/results/'
for name in names:
    df = pd.read_csv(folder + name + '.csv', header=0, index_col=0, parse_dates=[0], names=['timestamp', 'profile'])
    df = df.resample("H").mean()
    df.to_csv('results/' + continent + '/' + country + '/results/' + name + ' Hourly.csv')
print('DONE!')
