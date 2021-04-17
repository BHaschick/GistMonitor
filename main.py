import helperFunctions as hf

users = ['gwrgergreg', 'FiyinfobaO', 'subratrout']
users = ['FiyinfobaO']
allRemoteGists = {}
newGists = {}
localGists = hf.getLocalGists()

for user in users:
    
    #remoteGists = hf.getUserRemoteGists(user)
    remoteGists = hf.getFakeRemoteGists()    
    if len(remoteGists) == 0 or (user not in remoteGists):
        users.remove(user)
        continue

    allRemoteGists[user] = remoteGists
    #newGists[user] = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
  
#hf.writeOutGists(allRemoteGists)
hf.displayNewGists(newGists)