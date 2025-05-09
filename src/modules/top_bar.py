from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

def header(options:list[str]):
    children:list = []
    # creating list of buttons
    for option in options:
        children.append(
            dbc.Col(
                dbc.Button(children=option.capitalize(), id=option, color="primary", className="ms-2", n_clicks=0, href=f'/{option}'),
                width="auto",
            )
        )

    # defining the top bar
    top_bar = dbc.Navbar(
        dbc.Container([
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Liam RICE", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            dbc.Collapse(
                children=children,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]),
        color="dark",
        dark=True,
    )

    return top_bar
