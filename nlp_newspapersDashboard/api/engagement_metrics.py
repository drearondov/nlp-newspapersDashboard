import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dash import html


def create_stats_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Transforms stats data into long format.

    Args:
        data (pd.DataFrame): Statistics DataFrame clean and compiled

    Returns:
        pd.DataFrame: Stats data in long form
    """
    data["year"] = data["created_at"].dt.isocalendar().year
    data["week"] = data["created_at"].dt.isocalendar().week

    stats_summary = (
        data[
            [
                "newspaper",
                "retweet_count",
                "reply_count",
                "like_count",
                "quote_count",
                "year",
                "week",
            ]
        ]
        .groupby(by=["newspaper", "year", "week"])
        .agg(func=["count", "min", "mean", "std", "max", "sum"])
    )

    stats_summary[("retweet_count", "ratio")] = (
        stats_summary[("retweet_count", "sum")]
        / stats_summary[("retweet_count", "count")]
    )
    stats_summary[("reply_count", "ratio")] = (
        stats_summary[("reply_count", "sum")] / stats_summary[("reply_count", "count")]
    )
    stats_summary[("like_count", "ratio")] = (
        stats_summary[("like_count", "sum")] / stats_summary[("like_count", "count")]
    )
    stats_summary[("quote_count", "ratio")] = (
        stats_summary[("quote_count", "sum")] / stats_summary[("quote_count", "count")]
    )

    stats_summary = stats_summary.stack()
    stats_summary = stats_summary.melt(var_name="metric", ignore_index=False)
    stats_summary = stats_summary.reset_index()
    stats_summary.rename({"level_3": "stat"}, axis=1, inplace=True)

    stats_summary["year_week"] = (
        stats_summary["year"].astype("str") + "w" + stats_summary["week"].astype("str")
    )

    stats_summary["metric"] = stats_summary["metric"].str.removesuffix("_count")

    return stats_summary


def create_engagement_metrics_graphic(
    data: pd.DataFrame, colors: list[str], time_stamps: list[tuple[int, int]]
) -> go.Figure:
    """Returns a figure with the engagement metrics per newspaper.

    Args:
        data (pd.DataFrame): Data frame with a "created_at" column
        colors (list[str]): List of colors for the graph
        time_stamps (list[tuple[int, int]]): List with the timestamps

    Returns:
        go.Figure: Line graphs of stats per newspaper
    """
    fig = px.line(
        data,
        x="year_week",
        y="value",
        color="newspaper",
        facet_row="stat",
        facet_col="metric",
        facet_row_spacing=0.05,
        facet_col_spacing=0.05,
        color_discrete_sequence=colors,
        title=f"<b>Raw engagement stats per newspaper</b><br>From W{time_stamps[0][1]} of {time_stamps[0][0]} to W{time_stamps[-1][1]} of {time_stamps[-1][0]}",  # noqa: B950
        height=2100,
    )

    fig.for_each_annotation(lambda a: a.update(text=f"{a.text.split('=')[-1]}"))
    fig.update_layout(title={"x": 0.01, "y": 0.99})
    fig.update_xaxes(showticklabels=True, tickangle=-45)
    fig.update_yaxes(matches=None, showticklabels=True)

    return fig


def create_stats_ratios(data: pd.DataFrame) -> pd.DataFrame:
    """Create table with counts and ratios for newspapers.

    Args:
        data (pd.DataFrame): Raw stats dataframes

    Returns:
        dict: Table with counts and ratios for newspapers
    """
    data_stats = pd.DataFrame()

    data_stats["tweet_count"] = data["newspaper"].value_counts()

    data_stats = data_stats.merge(
        data.loc[data["referenced_tweets"].notna(), "newspaper"].value_counts(),
        how="left",
        left_index=True,
        right_index=True,
    )
    data_stats.rename(columns={"count": "referenced_tweet_count"}, inplace=True)

    data_stats = data_stats.merge(
        data.loc[data["possibly_sensitive"], "newspaper"].value_counts(),
        how="left",
        left_index=True,
        right_index=True,
    )
    data_stats.rename(columns={"count": "possibly_sensitive_count"}, inplace=True)

    data_stats = data_stats.merge(
        data.groupby("newspaper")
        .sum(numeric_only=True)
        .drop("possibly_sensitive", axis=1),
        how="left",
        left_index=True,
        right_index=True,
    )

    data_stats["reference_to_tweets_ratio"] = (
        data_stats["referenced_tweet_count"] / data_stats["tweet_count"]
    )
    data_stats["sensitive_to_tweets_ratio"] = (
        data_stats["possibly_sensitive_count"] / data_stats["tweet_count"]
    )
    data_stats["retweet_to_tweets_ratio"] = (
        data_stats["retweet_count"] / data_stats["tweet_count"]
    )
    data_stats["reply_to_tweets_ratio"] = (
        data_stats["reply_count"] / data_stats["tweet_count"]
    )
    data_stats["like_to_tweets_ratio"] = (
        data_stats["like_count"] / data_stats["tweet_count"]
    )
    data_stats["quote_to_tweets_ratio"] = (
        data_stats["quote_count"] / data_stats["tweet_count"]
    )

    return data_stats.T.reset_index(names=["Stat"])


def create_stats_table(data_frame: pd.DataFrame) -> html.Table:
    """Constructor for a Dash Table from a Data Frame.

    Args:
        data_frame (pd.DataFrame):  Source data for Table

    Returns:
        html.Table: Dash Table element
    """
    table_rows: list[html.Tr] = []

    for _, row in data_frame.iterrows():
        single_row: list[html.Td] = []

        for item in row.tolist():
            if isinstance(item, str):
                item = item.replace("_", " ")
                item = item.title()
            elif isinstance(item, float):
                item = "{:.2f}".format(item)

            single_row.append(html.Td(item))

        table_rows.append(html.Tr(children=single_row))

    dash_table = html.Table(
        className="table is-fullwidth is-striped",
        children=[
            html.Thead(
                children=html.Tr(
                    children=[
                        html.Th(column_name) for column_name in data_frame.columns
                    ]
                )
            ),
            html.Tbody(children=table_rows),
        ],
    )
    return dash_table
