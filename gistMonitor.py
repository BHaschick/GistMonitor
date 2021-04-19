# pyinstaller --onefile gistMonitor.py
import helperFunctions as hf

def main():
    print("Loading data")
    allRemoteGists = {}
    newGists = {}
    localGists = hf.getLocalGists() #Load in all saved local gists for comparison
    users = hf.getUserInput() #Get input from user
    
    for user in users:
        print("\nProcessing user: %s" % user)

        remoteGists = hf.getUserRemoteGists(user)

        if len(remoteGists) == 0:
            print("%s has no gists." % user)            
        else:    
            allRemoteGists[user] = remoteGists 
            newGists[user] = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
    
    allGists = hf.combineLocalAndRemoteGists(localGists, allRemoteGists)
    hf.writeOutGists(allGists)
    hf.displayNewGists(newGists)
    input("Press any button to continue.")

main()