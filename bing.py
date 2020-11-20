import requests
import os

def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

imgurl=requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
url="https://cn.bing.com/"+getmidstring(imgurl.text,'url":"','&rf')
date=getmidstring(imgurl.text,'startdate":"','","')
filename=date+".jpg"

img=requests.get(url)
open("src/"+filename, 'wb').write(img.content)

os.system("git add src/"+filename)
os.system("git commit -m '"+date+"的必应壁纸'")
