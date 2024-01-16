import pandas as pd
import plotly.express as px

def read_csv(file_path):
    return pd.read_csv(file_path)

def interactive_vis():
    data = read_csv('AAPL.US.csv')
    fig = px.line(data, x='Date', y='Adjusted_close', title='Apple Inc Stock Price')

    fig.update_traces(mode='lines', hoverinfo='x+y',  line=dict(color='green'))

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Close Price (USD)',
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
        plot_bgcolor='white',   
        paper_bgcolor='white',  
        xaxis_showgrid=False,   
        yaxis_showgrid=False,
        xaxis_linecolor='black', 
        yaxis_linecolor='black', 
        xaxis_ticks='',  
        yaxis_ticks='',
        title_font = dict(size=24)
    )
    fig.show()

interactive_vis()
