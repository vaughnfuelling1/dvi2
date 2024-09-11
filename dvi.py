from dash import Dash, html, dcc
import dash

import panel1
import panel2

app = Dash(__name__, use_pages=True, pages_folder="", assets_folder="/", assets_url_path='')
#app.config['suppress_callback_exceptions'] = True

dash.register_page(module="P1_module", title="P1", path='/'    , layout=panel1.get_layout())
dash.register_page(module="P2_module", title="P2", path="/pan2", layout=panel2.get_layout())

svg_img  = html.Img( src='hamburger.svg', style={'height': '2em', 'width': 'auto'}),
svg_img2 = html.Img( src='hamburger-off.svg', style={'height': '2em', 'width': 'auto'}),

app.layout = html.Div([
    html.H1(["DVI2"]),
    html.Div(svg_img),
    html.Div(svg_img2),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container,
])

if __name__ == '__main__':
    app.run(debug=True)
