import nltk
import pandas as pd
import time
import numpy as np
import requests
import praw
import json
import betamax
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

r = praw.Reddit(client_id='LjCRxQdehx5D0A',
                     client_secret='9FH2qph5PVsCMiG3-9sDZ_v2Ym8',
                     password='MadHacks2018',
                     user_agent='testscript by /u/Playtester0912',
                     username='Playtester0912')


# You can combine subreddits too with a + between them

for submission in r.subreddit('finance').top(limit=10):
    average=0
    ct =0 
#     post_corpus = ''
    print("POST TITLE: " + submission.title)
    print("Comments Analyzed: "+str(submission.num_comments))
    submission.comments.replace_more(limit=None)
    for i in submission.comments.list()[1:]:
        ct +=1
        snt = analyser.polarity_scores(i.body)
        average+=snt["compound"]
#         if(snt['compound'] <= -0.9):
#             print("NEGATIVE SENTIMENT COMMENT: " + i.body)
#             print()
#         print(type(snt['compound']))
#         print(snt)
    print("FINAL SCORING FOR THE POST: " + str(average/ct))
    print()

