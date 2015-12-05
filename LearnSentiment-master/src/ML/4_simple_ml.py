'''
Created on Nov 1, 2015

@author: Aditya
'''
import string
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

class MLSentiment():

    stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    def __init__(self):
        '''
        Constructor
        '''
          
    def train(self, trainfile):
        training_data = [x.strip().split('\t') for x in open(trainfile, 'r').readlines()]
        traindata = []
        labels = []
        for i in range(len(training_data)):
            this_sentence_counts = {}
            sentence = training_data[i][0]
            sentimentlabel = training_data[i][1]
            tokens = self.get_tokens(sentence)
            for token in tokens:
                try:
                    this_sentence_counts[token] = this_sentence_counts[token] + 1
                except:
                    this_sentence_counts[token] = 1
               
#             tmp2['label'] = sentimentlabel
            traindata.append(this_sentence_counts)
            labels.append(sentimentlabel)
        self.vec = DictVectorizer()
        X = self.vec.fit_transform(traindata)
#         for row in X.toarray():
#             print row
#         print 'Training'
        self.svm = SVC(C=0.1)
        self.svm.fit(X,labels)  
        print 'Done'
    
    def predict(self, sentence):
        tokens = self.get_tokens(sentence)
        thisdict = {}
        for token in tokens:
            try:
                thisdict[token] = thisdict[token] + 1
            except:
                thisdict[token] = 1
        
        data = self.vec.transform(thisdict)
        return self.svm.predict(data)
    
    def get_tokens(self, sentence):
        test_sentence = sentence.lower()
        test_sentence_without_punctuation = ' '.join(word.strip(string.punctuation) for word in test_sentence.split())
        filtered_sentence = " ".join(word for word in test_sentence_without_punctuation.split() if word not in self.stopwords)
        return filtered_sentence.split(' ')
    
if __name__ == '__main__':
    scores = MLSentiment()
    scores.train("../Extras/lokesh_train_1.txt")
    print scores.predict("2 . despite most reviewers giving kudos to the zen for music quality , i experienced a flaw using eax.")
    print scores.predict("i am really happy to see the big screen on this camera")
    print scores.predict("finally , i reiterate my thumbs-down rating for t-mobile as a carrier")
    print scores.predict("nokia makes a great phone , that 's clear.")
#     scores.test("../Extras/lokesh_test_1.txt")
#     scores.evaluate()
 #   scores.evaluate("../Extras/lokesh_test_1.txt")
#    scores.prediction("it's a very lovely morning today.")   