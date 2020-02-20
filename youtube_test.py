# -*- coding: utf-8 -*-

# Based on the sample Python code for youtube.videos.reportAbuse
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import json
import random
import time

df = pd.read_csv('./data/videoid.csv')

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets_file.JSON"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    

    videoCount = 0 

    for videoId in df['1']:
        request = youtube.videos().reportAbuse(
            body={
            "reasonId": "S",
            "videoId": videoId
            
            }
        )
        request.execute()
        print('Reported Video ID: {}'.format(videoId))

        videoCount += 1
        if videoCount % 10 == 0:
            sleep(10)
        elif videoCount % 2 == 1:
            sleep(4)

if __name__ == "__main__":
    main()