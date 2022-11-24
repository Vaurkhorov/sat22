import os
import shutil

import webbrowser
new = 2  # open in a new tab, if possible

url = "site"

f = open(url + r"\article.html", "r")

content = f.readlines()
foundKeywords = False
keywords = ""

for i in content:
    if "keywords" in i:
        keywords = tuple(i.split("keywords")[1].split("\"")[2].split(","))
        foundKeywords = True
        break

f.close()

requiredAd = None

keywords = map(lambda b: b.strip(), keywords)

for _ in keywords:
    print(_)
    if _ in map(lambda a: a.split(".")[0], os.listdir(url + r"\ads\\")):
        requiredAd = _ + ".png"

if requiredAd is not None:
    print(requiredAd)
    shutil.copyfile(url + "\\ads\\" + requiredAd, url + "\\ad.png")

webbrowser.open(r"site/article.html", new=new)
