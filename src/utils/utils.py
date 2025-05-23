import pandas as pd
from dash import html
import json


def read_csv(source:str) -> pd.DataFrame:
    df = pd.read_csv(source, header=0)
    return df



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

    with open(source, "r") as f:
        data = f.read()
        f.close()
        data = decoder.decode(data)

    return data



def read_txt(source:str) -> str:
    data = ""

    try:
        with open(source, encoding="UTF-8") as f:
            data = f.read()
    except:
        f.close()
        with open(source, encoding="UTF-16") as f:
            data = f.read()
            f.close()
    
    return data