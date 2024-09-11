from dash import Dash, dcc, html, Input, Output, State, callback

@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)

def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

def get_layout():
    my_div = html.Div([
                        html.Div(dcc.Input(id='input-on-submit', type='text')),
                        html.Button('Submit', id='submit-val', n_clicks=0),
                        html.Div(id='container-button-basic',
                        children='Enter a value and press submit')
                      ])
    return my_div

