import pytube

link=input('Enter your link:')
yt=pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded',link)
