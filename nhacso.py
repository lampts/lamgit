import urllib2
from xml.dom.minidom import parseString
import sys
import os
from urllib import urlretrieve
import re

# global variable
out_folder = "C:/Users/gnt/Desktop/NCT/"

# local functions

def nhacso_getXMLPath(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read()
    p = re.compile(r"xmlPath=http://[\w\d:#@%/;$()~_?\+-=\\\.&]*")
    xmlRe = p.search(page).group()
    xmlpath = xmlRe.replace('xmlPath=','').split('&')[0]
    return xmlpath

def nhacso_getalbum(url):
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()

    dom = parseString(data)
    xmlTag = dom.getElementsByTagName('mp3link')
    lst = []
    for i in range(len(xmlTag)):
               xmlTag1 = xmlTag[i].toxml()
               xmlData = xmlTag1.replace('<mp3link>','').replace('</mp3link>','')
               stData = xmlData.replace('<![CDATA[','').replace(']]>','')
               lst.append(stData)
    return lst
                   
# main function
if __name__ == "__main__":
    if len(sys.argv) != 2: # the program name and the two arguments
        sys.exit("python nhacso.py --url")
        
    # how to get this url? => firebug, script done later on
    
    print "> importing url!"
    # url = "http://nhacso.net/flash/album/xnl/1/uid/X1xWUUNaagUDAw==,WlxWUA==,Xg==,1325565352?1325565260148"

    xmlurl = nhacso_getXMLPath(sys.argv[1])    

    lst_mp3 = nhacso_getalbum(xmlurl)
    for i in lst_mp3:
        print i
        filename = i.split("/")[-1]
        print ">> ", filename
        outpath = os.path.join(out_folder, filename)
        urlretrieve(i, outpath)
        print "$ ", outpath
