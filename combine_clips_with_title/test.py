from moviepy.editor import *
from utils import *
config()


text = 'Bài 1- Thứ bạn cần thay đổi!'
txt_clip = TextClip(text,
                    size=(1920, 1080),
                    fontsize=70, color='white').set_duration(5)

final_clip = concatenate_videoclips([txt_clip], method="compose")
final_clip.write_videofile("my_concatenation.mp4", fps=30, codec='mpeg4')
