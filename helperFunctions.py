import json
import urllib
from subprocess import call
from urllib.request import urlopen
import os
import math

### Fetches current gists of user from GitHub ###
def getUserRemoteGists(user):
    perpage = 50.0
    userurl = urlopen('https://api.github.com/users/' + user)
    public_gists = json.load(userurl)
    gistcount = public_gists['public_gists']
    print ("Found user : " + user)
    print ("Found gists : " + str(gistcount))
    pages = int(math.ceil(float(gistcount)/perpage))
    print ("Found pages : " + str(pages))

    results = []

    for page in range(pages):
        pageNumber = str(page + 1)
        print ("Processing page number " + pageNumber)
        pageUrl = 'https://api.github.com/users/' + user + '/gists?page=' + pageNumber + '&per_page=' + str(int(perpage))
        u = urlopen (pageUrl)
        gists = json.load(u)
        #startd = os.getcwd()
        for gist in gists:   
            results.append(gist['id'])
    return results

### Returns dictionary of gists of every user ###
def getUsersStoredGists(user):
    try:
        with open('./contents/gists.txt', 'r') as json_file:
            gists = json.load(json_file)
        return gists
    except (FileNotFoundError):
        print("No gists have been previously stored for user: %s" % user)
        return {}
    except:
        print("Something went wrong in getting the stored gists for user: %s" % user)

def compareUserAndGists(user, gists):
    pass

def writeResults(user, resultsList):
    if len(resultsList) > 0:
        gistResult = {user:resultsList}
    try:
        with open('./contents/gists.txt', 'w+') as json_file:
            json.dumps(gistResult, json_file)
    except:
        print("Results couldn't be written")

def returnNewGists():
    pass