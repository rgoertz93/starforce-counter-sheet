import svg
from units.base import build_unit

stargate_unit = []
degrees = [0, 45, 90, 135]


def build_stg_unit(d):
    return {
        "type": "rect",
        "x": 26.520185,
        "y": 14.764094,
        "width": 4.4080563,
        "height": 22.679024,
        "stroke_width": 0.237106,
        "rotate": d
    }


for degree in degrees:
    stargate_unit.append(build_stg_unit(degree))

stargate_unit.append(
    {
        "type": "circle",
        "x": 28.670834,
        "y": 26.170834,
        "stroke_width": 0.619355,
        "radius": 15.361156,
        "fill": "none"
    }
)
stargate_unit.append(
    {
        "type": "text",
        "x": 2.9596367,
        "y": 14.583309
    }
)


def build_stargate_unit(color, fill, letter, text_class, x_offset, y_offset) -> [svg.SVG]:
    return build_unit(stargate_unit, color, fill, letter, text_class, x_offset, y_offset)


