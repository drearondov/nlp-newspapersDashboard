import pandas as pd

from pathlib import Path


def compile_data_frame(
    timestamps: list[tuple[int, int]], data_frame_type: str
) -> pd.DataFrame:
    """Reads eachfile from the timestamps, compile's it and returns a single DataFrame with all the data.

    Args:
        timestamps (list[tuple[int, int]]): List of timestamps of the form (year, week)
        data_frame_type (str): Type of DataFrame to Load

    Returns:
        pd.DataFrame: A cataframe with all data compiled
    """
    graph_data = []

    for timestamp in timestamps:
        data_path = Path(f"static/data/{data_frame_type}-{tuple(timestamp)}.feather")

        if not data_path.exists():
            continue

        graph_data.append(pd.read_feather(data_path))

    graph_data_frame = pd.concat(graph_data)

    return graph_data_frame
