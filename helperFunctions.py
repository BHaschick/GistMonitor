import json
import urllib
from subprocess import call
from urllib.request import urlopen
import os
import math

### Fetches current gists of user from GitHub ###
def getUserRemoteGists(user):

    try:
        userurl = urlopen('https://api.github.com/users/' + user)
    except urllib.request.HTTPError:
        print("user %s was not found" % user)
        return {}
    except:
        print("An error occured in requesting the user: %s" % user)
        return {}
    
    perpage = 50.0
    public_gists = json.load(userurl)
    gistcount = public_gists['public_gists']
    print ("Found user : " + user)
    print ("Found gists : " + str(gistcount))
    pages = int(math.ceil(float(gistcount)/perpage))

    results = []
    for page in range(pages):
        pageNumber = str(page + 1)
        pageUrl = 'https://api.github.com/users/' + user + '/gists?page=' + pageNumber + '&per_page=' + str(int(perpage))
        u = urlopen (pageUrl)
        gists = json.load(u)
        for gist in gists:
            tempResult = {gist['id']}
            results.append({"id":gist['id'], "updatedAt":gist['updated_at'],"html":gist['html_url']}) #id: [updated,html]
    return results

### Returns dictionary of gists of every user ###
def getLocalGists():
    try:
        with open('./contents/gists.txt', 'r') as json_file:
            gists = json.load(json_file)
        return gists
    except (FileNotFoundError):
        print("No gists have been previously stored")
        return {}
    except:
        print("Something went wrong in getting the stored gists")

def compareLocalAndRemoteGists(user, localGists, remoteGists):
    pass

def writeOutGists(gists):
    try:
        data = json.dumps(gists)
        with open('./contents/gists.txt', 'w+') as outputFile:
            outputFile.writelines(data)
    except Exception as e:
        print("Results could not be written: " + str(e))

def displayNewGists(gists):
    stringBuilder = ""
    for user in gists:
        stringBuilder += "User %s has the following new gists:\n" % user
    print(stringBuilder)