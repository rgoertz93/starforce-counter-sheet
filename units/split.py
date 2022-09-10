import svg

from models import black, orange, light_green, light_blue, dark_blue
from units.base import build_border, build_text, build_centered_text
from units.number import build_char_unit

split_top_def = {
    "x": 24,
    "y": 20,
}

split_bottom_def = {
    "x": 24,
    "y": 38,
}


def build_signed_num_string(num):
    if num > 0:
        return f"+{num}"
    return f"{num}"


def build_split(top_text, bottom_text, top_class, bottom_class, color, fill, x_offset, y_offset) -> [svg.SVG]:
    elements = [
        build_border(color, fill, x_offset, y_offset),
        build_centered_text({
            "x": split_top_def["x"] + x_offset,
            "y": split_top_def["y"] + y_offset,
            "text_class": top_class,
            "text": top_text
        }),
        build_centered_text({
            "x": split_bottom_def["x"] + x_offset,
            "y": split_bottom_def["y"] + y_offset,
            "text_class": bottom_class,
            "text": bottom_text
        })
    ]

    return elements


def draw_split_column(start_num, color, fill, x_offset, y_offset) -> [svg.SVG]:
    elements = []

    for n in range(start_num, start_num + 10):
        elements.append(build_split(f'{n:02}', build_signed_num_string((n - 20) * -1), "split-text", "split-italic-text", color, fill, x_offset, y_offset))
        x_offset += 48

    return elements


def draw_brkf_column(x_offset, y_offset) -> [svg.SVG]:
    elements = [
        build_split("Brkf", build_signed_num_string(0), "split-text", "split-italic-text", black, orange, x_offset, y_offset)
    ]

    x_offset += 48
    elements.append(build_split("Dstr", build_signed_num_string(0), "split-text", "split-italic-text", black, orange, x_offset, y_offset))
    x_offset += 48

    for n in range(21, 29):
        elements.append(build_split(f'{n:02}', build_signed_num_string((n - 20) * -1), "split-text", "split-italic-text", black, light_green, x_offset, y_offset))
        x_offset += 48

    return elements


def draw_dstr_column(x_offset, y_offset) -> [svg.SVG]:
    elements = [
        build_split(39, "-19", "split-text", "split-italic-text", black, light_green, x_offset, y_offset)
    ]

    x_offset += 48
    elements.append(build_split("Dstr", "-20", "split-text", "split-italic-text", black, orange, x_offset, y_offset))
    x_offset += 48
    elements.append(build_split("Dstr", "-21", "split-text", "split-italic-text", black, orange, x_offset, y_offset))
    x_offset += 48

    for n in range(1, 8):
        elements.append(build_char_unit(black, light_blue, "N", "black-num-text", x_offset, y_offset))

        x_offset += 48

    return elements


def draw_tac_sit_column(x_offset, y_offset) -> [svg.SVG]:
    elements = []

    x_offset += 48
    elements.append(build_split("TAC", "SIT", "split-text", "split-text", black, light_blue, x_offset, y_offset))
    x_offset += 48
    elements.append(build_split("TAC", "SIT", "blue-split-text", "blue-split-text", dark_blue, light_blue, x_offset, y_offset))
    x_offset += 48

    for n in range(1, 8):
        elements.append(build_char_unit(dark_blue, light_blue, "N", "blue-num-text", x_offset, y_offset))

        x_offset += 48

    return elements
