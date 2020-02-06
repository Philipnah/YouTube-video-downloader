import os
# youtube-dl is a requirement, install with: pip install youtube-dl

link = input("Insert link here: ")


videotitle = os.system('youtube-dl --skip-download --get-title -q ' + link)

videooraudio = input("\nDo you want to download only the audio, or both video and audio? v/a: ")
ifvideo = ""
ifvideoend = ""
Quality = ""

if videooraudio == "v":
    Quality = input("1080, 720 or 480: ") # 1080 and 720 doesn't seem to work
    selectedpath = input("insert the path to where you want to download it to (default is cwd)")
    videooraudio = "best"
    ifvideo = ')[height>'
    ifvideoend = ']" '

elif videooraudio == "a":
    videooraudio = "bestaudio) "


downloadfunc = 'youtube-dl -f "(' + videooraudio + ifvideo + Quality + ifvideoend + link
os.system(downloadfunc)