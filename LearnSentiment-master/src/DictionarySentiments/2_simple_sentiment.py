import string


class SimpleSentiments():
    stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    def __init__(self):
        self.lexicon_lines = None
    
    def read_dictionary(self,filepath):
        with open(filepath, "rb") as f:
            lines = f.readlines()
        self.lexicon_lines = []
        for line in lines:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            self.lexicon_lines.append(parts)
            
    def crunch_scores(self):
        tempscores = {}
        self.scores = {}        
        for sentence in self.lexicon_lines:
            try:
                pos_score = sentence[2].strip()
                neg_score = sentence[3].strip()
                words = [x.split("#")[0] for x in sentence[4].strip().split(" ")]
                for word in words:
                    try:
                        tempscores[word].append(float(pos_score))
                        tempscores[word].append(-float(neg_score))
                    except:
                        tempscores[word]=[]
                        tempscores[word].append(float(pos_score))
                        tempscores[word].append(-float(neg_score))
            except:
                pass
                    
        for word in tempscores.keys():
            # print word, sum(scores[word])/len(scores[word])
            self.scores[word] = sum(tempscores[word])/len(tempscores[word])
            
    def get_sentiment(self, sentence):
  #      test_word_score = []
        sum = 0
        test_sentence = sentence.lower()
        test_sentence_without_punctuation = ' '.join(word.strip(string.punctuation) for word in test_sentence.split())
        
        sentence = " ".join(word for word in test_sentence_without_punctuation.split() if word not in self.stopwords)
        
        for word in sentence.split(' '):
            try:
                test_score = self.scores[word]
                sum+=test_score
            except:
                pass
        sum = 1 if sum>1 else sum
        sum = -1 if sum<-1 else sum
        return sum
        
if __name__ == '__main__':
    print "Loading Lexicon"

    simple = SimpleSentiments()
    simple.read_dictionary("C:\\Users\\admin\\Desktop\\senti.txt")
    simple.crunch_scores()
    print simple.get_sentiment("This is so good good good good awesome. My name is Lokesh")
    print simple.get_sentiment("I hate all those 100's of crazy lines you write in Java.")
