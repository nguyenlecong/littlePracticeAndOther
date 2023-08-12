import os
from moviepy.editor import *
from utils import *
config()


class ClipCombiner():
    def __init__(self, clip_folder):
        self.fps = 30
        self.size = (1920, 1080)
        self.fontsize = 70
        self.duration = 5  # second
        self.color = 'white'
        self.clip_folder = clip_folder
        self.clips = []

    def create_intro_clip(self, text):
        intro_clip = TextClip(text,
                              size=self.size,
                              fontsize=self.fontsize,
                              color=self.color
                              ).set_duration(self.duration)
        return intro_clip

    def create_clip(self):
        print('Processing...')
        for file in sorted(os.listdir(self.clip_folder), key=get_key):
            base_name = file[:-4]
            intro_clip = self.create_intro_clip(base_name)
            self.clips.append(intro_clip)

            file_path = os.path.join(self.clip_folder, file)
            clip = VideoFileClip(file_path)
            self.clips.append(clip)

    def save_clip(self, output_name):
        final = concatenate_videoclips(self.clips)
        final.write_videofile(f"{output_name}.mp4", fps=self.fps)

    def run(self, output_name):
        self.create_clip()
        self.save_clip(output_name)


if __name__ == '__main__':
    clip_combiner = ClipCombiner('Matt')
    clip_combiner.run('full_course')
