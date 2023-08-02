
import cairosvg
import os
import traceback
img_path='Course\\publish\\chapter6\\assets\\'
for svg_file in os.listdir(img_path):
    try:
        cairosvg.svg2png(url=img_path+svg_file, write_to=img_path+svg_file.replace('.svg','.png'),dpi=600)  
    except:
        print(svg_file+'转换失败')
        traceback.print_exc()