from pytube import YouTube
i=0
urls =["https://youtu.be/4KkZHaWQJgg",
"https://youtu.be/dGmf00kKqP8",
"https://youtu.be/lVQhqmQY6dw",
"https://youtu.be/9Wwa_9o3beg",
"https://youtu.be/ZYGckUwhtuw",
"https://youtu.be/wzld8qSGa_4",
"https://youtu.be/pP7yPiNdFTk"]
for url in urls:
    lin= YouTube(url)
    stream=lin.streams.get_highest_resolution()
    stream.download()
    i=i+1
    print(i)
    
print('we are Done')










