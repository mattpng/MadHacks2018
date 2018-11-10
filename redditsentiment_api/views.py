from django.shortcuts import render
import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

import praw

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

@api_view(['GET'])
def get_user_comment_sentiment(request):
    """
    Get user's comments

    @param request The REST request to the endpoint

    """
    analyzer = SentimentIntensityAnalyzer()

    r = praw.Reddit(client_id='LjCRxQdehx5D0A',
                    client_secret='9FH2qph5PVsCMiG3-9sDZ_v2Ym8',
                    password='MadHacks2018',
                    user_agent='testscript by /u/Playtester0912',
                    username='Playtester0912')

    user = r.redditor(name='--orb')



    for commentId in user.comments.new():
        temp_comment = r.comment(id=commentId)
        test = analyzer.polarity_scores(temp_comment.body)
        print(test)

    r = {
        'result': 'true'
    }

    return JsonResponse(r)
