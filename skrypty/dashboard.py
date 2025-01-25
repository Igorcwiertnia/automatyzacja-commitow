import dash
from dash import dcc, html
import pandas as pd

# Wczytaj dane
df = pd.read_csv("commit_report.csv")

# Tworzenie aplikacji
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id='author-dropdown',
        options=[{'label': author, 'value': author} for author in df['Author'].unique()],
        placeholder="Wybierz autora"
    ),
    dcc.Graph(id="commit-graph")
])

# Callback do aktualizacji wykresu


@app.callback(
    dash.dependencies.Output("commit-graph", "figure"),
    [dash.dependencies.Input("author-dropdown", "value")]
)
def update_graph(author):
    filtered = df[df['Author'] == author] if author else df
    return {
        'data': [{'x': filtered['Date'], 'y': filtered['Message'], 'type': 'bar'}]
    }


if __name__ == "__main__":
    app.run_server(debug=True)
