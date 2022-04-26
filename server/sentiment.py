# importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob


class Text():

    def get_discussion_sentiment(self, post_data):
        sentiment_object = Text()
        discussion_text_ready_for_analysis = TextBlob(post_data['post'])
        sentence_sentiment_list = []
        for sentence in discussion_text_ready_for_analysis.sentences:
            sentence_sentiment = sentence.sentiment[0]
            sentence_sentiment_list.append(sentence_sentiment)
        sentiment_average = sentiment_object.get_average(sentence_sentiment_list)
        return sentiment_average
    
    def get_average(self, sentence_sentiment_list):
        return sum(sentence_sentiment_list) / len(sentence_sentiment_list)


# Three speeches file:
# https://github.com/ravenusmc/three_speeches/blob/master/server/sentiment.py
