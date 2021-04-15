'''
Using the Github API you should query a user’s publicly available github gists. The script should then tell you when a new gist has been published.
'''

import json
import urllib
from subprocess import call
from urllib.request import urlopen
import os
import math
USER = 'FiyinfobaO'

perpage=30.0
userurl = urlopen('https://api.github.com/users/' + USER)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']
print ("Found gists : " + str(gistcount))
pages = int(math.ceil(float(gistcount)/perpage))
print ("Found pages : " + str(pages))

#f=open('./contents/' + USER + '-contents.txt', 'w+')

for page in range(pages):
    pageNumber = str(page + 1)
    print ("Processing page number " + pageNumber)
    pageUrl = 'https://api.github.com/users/' + USER  + '/gists?page=' + pageNumber + '&per_page=' + str(int(perpage))
    u = urlopen (pageUrl)
    gists = json.load(u)
    #startd = os.getcwd()
    for gist in gists:
        print (gist)
        gistId = gist['id']
        gistUrl = 'git://gist.github.com/' + gistId + '.git' 

        if gist['description'] == None:
            description = ''
        else:
            description = gist['description']#.encode('utf8')#.replace("\r",' ').replace("\n",' ')
        #print (gist['id'], gistUrl, description)