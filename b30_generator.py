from PIL import Image, ImageDraw, ImageFont
import datetime

def generate_image(data_dict):
    width, height = 800, 600
    background_color = (255, 255, 255)
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_size_small = 16
    font_small = ImageFont.truetype("arial.ttf", font_size_small)  # Define font_small here
    x, y = 20, 20
    dx, dy = 130, 120

    max_line_heights = {}

    for i, (title, values) in enumerate(data_dict.items()):
        row, col = divmod(i, cols)
        x_offset, y_offset = col * dx, row * dy
        position = (x + x_offset, y + y_offset)

        font_big, max_title_height = get_optimal_font(draw, title, font_size_small, dx)
        max_line_heights.setdefault(row, []).append(max_title_height)

        draw.text(position, title, font=font_big, fill=(0, 0, 0))

        line_y = position[1] + max_title_height + font_size_small
        for j, value in enumerate(values):
            draw.text((position[0], line_y), str(value), font=font_small, fill=(0, 0, 0))
            line_y += font_size_small

    for row, max_heights in max_line_heights.items():
        max_row_height = max(max_heights)
        for col in range(cols):
            x_offset, y_offset = col * dx, row * dy
            position = (x + x_offset, y + y_offset + max_row_height)
            max_line_heights[row] = max_row_height

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"./output/output_{formatted_datetime}.png"
    image.save(output_filename)

def get_optimal_font(draw, text, font_size, max_width):
    font = ImageFont.truetype("arial.ttf", 100)
    text_width, text_height = draw.textsize(text, font=font)

    while text_width > max_width:
        font_size -= 1
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font=font)

    return font, text_height

cols = 6
