# importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob


class Text():

	def get_sentiment_values_of_single_speech(self, text_converted):
		sentiment_sentence_list = []
		sentence_and_sentiment_list = []
		count = 0
		first_sentence = ''
		first_sentence_sentiment = 0
		for sentence in text_converted.sentences:
			sentence_and_sentiment = {}
			if count == 0:
				first_sentence = sentence
				first_sentence_sentiment = format(sentence.sentiment[0], '.3f')
			sentence_sentiment = sentence.sentiment[0]
			sentiment_sentence_list.append(sentence_sentiment)
			sentence_and_sentiment['sentence'] = str(sentence)
			sentence_and_sentiment['sentiment'] = format(sentence_sentiment, '.3f')
			sentence_and_sentiment_list.append(sentence_and_sentiment)
			count += 1
		return sentiment_sentence_list, first_sentence, first_sentence_sentiment, sentence_and_sentiment_list

	def get_sentiment_average_per_speech(self, sentiment_sentence_list):
		return format(sum(sentiment_sentence_list) / len(sentiment_sentence_list), '.3f')
	
	def get_data_for_sentiment_graph(self, text_converted):
			sentiment_graph_data = []
			columns = ['Sentence', 'Sentiment']
			sentiment_graph_data.append(columns)
			count = 0 
			for sentence in text_converted.sentences:
				rows = []
				sentence_sentiment = sentence.sentiment[0]
				sentence_number = count + 1
				rows.append(sentence_number)
				rows.append(float(format(sentence_sentiment, '.3f')))
				sentiment_graph_data.append(rows)
				count += 1
			return sentiment_graph_data
