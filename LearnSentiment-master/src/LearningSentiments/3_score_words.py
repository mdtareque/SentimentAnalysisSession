'''
We assume a tab separated training file with sentence in first column and sentiment label in second column. 
This class would learn the ratio of a word to be in positive or negative sentence.
This ratio would then be used to compute sentiment of the whole sentence.

TODO: Modify it to use bigrams

'''
import string
import random
class ScoreLearner():
    stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    def __init__(self):
        pass
    
    def evaluate(self,filepath):
        testing_data = [x.strip().split('\t') for x in open(filepath, 'r').readlines()]
        correct = 0
        for i in range(len(testing_data)):
            sentence = testing_data[i][0]
            sentimentlabel = testing_data[i][1]
            predict = self.prediction(sentence)
            actual = sentimentlabel
            if predict > 0 and actual=="1" :
                correct+=1
            if predict < 0 and actual=="0" :
                correct+=1
        return correct/float(len(testing_data))

    def prediction(self, sentence):
        tokens = self.get_tokens(sentence)
        totalpos = 0
        totalneg = 0
        for token in tokens:
            try:
                pos = self.pos_freq[token]
            except:
                pos = 0
            try:
                neg = self.neg_freq[token]
            except:
                neg = 0
            try:
                pos_prob_word = pos/float(pos+neg)
            except :
                pos_prob_word = 0
            try:
                neg_prob_word = neg/float(pos+neg)
            except:
                neg_prob_word = 0
            totalpos += pos_prob_word
            totalneg += neg_prob_word
        final_score = totalpos-totalneg
        return final_score
#         if final_score > 0 :
#             print "Positive Sentiment"
#         if final_score < 0 :
#             print "Negative Sentiment"
#         if final_score == 0:
#             print "Neutral"
                
    '''
    Input : Labelled File
    Process : Tokenize each sentence, compute probability for each token
    Output: Create multiple hashmaps 
    '''
    def train_corpus(self, filepath):
        training_data = [x.strip().split('\t') for x in open(filepath, 'r').readlines()]
        self.pos_freq = {}
        self.neg_freq = {}
        for i in range(len(training_data)):
            sentence = training_data[i][0]
            sentimentlabel = training_data[i][1]
            tokens = self.get_tokens(sentence)            
            for token in tokens:
                if sentimentlabel=="0":
                    try:
                        self.neg_freq[token] = self.neg_freq[token]+1
                    except:
                        self.neg_freq[token] = 1
                if sentimentlabel=="1":
                    try:
                        self.pos_freq[token] = self.pos_freq[token]+1
                    except:
                        self.pos_freq[token] = 1
    
    def get_tokens(self, sentence):
        test_sentence = sentence.lower()
        test_sentence_without_punctuation = ' '.join(word.strip(string.punctuation) for word in test_sentence.split())
        filtered_sentence = " ".join(word for word in test_sentence_without_punctuation.split() if word not in self.stopwords)
        return filtered_sentence.split(' ')
    
if __name__ == '__main__':
    scores = ScoreLearner()
    scores.train_corpus("../Extras/lokesh_train_1.txt")
    print scores.evaluate("../Extras/lokesh_test_1.txt")
#    scores.prediction("it's a very lovely morning today.")