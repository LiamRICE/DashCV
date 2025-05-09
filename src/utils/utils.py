import pandas as pd
from dash import html
import json



def get_data(source:str) -> list:
    # reading data
    df = pd.read_csv(source, header=0)
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



def read_json(source:str) -> pd.DataFrame:
    data = {}
    decoder = json.JSONDecoder()

    with open("./src/data/skills.json", "r") as f:
        data = f.read()
        f.close()
        data = decoder.decode(data)

    return data