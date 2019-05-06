def winners(ballot):
    candidateList = []
    for i in ballot:
        iSplit = i.split()
        candidateList.extend(iSplit)
    totalVotesAllowed = len(ballot[0].split())
    candidateList = set(candidateList)
    dicList = []
    for i in candidateList:
        canList = [i, 0]
        dicList.append(canList)
    d = {key: value for (key, value) in dicList}
    for votesRecorded in ballot:
        voteList = votesRecorded.split()
        for candidate in d.keys():
            if candidate in voteList:
                votes = totalVotesAllowed - voteList.index(candidate)
                d[candidate] += votes
    maxVotes = max((list((d.values()))))
    currentStatus = list(d.items())
    maxVotesCandidates = []
    for i in currentStatus:
        if i[1] == maxVotes:
            maxVotesCandidates.append(i[0])
    maxVotesCandidates.sort()
    return maxVotesCandidates

if __name__ == '__main__':

    print(winners(['slim jim tim kim', 'jim slim tim kim', 'jim slim tom tam', 'slim jim tom tam', 'tom tam bob jim',
     'tom tam bob slim', 'tam tom bob jim', 'tam tom bob slim']))