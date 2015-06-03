import urllib.request
import re
import webbrowser
import os, sys

class Manga:
    def __init__(self,title,nc = 1 ):
        self.title = title
        self.nc = int(nc)
        self.alert = True
        self.lastread = int(0)  

def list_init():
	try:
		#dir = os.path.dirname(__file__)
		dir = os.getcwd()
		#dir = sys.path.append(os.path.realpath('..'))
		print(dir)
		filename = dir + '/mangas.txt'
		print(filename)
		file = open(filename,'r+')
		mlist = []
		lines = file.readlines()
		for line in lines:
			mlist.append(Manga(line.split(' ')[0],line.split(' ')[1]))
		return mlist
	except IOError:
        	print("IOError couldn't open mangas.txt\n")
    
       
def newchaptercheck(manga):
    html_content = urllib.request.urlopen('http://www.mangareader.net/{0}'.format(manga.title)).read()
    matches = re.findall(str(manga.nc),str(html_content))
    if len(matches) != 0:
        webbrowser.open("http://www.mangareader.net/{0}/{1}".format(manga.title,str(manga.nc)))
    else:
        print("Error searching for manga couldn't find newest chapter")

    
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
