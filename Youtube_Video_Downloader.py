import pytube

link = input('Youtube Video URL :')
video_download = pytube.YouTube(link)
video_download.streams.get_highest_resolution().download()
print('Video Downloaded', link)