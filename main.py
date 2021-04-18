import helperFunctions as hf

def main():

    allRemoteGists = {}
    newGists = {}
    localGists = hf.getLocalGists()
    users = hf.getUsers()
    for user in users:
        
        remoteGists = hf.getUserRemoteGists(user)

        if len(remoteGists) == 0:
            print("%s has no gists. Removing from the list of users to check." % user)
            users.remove(user)
            continue

        allRemoteGists[user] = remoteGists
        newGists[user] = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
    
    hf.writeOutGists(allRemoteGists)
    hf.displayNewGists(newGists)

main()