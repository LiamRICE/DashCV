import pandas as pd
from dash import html

def get_data(source:str) -> list:
    # reading data
    df = pd.read_csv(source, header=1)
    # set up data in html structure
    children = []
    one = True
    for title, description in df.itertuples(index=False, name=None):
        if one:
            one = False
        else:
            children.append(html.Br())
        children.append(html.Div(children=[html.H3(children=title), html.A(children=description)]))
    
    return children