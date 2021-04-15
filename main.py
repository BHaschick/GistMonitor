'''
Using the Github API you should query a user’s publicly available github gists. The script should then tell you when a new gist has been published.
'''
import helperFunctions as hf


users = ['FiyinfobaO']
localGists = hf.getUsersStoredGists()

for user in users:
    remoteGists = hf.getUserRemoteGists(user)
    newGists = hf.compareLocalAndRemoteGists(user, localGists, remoteGists)
    if len(newGists) > 0:
        hf.writeResults(user, newGists)