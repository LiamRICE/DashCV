from dash import html
from PIL import Image
import dash_bootstrap_components as dbc
from src.utils.utils import get_data



def about_page(name:str):
    children = get_data("./src/data/"+name+".csv")

    # load image
    pil_image = Image.open("./src/assets/liam.jpg")

    # set up final component
    component = dbc.CardGroup(children=[
        html.Div(children=html.Img(title = "Liam RICE", src=pil_image, alt="Photo of Liam on Koh Samet in Thailand", style={"width":500, 'padding':50}, className='flex-shrink-0')),
        html.Div(children=children, style={'padding':50, 'width':400, 'min-width':400}, className='flex-grow-1 ms-3')
    ], style={'background-color':'azure'})

    return component
