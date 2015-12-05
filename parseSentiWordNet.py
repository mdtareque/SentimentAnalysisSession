#!/usr/bin/python
wordList=[]

score_map = {}
def read_and_save(filepath):
    data = [x.strip().split('\t') for x in open(filepath, 'r').readlines()]
    for row in data:
        if '#' in  row[0]:
            continue  # we ignore commetns
        #print row
        words=row[4]
        pos_score = float(row[2])
        neg_score = float(row[3])
        #let's process
        words = [thisword.split('#')[0] for thisword in words.split()] # split on space by default
        #print words, pos_score, neg_score
        global score_map
        # There are multiple words
        for word in words:
            if word in score_map:
                # avg reoccurrences of word
                score_map[word] = (score_map[word] + pos_score-neg_score) / 2.0
                pass
                #score_map[word] = pos_score - neg_score
            else:
                score_map[word] = pos_score - neg_score


def get_word_score(word):
    global score_map
    if word in score_map:
        return score_map[word]
    else:
        return 0.0


def get_sentence_score(sentence):
    """
    Quick and dirty solution,
    no punctuations are removed, no stemming, no number removal
    """
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    score = []
    for word in sentence:
        score.append(get_word_score(word))
    return sum(score)/len(score)


def analyze(filepath):
    data = [x.strip().split('\t')[0] for x in open(filepath, 'r').readlines()]
    score=0
    for s in data:
        score += get_sentence_score(s)
    return score/len(data)




read_and_save('home/swn/www/admin/dump/SentiWordNet_3.0.0_20130122.txt')
print "done..."
print

print 'get_word_score("soamazing")'
print get_word_score("soamazing")
print 'get_word_score("able")'
print get_word_score("able")
print

print 'get_sentence_score("This is so Amazing")'
print get_sentence_score("This is so Amazing")
print

print 'get_sentence_score("This is so ugly")'
print get_sentence_score("This is so ugly")
print 'get_sentence_score("This is so ugly")'
print get_sentence_score("This is so ugly")
print

print 'get_sentence_score("this is not good")'
print get_sentence_score("this is not good")
print 'get_sentence_score("this is bad")'
print get_sentence_score("this is bad")
print

print 'analyze("LearnSentiment-master/resources/liu_simple.txt")'
print analyze('LearnSentiment-master/resources/liu_simple.txt')
