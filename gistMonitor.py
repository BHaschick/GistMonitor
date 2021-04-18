import helperFunctions as hf

def main():
    print("Loading data")
    allRemoteGists = {}
    newGists = {}
    localGists = hf.getLocalGists() #Load in all saved local gists for comparison
    users = hf.getUserInput() #Get input from user
    
    for user in users:
        print("Processing user: %s" % user)

        remoteGists = hf.getUserRemoteGists(user)

        if len(remoteGists) == 0:
            print("%s has no gists. Removing from the list of users to check." % user)
            users.remove(user)
            continue

        allRemoteGists[user] = remoteGists 
        newGists[user] = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
    
    hf.writeOutGists(allRemoteGists)
    hf.displayNewGists(newGists)
    input("Press any button to continue.")

main()