import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_number_tweets_graphic(
    data: pd.DataFrame, colors: list[str], time_stamps: list[tuple[int, int]]
) -> go.Figure:
    """Returns a picture with a histogram per newspaper

    Args:
        data (pd.DataFrame): Data frame with a "created_at" column
        colors (list[str]): List of colors for the graph
        time_stamps (list[tuple[int, int]]): List with the timestamps

    Returns:
        go.Figure: Histogram figure
    """
    fig = px.histogram(
        data,
        x="created_at",
        color_discrete_sequence=colors,
        facet_row="newspaper",
        title=f"<b>Number of tweets per newspaper</b><br>From W{time_stamps[0][1]} of {time_stamps[0][0]} to W{time_stamps[-1][1]} of {time_stamps[-1][0]}",
        height=1600,
    )

    fig.update_traces(xbins_size="D1")
    fig.update_layout(title={"x": 0.02, "y": 0.97})
    fig.for_each_annotation(lambda a: a.update(text=f"@{a.text.split('=')[-1]}"))

    return fig
