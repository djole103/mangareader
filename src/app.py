import urllib.request
import re
import webbrowser
import os, sys
import tkinter as tk
import pprint

class Manga:
    def __init__(self, title, htmltitle, lastread=1, newestchap=1):
        self.title = title
        self.htmltitle = htmltitle
        self.newestchap = newestchap
        self.alert = True
        self.lastread = lastread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def onExit(self):
            f = open("mangas.txt",'w')
            for manga in mangadict.values():
                f.write("%s %s\n" % (manga.htmltitle,manga.lastread))
            root.destroy()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Open a newer chapter\n(click me)"
        self.hi_there["command"] = lambda: newchapteropen(mangadict["Bleach"])
        self.hi_there.pack(side="top")

        self.addmanga = tk.Button(self)
        self.addmanga["text"] = "Add a manga!"
        self.addmanga["command"] = lambda: print(self.newmangastr)#lambda: addManga(TEXTBOXVALUE)
        self.addmanga.pack(side="top")

        self.newmanga = tk.Entry()
        self.newmanga.pack()
        self.newmangastr = tk.StringVar(value=self.newmanga)

        #add a textbox to input title and option for most recently read

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=self.onExit)
        self.QUIT.pack(side="bottom")




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
        file.close()
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

def addManga(title,lastread=1):
    if not mangadict[title]:
        mangadict[title] = Manga(title,titleToHtml(title),lastread=lastread)
        with open("mangas.txt", "a") as file:
            file.write("%s %s" % title,lastread)
    else:
        #when you press the exit button the db file will be updated
        mangadict[title].lastread = lastread




def deleteManga(title):
    if mangadict[title]:
        del mangadict[title]
        f = open("mangas.txt",'w')
        for manga in mangadict.values():
            f.write("%s %s\n" % (manga.htmltitle,manga.lastread))


mangadict = dict_init()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

#newchapteropen(mangadict["Bleach"])

#print("{} {}\n".format(mangadict["Bleach"].htmltitle, int(mangadict["Bleach"].newestchap)))
