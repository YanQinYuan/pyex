#生成激活码图片

# coding=utf-8

# def generate(self, size=(120, 30), chars=None, format='PNG', mode='RGB', bg_color=(255, 255, 255), fg_color=(0, 0, 255), font_size=18, font_file=None, length=4, draw_lines=True, line_range=(1, 2), draw_points=True, point_chance=2):
    
#     """
#     @param size: 图片的大小，格式（宽，高），默认为(120, 30)
#     @param chars: 允许的字符集合，格式字符串
#     @param format: 图片保存的格式，默认为 PNG，可选的为 GIF，JPEG，TIFF，PNG
#     @param mode: 图片模式，默认为 RGB
#     @param bg_color: 背景颜色，默认为白色
#     @param fg_color: 前景色，验证码字符颜色，默认为蓝色 #0000FF
#     @param font_size: 验证码字体大小
#     @param font_file: 验证码字体，默认为 None
#     @param length: 验证码字符个数
#     @param draw_lines: 是否划干扰线
#     @param line_range: 干扰线的条数范围，格式元组，默认为 (1, 2)，只有 draw_lines 为s True 时有效
#     @param draw_points: 是否画干扰点
#     @param point_chance: 干扰点出现的概率，大小范围 [0, 100]，只有 draw_points 为 True 时有效
#     @return: [0]: PIL Image 实例
#     @return: [1]: 验证码图片中的字符串


import gvcode
img, code = gvcode.generate()
print(code)
#img.show()
img.save('D:/www/python-ex/verification.jpg')