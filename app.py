import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import inspect
import re

DEF_REGEX = r"def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(.*\):"


def stringify(s):
    return f'"{s}"'


def replace_all(s, d):
    for k, v in d.items():
        s = s.replace(k, v)
    return s


def get_alt_bar_chart(x_axis_labelAngle, x_axis_titleFontStyle):
    source = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X(
                "a",
                axis=alt.Axis(
                    labelAngle=x_axis_labelAngle, titleFontStyle=x_axis_titleFontStyle
                ),
            ),
            y=alt.Y("b"),
        )
    )

    return chart


def main():
    st.title("Altair Playground")
    st.subheader("Bar Chart 📊")

    st.sidebar.title("Chart Configuration")
    st.sidebar.subheader("Axis")

    x_axis_labelAngle = st.sidebar.slider(
        label="X-axis label angle",
        min_value=-360,
        max_value=360,
        value=-90,
        key="x_axis_labelAngle",
    )

    x_axis_titleFontStyle = st.sidebar.selectbox(
        "X-axis title font style", ("normal", "italic",), key="x_axis_titleFontStyle",
    )

    chart = get_alt_bar_chart(x_axis_labelAngle, x_axis_titleFontStyle)
    st.altair_chart(chart, use_container_width=True)

    snippet = inspect.getsource(get_alt_bar_chart)

    properties = dict(
        x_axis_labelAngle=str(x_axis_labelAngle),
        x_axis_titleFontStyle=stringify(x_axis_titleFontStyle),
    )

    snippet = replace_all(snippet, properties)
    snippet = re.sub(DEF_REGEX, r"def bar_chart():", snippet)

    st.subheader("Snippet 📝")
    st.code(snippet, language="python")


if __name__ == "__main__":
    main()
