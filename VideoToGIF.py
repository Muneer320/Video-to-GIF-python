from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4")

clip.write_gif("video.gif")