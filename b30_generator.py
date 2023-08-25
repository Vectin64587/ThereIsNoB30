from PIL import Image, ImageDraw, ImageFont
import datetime,ast

def generate_image(data_dict):
    # 创建一个白色背景的图片
    width, height = 800, 600
    background_color = (255, 255, 255)
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # 字体设置
    font_size_big = 24
    font_size_small = 16
    font_big = ImageFont.truetype("arial.ttf", font_size_big)
    font_small = ImageFont.truetype("arial.ttf", font_size_small)

    # 按单曲 PTT 大小降序排序字典项
    sorted_data = sorted(data_dict.items(), key=lambda x: x[1][2], reverse=True)

    # 绘制每行的内容
    rows, cols = 5, 6
    x, y = 20, 20  # 初始位置
    dx, dy = 130, 120  # 每个组之间的间隔

    for i, (title, values) in enumerate(sorted_data):
        row, col = divmod(i, cols)
        x_offset, y_offset = col * dx, row * dy
        position = (x + x_offset, y + y_offset)

        # 绘制粗体标题
        draw.text(position, title, font=font_big, fill=(0, 0, 0))

        # 绘制分数、定数、大小 P、单曲 PTT
        for j, value in enumerate(values):
            line_y = position[1] + font_size_big + (j + 1) * font_size_small
            draw.text((position[0], line_y), str(value), font=font_small, fill=(0, 0, 0))

    # 获取当前日期和时间作为文件名的一部分
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # 保存图片
    output_filename = f"./output/output_{formatted_datetime}.png"
    # 保存图片
    image.save(output_filename)

# 示例字典数据
# data_dict = {
#     "Group 1": [95, 9, 5.12, 965],
#     "Group 2": [82, 8, 4.85, 850],
#     "Group 3": [78, 7, 4.60, 820],
#     # ... 继续添加数据 ...
#     "Group 30": [67, 6, 4.30, 750]
# }




