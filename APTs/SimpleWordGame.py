def points(player, dictionary):
    """
    return int representing points earned
    by player, a list of strings, based on
    words in dictionary, a list of strings
    """

    scores = []
    for word in set(player):
        if word in dictionary:
            score = (len(word))**2
            scores.append(score)
    return sum(scores)
