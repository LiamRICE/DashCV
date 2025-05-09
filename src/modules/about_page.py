from dash import html
from PIL import Image
from src.utils.utils import get_data



def about_page():
    children = get_data("./src/data/about_text.csv")

    # load image
    pil_image = Image.open("./src/assets/liam.jpg")

    # set up final component
    component = html.Div(children=[
        html.Div(children=html.Img(title = "Liam RICE", src=pil_image, alt="Photo of Liam on Koh Samet in Thailand", style={"width":500, 'padding':50}, className='flex-shrink-0')),
        html.Div(children=children, style={'padding':50, 'width':'100%'}, className='flex-grow-1 ms-3')
    ], style={'background-color':'azure'}, className='d-flex')

    return component
