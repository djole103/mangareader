import urllib.request
import re
import webbrowser
import os, sys
import pprint

# refresh(mlist)

# for x in mlist:
#    print("{} {}\n".format(x.title,x.nc))
#    
# shingeki = Manga("shingeki-no-kyojin",63)
# a.append(shingeki)
# for x in a:
#     newchaptercheck(x)
# x = input('Gimme da money: ')

class Manga:
    def __init__(self, title, lastread=1, newestchap=1):
        self.title = title
        self.newestchap = newestchap
        self.alert = True
        self.lastread = lastread


def dict_init():
    try:
        dir = os.getcwd()
        filename = dir + '/mangas.txt'
        file = open(filename, 'r+')
        mangadict = {}
        lines = file.readlines()
        for line in lines:
            title = line.split(' ')[0]
            lastread = int(line.split(' ')[1])
            print("%s" % title)
            mangadict[title] = Manga(title=title, lastread=lastread)
        return mangadict
    except IOError:
        print("IOError couldn't open mangas.txt\n")


def newchapteropen(manga):
    refresh(manga)
    if manga.lastread < manga.newestchap:
        try:
            webbrowser.open("http://www.mangareader.net/{0}/{1}".format(manga.title, str(manga.lastread + 1)))
            manga.lastread += 1
        except Exception as e:
            print("Couldn't open the new chapter! Exception: %s" % e)
    else:
        print("No new chapters sorry bud!")


def refresh(manga):
    print("http://www.mangareader.net/%s" % manga.title)
    html_content = urllib.request.urlopen('http://www.mangareader.net/{0}'.format(manga.title)).read()
    while (len(re.findall(pattern=str(manga.newestchap + 1), string=str(html_content))) > 0):
        manga.newestchap += 1
        if (manga.newestchap > manga.lastread):
            manga.alert = True

def titleFormat(title):
    return re.sub(pattern='\ ',repl='-',string=title.lower())


mangadict = dict_init()
newchapteropen(mangadict["bleach"])

print("{} {}\n".format(mangadict["bleach"].title, int(mangadict["bleach"].newestchap)))
