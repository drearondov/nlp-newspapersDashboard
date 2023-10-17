from plotly.graph_objects import layout

plotly_gruvbox = layout.Template(
    {
        "data": {
            "bar": [
                {
                    "error_x": {"color": "#282828"},
                    "error_y": {"color": "#282828"},
                    "marker": {
                        "line": {"color": "white", "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "bar",
                }
            ],
            "barpolar": [
                {
                    "marker": {
                        "line": {"color": "white", "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "barpolar",
                }
            ],
            "carpet": [
                {
                    "aaxis": {
                        "endlinecolor": "#282828",
                        "gridcolor": "#d9d9d9",
                        "linecolor": "#d9d9d9",
                        "minorgridcolor": "#d9d9d9",
                        "startlinecolor": "#282828",
                    },
                    "baxis": {
                        "endlinecolor": "#282828",
                        "gridcolor": "#d9d9d9",
                        "linecolor": "#d9d9d9",
                        "minorgridcolor": "#d9d9d9",
                        "startlinecolor": "#282828",
                    },
                    "type": "carpet",
                }
            ],
            "choropleth": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}
            ],
            "contour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "contour",
                }
            ],
            "contourcarpet": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}
            ],
            "heatmap": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "heatmap",
                }
            ],
            "heatmapgl": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "heatmapgl",
                }
            ],
            "histogram": [
                {
                    "marker": {
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2}
                    },
                    "type": "histogram",
                }
            ],
            "histogram2d": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "histogram2d",
                }
            ],
            "histogram2dcontour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "histogram2dcontour",
                }
            ],
            "mesh3d": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}
            ],
            "parcoords": [
                {
                    "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "parcoords",
                }
            ],
            "pie": [{"automargin": True, "type": "pie"}],
            "scatter": [
                {
                    "fillpattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    "type": "scatter",
                }
            ],
            "scatter3d": [
                {
                    "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatter3d",
                }
            ],
            "scattercarpet": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattercarpet",
                }
            ],
            "scattergeo": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergeo",
                }
            ],
            "scattergl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergl",
                }
            ],
            "scattermapbox": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattermapbox",
                }
            ],
            "scatterpolar": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolar",
                }
            ],
            "scatterpolargl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolargl",
                }
            ],
            "scatterternary": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterternary",
                }
            ],
            "surface": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "surface",
                }
            ],
            "table": [
                {
                    "cells": {"fill": {"color": "#f2f2f2"}, "line": {"color": "white"}},
                    "header": {
                        "fill": {"color": "#d9d9d9"},
                        "line": {"color": "white"},
                    },
                    "type": "table",
                }
            ],
        },
        "layout": {
            "annotationdefaults": {
                "arrowcolor": "#282828",
                "arrowhead": 0,
                "arrowwidth": 1,
            },
            "autotypenumbers": "strict",
            "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
            "colorscale": {
                "diverging": [
                    [0, "#8e0152"],
                    [0.1, "#c51b7d"],
                    [0.2, "#de77ae"],
                    [0.3, "#f1b6da"],
                    [0.4, "#fde0ef"],
                    [0.5, "#f7f7f7"],
                    [0.6, "#e6f5d0"],
                    [0.7, "#b8e186"],
                    [0.8, "#7fbc41"],
                    [0.9, "#4d9221"],
                    [1, "#276419"],
                ],
                "sequential": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
                "sequentialminus": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
            },
            "colorway": [
                "#636efa",
                "#EF553B",
                "#00cc96",
                "#ab63fa",
                "#FFA15A",
                "#19d3f3",
                "#FF6692",
                "#B6E880",
                "#FF97FF",
                "#FECB52",
            ],
            "font": {"color": "#282828"},
            "geo": {
                "bgcolor": "white",
                "lakecolor": "white",
                "landcolor": "white",
                "showlakes": True,
                "showland": True,
                "subunitcolor": "#d9d9d9",
            },
            "hoverlabel": {"align": "left"},
            "hovermode": "closest",
            "mapbox": {"style": "light"},
            "paper_bgcolor": "white",
            "plot_bgcolor": "white",
            "polar": {
                "angularaxis": {
                    "gridcolor": "#f2f2f2",
                    "linecolor": "#f2f2f2",
                    "ticks": "",
                },
                "bgcolor": "white",
                "radialaxis": {
                    "gridcolor": "#f2f2f2",
                    "linecolor": "#f2f2f2",
                    "ticks": "",
                },
            },
            "scene": {
                "xaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "#e8e8e8",
                    "gridwidth": 2,
                    "linecolor": "#f2f2f2",
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": "#f2f2f2",
                },
                "yaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "#e8e8e8",
                    "gridwidth": 2,
                    "linecolor": "#f2f2f2",
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": "#f2f2f2",
                },
                "zaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "#e8e8e8",
                    "gridwidth": 2,
                    "linecolor": "#f2f2f2",
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": "#f2f2f2",
                },
            },
            "shapedefaults": {"line": {"color": "#282828"}},
            "ternary": {
                "aaxis": {"gridcolor": "#e8e8e8", "linecolor": "#b5b5b5", "ticks": ""},
                "baxis": {"gridcolor": "#e8e8e8", "linecolor": "#b5b5b5", "ticks": ""},
                "bgcolor": "white",
                "caxis": {"gridcolor": "#e8e8e8", "linecolor": "#b5b5b5", "ticks": ""},
            },
            "title": {"x": 0.05},
            "xaxis": {
                "automargin": True,
                "gridcolor": "#f2f2f2",
                "linecolor": "#f2f2f2",
                "ticks": "",
                "title": {"standoff": 15},
                "zerolinecolor": "#f2f2f2",
                "zerolinewidth": 2,
            },
            "yaxis": {
                "automargin": True,
                "gridcolor": "#f2f2f2",
                "linecolor": "#f2f2f2",
                "ticks": "",
                "title": {"standoff": 15},
                "zerolinecolor": "#f2f2f2",
                "zerolinewidth": 2,
            },
        },
    }
)
