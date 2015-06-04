import urllib.request
import re
import webbrowser
import os, sys

class Manga:
    def __init__(self,title,lastread = None ):
        self.title = title
        self.newestchap = int(newestchap)
        self.alert = True
        self.lastread = lastread  

def list_init():
	try:
		dir = os.getcwd()
		print(dir)
		filename = dir + '/mangas.txt'
		file = open(filename,'r+')
		mlist = []
		lines = file.readlines()
		for line in lines:
			mlist.append(Manga(line.split(' ')[0],line.split(' ')[1]))
		return mlist
	except IOError:
        	print("IOError couldn't open mangas.txt\n")
    
       
def newchapteropen(manga):
    if manga.lastread < manga.newestchap:
	try:
       		webbrowser.open("http://www.mangareader.net/{0}/{1}".format(manga.title,str(manga.lastread+1)))
		manga.lastread +=1
	except Exception as e:
		print("Couldn't open the new chapter! Exception: %s" % e)
    else:
        print("No new chapters sorry bud!")

    
def refresh(mlist):
    for manga in mlist:
        html_content = urllib.request.urlopen('http://www.mangareader.net/{0}'.format(manga.title)).read()
        while(len(re.findall(str(manga.nc+1),str(html_content)))>0):
            manga.nc+=1
        if(manga.nc>manga.lastread):
            manga.alert = True


mlist = list_init()
newchaptercheck (mlist[0])
#refresh(mlist)

for x in mlist:
    print("{} {}\n".format(x.title,x.nc))
#    
# shingeki = Manga("shingeki-no-kyojin",63)
# a.append(shingeki)
# for x in a:
#     newchaptercheck(x)
print(("a","b"))
x = input('Gimme da money: ')
