import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def update_hot_topics(
    top30_df: pd.DataFrame, words: list[str], hot_topics: str
) -> pd.DataFrame:
    """Updates the Top 30 Dataframe table with a Hot Topic input from the user.

    Args:
        top30_df(pd.DataFrame): Top 30 words per newspaper Dataframe
        words(list[str]): List of words in the Top 30 Data Frame to be included in a Hot Topic
        hot_topics(str): Name of the Hot Topic to be created

    Returns:
        pd.DataFrame: Updated Data Frame
    """

    hot_topic_dict = {}

    for word in words:
        hot_topic_dict[word] = hot_topics

    top30_df["hot_topics"] = top30_df["word"].map(hot_topic_dict)
    top30_df["hot_topics"].fillna("", inplace=True)

    return top30_df


def create_top_30_graph(
    top30_df: pd.DataFrame, colours: list[str], time_stamps: list[tuple[int, int]]
) -> go.Figure:
    """Return a Graph for the Top 30 words per Newspaper

    Args:
        top30_df(pd.DataFrame): Dataframe with the top 30 words per newspaper
        colours(list[str]): List of colors to be used in the color achemes
        timepstamps(list[tuple[int, int]]): List with the timestamps for the title

    Returns:
       go.Figure: Figure with Top 30 words per newspaper
    """
    fig = px.bar(
        top30_df,
        x="word",
        y="count",
        facet_row="newspaper",
        facet_col="week",
        color="hot_topics",
        color_discrete_sequence=colours[1:],
        title=f"<b>Top 30 words per newspaper per week</b><br>From W{time_stamps[0][1]} of {time_stamps[0][0]} to W{time_stamps[-1][1]} of {time_stamps[-1][0]}",
        height=3200,
    )

    fig.for_each_annotation(lambda a: a.update(text=f"{a.text.split('=')[-1]}"))
    fig.update_layout(title={"x": 0.01, "y": 0.99})
    fig.update_xaxes(
        matches=None, showticklabels=True, categoryorder="total descending"
    )
    fig.update_yaxes(matches=None, showticklabels=True)

    return fig
