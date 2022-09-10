import svg
from units.base import build_unit

starforce_unit = [
    {
        "type": "rect",
        "x": 19,
        "y": 20,
        "width": 20.241743,
        "height": 3.9836814,
        "stroke_width": 0.0808346,
        "rotate": 0
    },
    {
        "type": "rect",
        "x": 26.5,
        "y": 21,
        "width": 4.7963624,
        "height": 20.241524,
        "stroke_width": 0.0810573,
        "rotate": 0
    },
    {
        "type": "circle",
        "x": 29,
        "y": 15,
        "stroke_width": 0.0812941,
        "radius": 7.3567719,
    },
    {
        "type": "text",
        "x": 5,
        "y": 15
    },
]


def build_starforce_unit(color, fill, letter, text_class, x_offset, y_offset) -> [svg.SVG]:
    return build_unit(starforce_unit, color, fill, letter, text_class, x_offset, y_offset)

