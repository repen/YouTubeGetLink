from pytube import YouTube
def get_video(url):
    ob = YouTube(url)
    return ob
