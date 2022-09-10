import svg


def build_rect(params) -> svg.Rect:
    center_x = params["x"] + (params["width"] / 2)
    center_y = params["y"] + (params["height"] / 2)

    return svg.Rect(
        x=params["x"],
        y=params["y"],
        width=params["width"],
        height=params["height"],
        fill=params["fill"],
        stroke=params["stroke"],
        stroke_width=params["stroke_width"],
        transform=[svg.Rotate(params["rotate"], center_x, center_y)]
    )


def build_circle(params) -> svg.Circle:
    return svg.Circle(
        cx=params["x"],
        cy=params["y"],
        r=params["radius"],
        fill=params["fill"],
        stroke=params["stroke"],
        stroke_width=params["stroke_width"]
    )


def build_text(params) -> svg.Text:
    return svg.Text(
        x=params["x"],
        y=params["y"],
        class_=params["text_class"],
        text=params["text"]
    )


def build_unit(unit_def, color, fill, letter, text_class, x_offset, y_offset) -> [svg.SVG]:
    elements = [build_rect({
        "type": "rect",
        "x": 0 + x_offset,
        "y": 0 + y_offset,
        "width": 48,
        "height": 48,
        "fill": fill,
        "stroke": color,
        "stroke_width": 0.0950182,
        "rotate": 0
    })]

    for item in unit_def:
        params = item.copy()
        params["stroke"] = color
        params["fill"] = params["fill"] if "fill" in params else color
        params["text_class"] = text_class

        params["x"] = item["x"] + x_offset
        params["y"] = item["y"] + y_offset

        if params["type"] == "rect":
            elements.append(build_rect(params))
        elif params["type"] == "circle":
            elements.append(build_circle(params))
        elif params["type"] == "text":
            params["text"] = letter
            elements.append(build_text(params))

    return elements
