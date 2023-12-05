import plotly.io as pio

from dash import Dash, Input, Output, dcc, html, get_asset_url
from datetime import date
from datetime import timedelta
from loguru import logger

from api.io import compile_data_frame
from api.number_tweets import create_number_tweets_graphic
from api.engagement_metrics import (
    create_stats_summary,
    create_engagement_metrics_graphic,
    create_stats_ratios,
    create_stats_table,
)
from api.top_30_words import create_top_30_graph


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
                                    src=get_asset_url("nlp-newspaperDashboard.svg"),
                                    width=36,
                                ),
                                html.H1(
                                    "Headline Newspaper Analysis",
                                    className="title is-2 is-family-secondary",
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
                    id="api",
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
    """Converts the selected values from the app into a list of timestamps to load data.

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
    Input("api", "value"),
)
def api_handler(timestamps: list[tuple[int, int]], tab_selection: str) -> html.Div:
    """Gets the current selection and returns a div with the graphics necesaries.

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
            stats_data = compile_data_frame(timestamps, "data_clean")
            stats_summary = create_stats_summary(stats_data)
            stats_ratios = create_stats_ratios(stats_data)

            return html.Div(
                children=[
                    dcc.Graph(
                        id="engagement-metrics-graph",
                        figure=create_engagement_metrics_graphic(
                            stats_summary, gruvbox_colors, timestamps
                        ),
                    ),
                    html.H2(
                        "Stats & Ratios",
                        className="title is-4 mt-5 is-family-secondary",
                    ),
                    create_stats_table(stats_ratios),
                ]
            )
        case "top-30-words":
            corpus_data = compile_data_frame(timestamps, "corpus")
            top30 = compile_data_frame(timestamps, "top30")

            return html.Div(
                className="is-flex",
                children=[
                    dcc.Graph(
                        className="is-flex-grow-3",
                        id="top-30-words-graph",
                        figure=create_top_30_graph(top30, gruvbox_colors, timestamps),
                    ),
                    html.Div(
                        children=[
                            html.H3(
                                children=["Add new topic"],
                                className="title is-5 is-family-secondary",
                            ),
                            html.Div(
                                children=[
                                    dcc.Input(
                                        id="top30-new-topic",
                                        type="text",
                                        placeholder="New topic",
                                        debounce=True,
                                    ),
                                    dcc.Input(
                                        id="top30-input-words",
                                        type="text",
                                        placeholder="Words to be added to hot topic (separate with commas)",
                                        debounce=True,
                                    ),
                                ]
                            ),
                            html.H3(
                                children=["Current topics"],
                                className="title is-5 is-family-secondary",
                            ),
                            html.Div(id="current-topics", className="tags"),
                        ],
                    ),
                ],
            )
        case "sentiment-analysis":
            pass  # TODO: Sentiment Analysis api


@app.callback(
    Output("current-topics", "children"),
    Input("current-topics", "children"),
    Input("top30-new-topic", "text"),
    Input("top30-new-topic-words", "text"),
)
def update_tracked_topics(
    current_topics: list[html.Span], top30_new_topic: str, top30_new_topic_words: str
) -> list[html.Span]:
    """Gets the current list of tracked topics and stores it.

    Args:
        current_topics (list[html.Span]): Current list of topics tracked
        top30_new_topic (str): New topics to track
        top30_new_topic_words (str): Words belonging to the topic

    Returns:
        list[html.Span]: An updated list of the topics
    """
    current_topics.append(html.Span(top30_new_topic, className="tag"))
    pass


if __name__ == "__main__":
    app.run_server(debug=True)
