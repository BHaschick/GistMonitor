import json
import urllib
from subprocess import call
from urllib.request import urlopen
from urllib.error import HTTPError
import os
import sys
import math

### Fetches current gists of user from GitHub ###
def getUserRemoteGists(user):

    try:
        userurl = urlopen('https://api.github.com/users/' + user)
    except HTTPError as err:
        print("User %s: %s" % (user, str(err)))
        input("Press any button to continue.")
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

### Returns dictionary of gists for every existing/stored user ###
def getLocalGists():
    try:
        with open('./gists.txt', 'r') as json_file:
            gists = json.load(json_file)
        return gists
    except (FileNotFoundError):
        print("No gists have been previously stored")
        with open('./gists.txt', 'w+') as outputFile:
            outputFile.writelines("")
        return {}
    except Exception as e:
        print("Something went wrong in getting the stored gists: %s" % e)

def compareLocalAndRemoteGists(user, localGists, remoteGists):
    newGists = []
    try:
        if user not in localGists:
            return remoteGists
        for entry in remoteGists:
            if entry not in localGists[user]:
                newGists.append(entry) 
        return newGists
    except Exception as e:
        print("Could not compare local and remote gists. Returned error: %s" % str(e))

def writeOutGists(gists):
    try:
        data = json.dumps(gists)
        with open('./gists.txt', 'w') as outputFile:
            outputFile.writelines(data)
    except Exception as e:
        print("Results could not be written: " + str(e))

def displayNewGists(gists):
    stringBuilder = ""
    if len(gists) == 0:
        print("No valid users were found")
        return
    for user in gists:
        if len(gists[user]) == 0:
            print("No new gists were found for %s" % user)
            continue
        stringBuilder += "User %s has the following new gists:\n" % user
        for entry in gists[user]:
            stringBuilder += "\tID: %s, Updated: %s, Accessible via: %s\n" % (entry["id"], entry["updatedAt"], entry["html"])
    print(stringBuilder)

def getUserInput():
    
    userInput = str(input("Please enter a username or csv list of usernames: "))
    try:
        if userInput == "":
            print("Please enter a username")
            getUsers()
        if "," in userInput:
            userList=userInput.replace(' ','').split(',')
            return userList
        else:
            return [userInput]
    except:
        print("Something went wrong in getting the user. Please try again.")
        getUsers()
   
    