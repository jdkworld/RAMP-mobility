import pandas as pd
import plotly.express as px

country = 'IND'
continent = 'Europe'


profile = 'Mobility Profiles'
profile2 = 'Charging Profiles'
name = 'Charging Profiles Hourly'
names = ['Charging Profiles', 'Mobility Profiles', 'Usage']
yaxis_titles = ['power[kW]', 'power[W]', 'average number of cars driving']
units = ['kW', 'W', '-']
resolutions = ['hour','minute']

folder = 'results/' + continent + '/' + country + '/results/'
for i, name in enumerate(names):
    for resolution in resolutions:
        if resolution == 'hour':
            res = ' Hourly'
        else:
            res = ''
        try:
            df = pd.read_csv(folder + name + res + '.csv', header=0, index_col=0, parse_dates=[0], names=['timestamp', 'profile'])
            fig = px.line(df, x=df.index, y='profile', render_mode='webgl')
            fig.update_layout(title=name + res, xaxis_title='timestamp', yaxis_title=yaxis_titles[i])
            fig.write_html(folder + name + res + ".html", include_plotlyjs='cdn')
        except:
            print('Profile ' + name + ' ' + res + ' does not exist.')
print('DONE!')

"""
df = pd.read_csv('results/Europe/IND/results/' + profile + '.csv', header=0, names=['datetime', ' profile'])
print(df)
names = df.columns.values.tolist()
fig = px.line(df, x='datetime', y=names, render_mode='webgl')
fig.update_layout(showlegend=True)
fig.write_html(profile + ".html", include_plotlyjs='cdn')

df = pd.read_csv('results/Europe/IND/results/' + profile2 + '.csv', header=0, names=['datetime', ' profile'])
print(df)
names = df.columns.values.tolist()
fig = px.line(df, x='datetime', y=names, render_mode='webgl')
fig.update_layout(showlegend=True)
fig.write_html(profile2 + ".html", include_plotlyjs='cdn')
"""