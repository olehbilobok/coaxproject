import urllib.request
from moviepy.editor import VideoFileClip
import os

url = "https://v16-webapp.tiktok.com/2ec6654796f17904c0c8390e516d62d8/62e909d3/video/tos/maliva/\
tos-maliva-ve-0068c799-us/c3bfb39877af4ff2b576dfc1fdda438a/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%\
7C0%7C1%7C0&cv=1&br=4036&bt=2018&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZGHRKwe2NiZ3yl7Gb&mime_type=video_mp4&qs=0&\
rc=NjM5NTpkaTQ1aDY1ZTtlZkBpMzY2eTU6ZnlzOzMzZzczNEAxNDYzMzI2X18xYS9hLi82YSM2NGtxcjRfNmJgLS1kMS9zcw%3D%3D&\
l=202208020524220101921680800B8ACE05"


def get_video():

    video_file = 'tik_tok_video.mp4'
    urllib.request.urlretrieve(url, video_file)
    return video_file


def convert_video(video_file):

    gif_file = "tik_tok.gif"
    videoClip = VideoFileClip(video_file)
    videoClip.write_gif(gif_file, fps=5)
    return gif_file


def get_gif_path(gif_file):

    print(os.path.abspath(gif_file))


if __name__ == "__main__":

    video_file = get_video()
    gif_file = convert_video(video_file)
    get_gif_path(gif_file)