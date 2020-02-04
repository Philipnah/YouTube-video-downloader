import pytube as pt

link = input("Insert link here: ")

videotitle = pt.YouTube(url=link)

filesize = pt.Stream.filesize(link.get())

selectedpath = input("insert the path to where you want to download it to (default is cwd)")

print("Selected video is called:", videotitle + ". The video will use up:", filesize*10**6, "\nAre you sure you want to download it? y/N")


# pt.Stream.download(output_path=selectedpath, filename=videotitle)

print(videotitle)