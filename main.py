'''
Using the Github API you should query a user’s publicly available github gists. The script should then tell you when a new gist has been published.
'''
import helperFunctions as hf

users = ['gwrgergreg', 'Haschick', 'FiyinfobaO', 'subratrout']
allRemoteGists = {}
newGists = {}
localGists = hf.getLocalGists()
print(localGists)
'''
for user in users:
    
    remoteGists = hf.getUserRemoteGists(user)
    
    if len(remoteGists) == 0:        
        continue

    allRemoteGists[user] = remoteGists
    newGists[user] = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
    
hf.displayNewGists(localGists)    #change later to new gists
#hf.writeOutGists(allRemoteGists)
'''