import io
from dash import Dash, html, dcc, Input, Output, State, callback, get_asset_url, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from src.utils.utils import read_csv, read_txt
from dash.exceptions import PreventUpdate


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# def filters(dataframe:pd.DataFrame) -> html.Div:
#     states = dataframe.State.unique().tolist()
#     division = dcc.Dropdown(
#         id="filter_dropdown",
#         options=[{"label": st, "value": st} for st in states],
#         placeholder="-Select a State-",
#         multi=True,
#         value=dataframe.State.values,
#     ),
#     return division


def experience_page(name:str):
    # read the text to show on the component
    text = read_txt("./src/data/experience_page.md")
    # get data for tables
    data = read_csv("./src/data/experience_data.csv")
    place_holder = None
    df_filter = pd.DataFrame(
        {
            "Skill":[place_holder],
            "Level":[place_holder],
            "Year":[place_holder],
            "Position":[place_holder]
        }
    )

    # set up the component
    components = html.Div(children=[
        dcc.Markdown(children=text),
        # filters(data),
        dcc.Download(id="download"),
        html.Button("Download",
                    id="save-button"),
        html.Div("Press button to save data at your desktop",
                    id="output-1"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            export_format="xlsx",
            export_columns="visible",
            style_table={"overflowX": "scroll"},
        )
    ])

    return components


@callback(
Output("download", "data"),
Input("save-button", "n_clicks"),
State("table", "data"))
def download_as_csv(n_clicks, table_data):
    df = pd.DataFrame.from_dict(table_data)
    if not n_clicks:
      raise PreventUpdate
    download_buffer = io.StringIO()
    # df.to_excel(download_buffer, index=False)
    df.to_csv(download_buffer, index=False)
    download_buffer.seek(0)
    return dict(content=download_buffer.getvalue(), filename="data.csv")

