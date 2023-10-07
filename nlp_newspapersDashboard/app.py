import pandas as pd
import plotly.io as pio

from dash import Dash, html, dcc, dash_table, Input, Output
from dash.exceptions import PreventUpdate
from datetime import date, timedelta


pd.set_option("display.max_colwidth", 300)
pd.set_option("display.max_rows", 25)
pd.set_option("display.precision", 2)
pd.set_option("display.float_format", "{:,.2f}".format)

pio.templates.default = "plotly_white"

gruvbox_colors = [
    "#458588",
    "#FABD2F",
    "#B8BB26",
    "#CC241D",
    "#B16286",
    "#8EC07C",
    "#FE8019",
]


app = Dash(__name__, assets_folder="static/dist")
app.title = "Newspaper Headline Analysis"


# UI

app.layout = html.Div(
    className="p-6",
    children=[
        dcc.Store(id="timestamps-store", storage_type="session"),
        html.H1("Headline Newspaper Analysis", className="title is-family-secondary"),
        html.Div(
            className="is-flex mb-6",
            style={"gap": "6em"},
            children=[
                html.Div(
                    children=[
                        html.P("Period", className="title is-6 is-family-secondary"),
                        dcc.DatePickerRange(
                            id="timestamps",
                            style={"border-radius": "15px"},
                            min_date_allowed=date(2022, 7, 1),
                            max_date_allowed=date(2023, 4, 3),
                            initial_visible_month=date(2022, 7, 1),
                            end_date=date(2023, 4, 3),
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.P("Frequency", className="title is-6 is-family-secondary"),
                        dcc.RadioItems(
                            id="frequency",
                            className="is-flex pt-2",
                            inputClassName="mr-2",
                            labelClassName="radio",
                            style={"gap": "2em"},
                            options=["1 week", "2 weeks", "4 weeks"],
                            value="2 weeks",
                        ),
                    ],
                ),
            ],
        ),  # Header, options and tutorial
        dcc.Tabs(
            id="tabs",
            value="number-tweets",
            colors={"background": "#333333"},
            children=[
                dcc.Tab(
                    label="# of tweets",
                    value="number-tweets",
                    children=[
                        dcc.Graph(id="number-tweets-graph"),
                        dash_table.DataTable(id="tweet-stats-table"),
                    ],
                ),
                dcc.Tab(
                    label="Engagement Metrics",
                    value="engagement-metrics",
                    children=[
                        dcc.Graph(id="engagement-per-newspaper-graph"),
                        dash_table.DataTable(id="engagement-per-newspaper-table"),
                    ],
                ),
                dcc.Tab(
                    label="Top 30 words",
                    value="top-30-words",
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="top30-words-graph", style={"flex-grow": 3}
                                ),
                                dash_table.DataTable(id="hot-topics-table"),
                            ],
                            style={"display": "flex"},
                        ),
                        dcc.Graph(id="unique-words-per-newspaper-graph"),
                    ],
                ),
                dcc.Tab(
                    label="Sentiment Analysis",
                    value="sentiment-analysis",
                    children=[
                        dcc.Graph(id="sentiment-analysis-graph"),
                        dcc.Graph(id="emotion-analysis-graph"),
                    ],
                ),
            ],
        ),  # Graphs and results
    ],
)


# Callbacks


@app.callback(
    Output("timestamps-store", "data"),
    Input("timestamps", "start_date"),
    Input("timestamps", "end_date"),
    Input("frequency", "value"),
)
def get_timestamps(
    start_date: str, end_date: str, frequency: str
) -> list[tuple[int, int]]:
    """Converts the selected values from the app into a list of timestamps to load data

    Args:
        start_date (str): Start date selected by the user
        end_date (str): End date selected by the user
        frequency (str): Frequency selected by user

    Returns:
        List: Tuples with the form (year, week)
    """
    time_stamps = []

    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_tuple = (
            start_date_object.isocalendar().year,
            start_date_object.isocalendar().week,
        )
    else:
        raise PreventUpdate
    if end_date is not None:
        end_date_object = date.fromisoformat(start_date)
        end_tuple = (
            end_date_object.isocalendar().year,
            end_date_object.isocalendar().week,
        )
    else:
        raise PreventUpdate

    time_stamps.append(start_tuple)

    next_date_object = start_date_object

    while next_date_object < end_date_object:
        next_date_object = next_date_object + timedelta(weeks=float(frequency[0]))
        time_stamps.append(
            (next_date_object.isocalendar().year, next_date_object.isocalendar().week)
        )

    time_stamps.append(end_tuple)

    return time_stamps


if __name__ == "__main__":
    app.run_server(debug=True)
