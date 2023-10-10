import logging
import pandas as pd
import plotly.io as pio
import sys

from dash import Dash, Input, Output, dcc, html, get_asset_url
from datetime import date
from datetime import timedelta

from controllers.io import compile_data_frame
from controllers.number_tweets import create_number_tweets_graphic

pd.set_option("display.max_colwidth", 300)
pd.set_option("display.max_rows", 25)
pd.set_option("display.precision", 2)
pd.set_option("display.float_format", "{:,.2f}".format)

pio.templates.default = "none"

gruvbox_colors = [
    "#458588",
    "#FABD2F",
    "#B8BB26",
    "#CC241D",
    "#B16286",
    "#8EC07C",
    "#FE8019",
]

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(stream=sys.stdout, format=log_format, level=logging.INFO)

logger = logging.getLogger()


app = Dash(__name__, assets_folder="static/dist")
app.title = "Newspaper Headline Analysis"
app._favicon = "favicon.ico"


# UI
app.layout = html.Div(
    className="p-6",
    children=[
        dcc.Store(id="timestamps-store", storage_type="session"),
        html.Div(
            className="is-flex mb-5 is-justify-content-space-between",
            style={"gap": "5em"},
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="is-flex my-3",
                            style={"gap": "1em"},
                            children=[
                                html.Img(
                                    src=get_asset_url("nlp-newspaperDashboard.svg")
                                ),
                                html.H1(
                                    "Headline Newspaper Analysis",
                                    className="title is-family-secondary",
                                ),
                            ],
                        ),
                        html.Div(
                            className="is-flex",
                            style={"gap": "2em"},
                            children=[
                                html.Div(
                                    children=[
                                        html.P(
                                            "Period",
                                            className="title is-6 is-family-secondary mb-1",
                                        ),
                                        dcc.DatePickerRange(
                                            id="timestamps",
                                            style={"border-radius": "15px"},
                                            min_date_allowed=date(2022, 7, 1),
                                            max_date_allowed=date(2023, 4, 3),
                                            initial_visible_month=date(2022, 7, 1),
                                            start_date=date(2023, 1, 1),
                                            end_date=date(2023, 4, 3),
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.P(
                                            "Frequency",
                                            className="title is-6 is-family-secondary mb-1",
                                        ),
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
                        ),
                    ]
                ),
                dcc.Tabs(
                    id="tabs",
                    value="number-tweets",
                    parent_className="is-flex-grow-2",
                    style={"padding": "0.5em"},
                    colors={"background": "#e7e7e7"},
                    children=[
                        dcc.Tab(label="# of tweets", value="number-tweets"),
                        dcc.Tab(label="Engagement Metrics", value="engagement-metrics"),
                        dcc.Tab(label="Top 30 words", value="top-30-words"),
                        dcc.Tab(label="Sentiment Analysis", value="sentiment-analysis"),
                    ],
                ),
            ],
        ),  # Header, options and tutorial
        html.Div(id="tab-content"),  # Graphs and results
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

    logger.info(f"Start Date: {start_date}")
    logger.info(f"End Date: {end_date}")

    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_tuple = (
            start_date_object.isocalendar().year,
            start_date_object.isocalendar().week,
        )
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_tuple = (
            end_date_object.isocalendar().year,
            end_date_object.isocalendar().week,
        )

    logger.info(f"Start Tuple: {start_tuple}")
    logger.info(f"End Date: {end_tuple}")

    time_stamps.append(start_tuple)

    next_date_object = start_date_object

    while next_date_object < end_date_object:
        next_date_object = next_date_object + timedelta(weeks=float(frequency[0]))
        time_stamps.append(
            (next_date_object.isocalendar().year, next_date_object.isocalendar().week)
        )

    time_stamps.append(end_tuple)

    logger.info(f"{time_stamps}")

    return time_stamps


@app.callback(
    Output("tab-content", "children"),
    Input("timestamps-store", "data"),
    Input("tabs", "value"),
)
def tabs_handler(timestamps: list[tuple[int, int]], tab_selection: str) -> html.Div:
    """Gets the current selection and returns a div with the graphics necesaries

    Args:
        timestamps (list[tuple[int, int]]): List of timestamps selected
        tab_selection (str): String corresponfing to the selected tab

    Returns:
        html.Div: Content corresponding to the tab selected
    """
    match tab_selection:
        case "number-tweets":
            corpus_data = compile_data_frame(timestamps, "corpus")

            return html.Div(
                children=[
                    dcc.Graph(
                        id="number-tweets-graph",
                        figure=create_number_tweets_graphic(
                            corpus_data, gruvbox_colors, timestamps
                        ),
                    )
                ]
            )
        case "engagement-metrics":
            pass
        case "top-30-words":
            pass
        case "sentiment-analysis":
            pass


if __name__ == "__main__":
    app.run_server(debug=True)
