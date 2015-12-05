
def readFileAndBuildUnique(filepath):
    data = [x.strip().split('\t')[0] for x in open(filepath, 'r').readlines()]
    wordList = set()
    for line in data:
        for word in line.split():
            if word not in "~!,'\".=-)([]#/@?.$%&*+:;>^_":
                wordList.add(word)
            # better create a set and convert to list later
            # if word not in wordList and word not in "~!,'\".":
            #    wordList.append(word)

    wordList = list(wordList)
    wordList.sort()
    print wordList
    print len(wordList)

    #for w in wordList:
    #    if len(w) < 2:
    #        print w
    #print len(wordList)

    vect = [ [ 0 for i in range(len(wordList))] for x in data]
    for l in range(len(vect)):
        for w in range(len(wordList)):
            if wordList[w] in data[l]:
                vect[l][w]++


    print len(vect)
    print wordList[4]
    for i in range(15):
        print vect[i][:20]



readFileAndBuildUnique("LearnSentiment-master/resources/liu_simple.txt")
