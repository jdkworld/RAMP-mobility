import pandas as pd
import plotly.express as px
from pathlib import Path


def to_hourly(df, name, output_folder):
    hourly_df = df.resample("H").mean()
    df.to_csv(f'{output_folder}{name} Hourly.csv')
    return hourly_df

def to_plotly_html(df, name, output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    if 'Mobility' in name:
        yax = 'power[W]'
    elif 'Charging' in name:
        yax = 'power[kW]'
    else:
        yax = 'average number of cars driving'

    fig = px.line(df, x=df.index, y=df.columns, render_mode='webgl')
    fig.update_layout(title=name, yaxis_title=yax, showlegend=False)
    fig.write_html(f'{output_folder}{name}.html', include_plotlyjs='cdn')

def csv_to_json():
    pass

