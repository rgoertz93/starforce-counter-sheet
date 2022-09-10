import svg

from units.base import build_rect, build_border, build_text

number_def = {
    "x": 17,
    "y": 32,
}

underline_def = {
    "x": 19.9,
    "y": 35.2,
    "width": 8,
    "height": 1.58,
    "stroke_width": 0.0181455,
    "rotate": 0
}


def build_underline(color, fill, text_class, x_offset, y_offset) -> svg.Rect:
    params = underline_def.copy()
    params["stroke"] = color
    params["fill"] = fill
    params["text_class"] = text_class
    params["x"] = underline_def["x"] + x_offset
    params["y"] = underline_def["y"] + y_offset

    return build_rect(params)


def build_char_unit(color, fill, num, text_class, x_offset, y_offset) -> [svg.SVG]:
    return [
        build_border(color, fill, x_offset, y_offset),
        build_text({
            "x": number_def["x"] + x_offset,
            "y": number_def["y"] + y_offset,
            "text_class": text_class,
            "text": num
        })
    ]


def draw_number_column(color, fill, text_class, x_offset, y_offset) -> [svg.SVG]:
    elements = []

    for n in range(0, 10):
        elements.append(build_char_unit(color, fill, str(n), text_class, x_offset, y_offset))

        if n in (6, 9):
            elements.append(build_underline(color, color, text_class, x_offset, y_offset))

        x_offset += 48

    return elements
