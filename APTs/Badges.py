def findLabel(labels, deeds, needs):
    numBadges = len(labels)
    for index in range(numBadges):
        if (set(needs[index].split()) < set(deeds)) or (set(needs[index].split()) == set(deeds)):
            return labels[index]
    return "nobadge"