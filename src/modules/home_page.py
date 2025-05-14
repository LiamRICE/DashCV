from dash import Dash, html, dcc, Input, Output, callback, get_asset_url
from PIL import Image
import plotly.express as px
import pandas as pd
import json
import dash_bootstrap_components as dbc
from src.utils.utils import read_json, read_txt


def home_page(name:str):

    text = read_txt("./src/data/home_page.txt")
    
    components = html.Div(children=[
        dcc.Markdown(children = text)
    ])

    return components