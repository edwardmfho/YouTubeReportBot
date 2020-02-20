import time
import csv
import pandas as pd 

from selenium import webdriver

channels = [
    'https://www.youtube.com/channel/UC2UcOi6RPQG5J3DovCre1JA/videos',
    'https://www.youtube.com/channel/UCO4mttl54gQ0UW-DqyVrvLQ/videos',
    'https://www.youtube.com/channel/UCuNY7uTtTLTCS34YZHdefjA/videos',
    'https://www.youtube.com/channel/UCjQiROcVtb0ZqPpA-xE2flA/videos',
    'https://www.youtube.com/user/silentmajorityhk/videos',
    'https://www.youtube.com/user/albertip/videos',
    'https://www.youtube.com/channel/UCFEfp4o-Q46liveICbhyCHw/videos',
    'https://www.youtube.com/user/singtaotv/videos',
    'https://www.youtube.com/user/cuachiufai/videos',
    'https://www.youtube.com/channel/UCaSlyjhR4WC7QhYuaivxb6g/videos',
    'https://www.youtube.com/user/veronbenny/videos',
    'https://www.youtube.com/user/arsing1225/videos',
    'https://www.youtube.com/channel/UCp1Y_N-FSsuYJ9UUBO7vWGQ/videos',
    'https://www.youtube.com/channel/UCbSj5vM3ctjI7_OaKckMqDQ/videos',
    'https://www.youtube.com/user/leetszking/videos',
    'https://www.youtube.com/channel/UCIIwLX8REayuH-sNLf8c-3A/videos',
    'https://www.youtube.com/channel/UCIV3Card7sB1UHLLG8gWNUQ/videos',
    'https://www.youtube.com/user/jackyko1109/videos',
    'https://www.youtube.com/channel/UCkO4xzcz9g6XJbcqEzfOqjw/videos',
    'https://www.youtube.com/channel/UCFfLWSnUCblI4Lpsph7H1lA/videos',
    'https://www.youtube.com/channel/UChsweFvHEManjCQruTQZkVA/videos',
    'https://www.youtube.com/user/pennys627/videos',
    'https://www.youtube.com/channel/UCkpEyjUMcrGuJz4j2HB0VUA/videos',
    'https://www.youtube.com/channel/UCvlBe-TQfjLFINSSYQt9Tjg/videos',
    'https://www.youtube.com/channel/UCTm6y67OtLNpYONtVi0Y2nQ/videos'
    ]
urls = {}

class ReportBot():


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def retrieve_link(self):
        channelCount = 0
        totalVideo = 0
        for channel in channels:
            channelCount += 1
            self.driver.get(channel)
            videos = self.driver.find_elements_by_id('video-title')
            
            videoCount = 0 

            for video in videos:
                url = video.get_attribute("href")
                temp_video_name = video.text
                video_name = temp_video_name.encode('utf-8')
                urls[video_name] = url[32:]
                videoCount += 1
                print('Video Processed: {}'.format(videoCount))
                time.sleep(2)
                
                
            totalVideo += videoCount
            print('{} channel(s) processed\n {} videos processed.'.format(channelCount, videoCount))
        
        
        
        df = pd.DataFrame(urls.items())

        

        print('All video processed, total number of video = {}'.format(totalVideo))
        df = df.rename(columns = {"0" : "VideoTitle", "1": "videoId"})
        df.to_csv('output.csv', index=False)
        print('File compiled')

if __name__ == "__main__":
    bot = ReportBot()
    bot.retrieve_link()