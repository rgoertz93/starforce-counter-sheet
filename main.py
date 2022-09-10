from textwrap import dedent
import svg

from models import unit_rows
from units.number import draw_number_column
from units.split import draw_split_column, draw_brkf_column, draw_dstr_column, draw_tac_sit_column
from units.starforce import build_starforce_unit
from units.stargate import build_stargate_unit


def draw_unit_column(color, fill, from_text, text_class, from_num, x_offset, y_offset):
    elements = []
    for char in range(ord(from_text), ord(from_text) + 6):
        elements.extend(build_starforce_unit(color, fill, chr(char), text_class, x_offset, y_offset))
        x_offset += 48

    for n in range(from_num, from_num + 4):
        elements.extend(build_stargate_unit(color, fill, n, text_class, x_offset, y_offset))
        x_offset += 48

    return elements


def draw() -> svg.SVG:
    y_offset = 10

    elements = [
        svg.Style(
            text=dedent("""
    .black-text { font-style:normal; font-variant:normal; font-weight:normal; font-stretch:normal; font-size:12px; font-family:Arial; fill:#000000; stroke:#000000; stroke-width:0.0775406 }
    .white-text { font-style:normal; font-variant:normal; font-weight:normal; font-stretch:normal; font-size:12px; font-family:Arial; fill:#FFFFFF; stroke:#FFFFFF; stroke-width:0.0775406 }
    .orange-text { font-style:normal; font-variant:normal; font-weight:normal; font-stretch:normal; font-size:12px; font-family:Arial; fill:#E6B437; stroke:#E6B437; stroke-width:0.0775406 }
    .blue-text { font-style:normal; font-variant:normal; font-weight:normal; font-stretch:normal; font-size:12px; font-family:Arial; fill:#207AF2; stroke:#207AF2; stroke-width:0.0775406 }
    .green-text { font-style:normal; font-variant:normal; font-weight:normal; font-stretch:normal; font-size:12px; font-family:Arial; fill:#255C32; stroke:#255C32; stroke-width:0.0775406 }
    .blue-num-text { font-style:normal; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 24px; font-family:Arial;fill:#207AF2;stroke:#207AF2;stroke-width:0.0241399 }
    .green-num-text { font-style:normal; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 24px; font-family:Arial;fill:#255C32;stroke:#255C32;stroke-width:0.0241399 }
    .black-num-text { font-style:normal; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 24px; font-family:Arial;fill:#000000;stroke:#000000;stroke-width:0.0241399 }
    .split-text { font-style:normal; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 14px; font-family:Arial;fill:#000000;stroke:#000000;stroke-width:0.0241399 }
    .blue-split-text { font-style:normal; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 14px; font-family:Arial;fill:#207AF2;stroke:#207AF2;stroke-width:0.0241399 }
    .split-italic-text { font-style:italic; font-variant:normal; font-weight:bold; font-stretch:normal; font-size: 14px; font-family:Arial;fill:#000000;stroke:#000000;stroke-width:0.0241399 }
            """)
        )
    ]

    for row in unit_rows:
        x_offset = 12

        col_1 = row[0]
        if col_1["type"] == "icons":
            elements.extend(draw_unit_column(col_1["color"], col_1["fill"], col_1["from_text"], col_1["text_class"], col_1["from_num"], x_offset, y_offset))
        elif col_1["type"] == "nums":
            elements.extend(draw_number_column(col_1["color"], col_1["fill"], col_1["text_class"], x_offset, y_offset))
        elif col_1["type"] == "split":
            elements.extend(draw_split_column(col_1["start_num"], col_1["color"], col_1["fill"], x_offset, y_offset))
        elif col_1["type"] == "brkf":
            elements.extend(draw_brkf_column(x_offset, y_offset))
        elif col_1["type"] == "dstr":
            elements.extend(draw_dstr_column(x_offset, y_offset))
        elif col_1["type"] == "tacsit":
            elements.extend(draw_tac_sit_column(x_offset, y_offset))

        x_offset += 528

        col_2 = row[1]
        if col_2["type"] == "icons":
            elements.extend(draw_unit_column(col_2["color"], col_2["fill"], col_2["from_text"], col_2["text_class"], col_2["from_num"], x_offset, y_offset))
        elif col_2["type"] == "nums":
            elements.extend(draw_number_column(col_2["color"], col_2["fill"], col_2["text_class"], x_offset, y_offset))

        y_offset += 48

    return svg.SVG(
        width=1200,
        height=800,
        elements=elements
    )


file = open(r"C:\Users\rgoertz\Desktop\atst.svg", "w")
file.write(draw().as_str())
file.close()
