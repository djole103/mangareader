import urllib.request
import re
import webbrowser
import os, sys
import tkinter
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
    def __init__(self, title, htmltitle, lastread=1, newestchap=1):
        self.title = title
        self.htmltitle = htmltitle
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
            title = htmlToTitle(line.split(' ')[0])
            htmltitle = line.split(' ')[0]
            lastread = int(line.split(' ')[1])
            print("%s" % title)
            mangadict[title] = Manga(title=title, htmltitle=htmltitle, lastread=lastread)
        return mangadict
    except IOError:
        print("IOError couldn't open mangas.txt\n")


def newchapteropen(manga):
    refresh(manga)
    if manga.lastread < manga.newestchap:
        try:
            webbrowser.open("http://www.mangareader.net/{0}/{1}".format(manga.htmltitle, str(manga.lastread + 1)))
            manga.lastread += 1
        except Exception as e:
            print("Couldn't open the new chapter! Exception: %s" % e)
    else:
        print("No new chapters sorry bud!")


def refresh(manga):
    print("http://www.mangareader.net/%s" % manga.htmltitle)
    html_content = urllib.request.urlopen('http://www.mangareader.net/{0}'.format(manga.htmltitle)).read()
    while (len(re.findall(pattern="%s %s" % (manga.title,str(manga.newestchap)), string=str(html_content))) > 0):
        manga.newestchap += 1
        if (manga.newestchap > manga.lastread):
            manga.alert = True

# Foo Bar -> foo-bar
def titleToHtml(title):
    return re.sub(pattern='\ ',repl='-',string=title.lower())

# foo-bar -> Foo Bar
def htmlToTitle(htmltitle):
    lowertitle = re.sub(pattern='-',repl=' ',string=htmltitle)
    return lowertitle.title()

#def addManga(title,lastread):

#def deleteManga(title):


mangadict = dict_init()
newchapteropen(mangadict["Bleach"])

print("{} {}\n".format(mangadict["Bleach"].htmltitle, int(mangadict["Bleach"].newestchap)))
