from enum import Enum
from dash import Dash, html, dcc, Input, Output, ctx, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from src.modules.top_bar import header
from src.modules.about_page import about_page
from src.modules.skills_page import skills_page
from src.modules.home_page import home_page
from src.modules.experience_page import experience_page

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

class State(Enum):
    HOME = 0
    ABOUT = 1
    SKILLS = 2
    EXPERIENCE = 3
    EDUCATION = 4

def select_children(state):
    if state == State.HOME:
        return home_page(state.name.lower())
    if state == State.ABOUT:
        return about_page(state.name.lower())
    elif state == State.SKILLS:
        return skills_page(state.name.lower())
    elif state == State.EDUCATION:
        return html.A(children="This is a page about Liam's education.")
    elif state == State.EXPERIENCE:
        return experience_page(state.name.lower())

app.layout = html.Div(children=[
    header(["about", "skills", "experience", "education"]),
    html.Div([
        # represents the browser address bar and doesn't render anything
        dcc.Location(id='url', refresh=False),
        # content will be rendered in this element
        html.Div(id='page-content')
    ], style={"padding":20})
])



# # Defining Callbacks
# @callback(
#     Output(component_id="clicked", component_property="children"),
#     Input(component_id="about", component_property="n_clicks"),
#     Input(component_id="skills", component_property="n_clicks"),
#     Input(component_id="experience", component_property="n_clicks"),
#     Input(component_id="education", component_property="n_clicks")
# )
# def on_click(a, b, c, d):
#     msg = "Nothing clicked..."
#     state = State.ABOUT
#     if "about" == ctx.triggered_id:
#         msg = "About was most recently clicked"
#         state = State.ABOUT
#     elif "skills" == ctx.triggered_id:
#         msg = "Skills was most recently clicked"
#         state = State.SKILLS
#     elif "experience" == ctx.triggered_id:
#         msg = "Experience was most recently clicked"
#         state = State.EXPERIENCE
#     elif "education" == ctx.triggered_id:
#         msg = "Education was most recently clicked"
#         state = State.EDUCATION
#     switch_state(state)
#     return msg

# Update the index
@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return select_children(State.HOME)
    if pathname == '/about':
        return select_children(State.ABOUT)
    elif pathname == '/skills':
        return select_children(State.SKILLS)
    elif pathname == '/experience':
        return select_children(State.EXPERIENCE)
    elif pathname == '/education':
        return select_children(State.EDUCATION)
    else:
        return select_children(State.ABOUT)
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run(debug=True)