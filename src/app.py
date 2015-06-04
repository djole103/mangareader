import urllib.request
import re
import webbrowser
import os, sys

class Manga:
    def __init__(self,title,lastread = None, newestchap=None ):
        self.title = title
        self.newestchap = newestchap
        self.alert = True
        self.lastread = lastread  

def dict_init():
	try:
		dir = os.getcwd()
		filename = dir + '/mangas.txt'
		file = open(filename,'r+')
		mangadict = {}
		lines = file.readlines()
		for line in lines:
			title = line.split(' ')[0]
			lastread = line.split(' ')[1]
			mangadict[title] = Manga(title,lastread)
		return mangadict
	except IOError:
        	print("IOError couldn't open mangas.txt\n")
    


def list_init():
	try:
		dir = os.getcwd()
		filename = dir + '/mangas.txt'
		file = open(filename,'r+')
		mangalist = []
		lines = file.readlines()
		for line in lines:
			mlist.append(Manga(line.split(' ')[0],line.split(' ')[1]))
		return mangalist
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


mangadict = dict_init()
newchapteropen(mangadict["bleach"])

print("{} {}\n".format(mangadict["bleach"].title,int(mangadict["bleach"].newestchap))

#refresh(mlist)

#for x in mlist:
#    print("{} {}\n".format(x.title,x.nc))
#    
# shingeki = Manga("shingeki-no-kyojin",63)
# a.append(shingeki)
# for x in a:
#     newchaptercheck(x)
#x = input('Gimme da money: ')
