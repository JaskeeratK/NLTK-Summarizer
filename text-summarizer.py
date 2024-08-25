import nltk
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

def summarizer(text):
    StopWords=set(stopwords.words("english"))
    word_freq={}
    for word in nltk.word_tokenize(text):
        if word not in StopWords:
            if word not in word_freq.keys():
                word_freq[word]=1
            else:
                word_freq[word]+=1
    max_freq_word=max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq_word
    
    sent_list=nltk.sent_tokenize(text)
    sent_score={}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if len(sent.split(' '))<30:
                    if sent not in sent_score.keys():
                        sent_score[sent]=word_freq[word]
                    else:
                        sent_score[sent]+=word_freq[word]
    summary_sentences = heapq.nlargest(7, sent_score, key=sent_score.get)

    summary=' '.join(summary_sentences)
    print(summary)

x=input("Enter the text you'd like to summarize:\n")
print("\n Here's the summarized text:\n")
summarizer(x)