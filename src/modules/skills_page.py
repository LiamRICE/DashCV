from dash import Dash, html, dcc, Input, Output, callback, get_asset_url
from PIL import Image
import plotly.express as px
import pandas as pd
import json
import dash_bootstrap_components as dbc
from src.utils.utils import read_json, read_txt

def skills_page(name:str):
    # read data
    data = read_json("./src/data/"+name+".json")
    skills_text_general = read_txt("./src/data/"+name+"_text.txt")

    # set up formatted data
    tab_names = []
    tab_text = []
    tab_data = []
    for i in data.get("skills"):
        tab_names.append(i.get("type"))
        tab_data.append(i.get("list"))
        tab_text.append(i.get("text"))
    
    # create containers for each tab
    bodies = []
    for i in range(len(tab_data)):
        l = tab_data[i]
        cards = []

        for item in l:
            # format item
            children = []
            if item.get("name"):
                children.append(html.H4(children=item.get("name")))
            if item.get("level"):
                children.append(dcc.Slider(min=0, max=10, step=1, value=item.get("level"), marks=None, tooltip={"placement": "bottom", "always_visible": True}, className="dbc"))
            if item.get("years"):
                children.append(html.P(str(item.get("years"))+" years of experience"))

            body = dbc.Card(
                dbc.CardBody(children=children),
                style={"width": "18rem", "min-width":300},
            )
        
            cards.append(body)
        
        text = ""
        if tab_text[i]:
            text = tab_text[i]
        
        bodies.append(html.Div(children=[
            html.H2(children=tab_names[i]),
            html.P(children=text),
            dbc.CardGroup(children=cards)
        ]))
    
    
    # create tabs contained in the tab object
    tabs = []
    for i in range(len(tab_names)):
        tab = dcc.Tab(
            label=tab_names[i],
            value=tab_names[i],
            children=bodies[i],
            id=tab_names[i]
        )
        tabs.append(tab)

    # tabs = [
    #     dcc.Tab(
    #         label="Tab one",
    #         value="tab-1",
    #         children=html.Div("Tab 1 Content", className="p-4 border"),
    #     ),
    #     dcc.Tab(
    #         label="Tab two",
    #         value="tab-2",
    #         children=html.Div("Tab 2 Content", className="p-4 border"),
    #     )
    # ]

    # setting up main component
    component = html.Div(children=[
        dcc.Markdown(children=skills_text_general),
        dbc.Tabs(
            children=tabs
        )
    ])

    return component
