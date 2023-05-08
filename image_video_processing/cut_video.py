import argparse 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


ap = argparse.ArgumentParser()
ap.add_argument('-i', default='out.avi')
args = ap.parse_args()

vid_path = args.i
vid_name = vid_path.split('/')[-1]
targetname = vid_path.replace(vid_name, 'cut_'+vid_name)

start_time = 
end_time = 60

ffmpeg_extract_subclip(vid_path, start_time, end_time, targetname=targetname)
