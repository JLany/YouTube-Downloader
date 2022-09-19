from asyncio import streams
from turtle import down

from art import *

import os
import subprocess

from pytube import YouTube
from pytube import Playlist

import moviepy.editor as mp

###################################### 
### MAKE SURE YOU HAVE ALL THE NECESSARY LIBRARYS
### you can use in your cmd "pip install pytube/moviepy/turtle" and so on
### if you do not have pip, go to Google and search how to get that guy

VIDEO_SAVE_PATH = r"" # add FULL path here
AUDIO_SAVE_PATH = r"" # add FULL path here


def convert_to_audio():
    for filename in os.listdir(VIDEO_SAVE_PATH):
        try: ########### PLEASE DELETE OLD CONVERTED VIDEOS BEFORE ANY ATTEMPT TO RUN AGAIN! #############
            file = os.path.join(VIDEO_SAVE_PATH, filename)
            if os.path.isfile(file):
                clip = mp.VideoFileClip(file)
                clip.audio.write_audiofile(AUDIO_SAVE_PATH + '/' + filename + ".mp3")
            else:
                print('file was not found')
        except:
            print('error converting file')


# CURRENTLY, THIS FUNCTION DOWNLOADS VIDEOS AND THEN CONVERTS THEM TO AUDIO
# IF YOU WANT SOMETHING ELSE YOU CAN EASILY MODIFY
def download():

    links_file = open('links_file.txt', 'r')

    default_filename = []
    counter = 0

    for link in links_file:
        try:
            yt = YouTube(link)
        except:
            print('Connection Error')
        
        streams = yt.streams.filter(mime_type='video/mp4') 


        ## THERE IS A LONG STORY FOR THIS ONE, YOU CAN JUST IGONRE IT
        ## IF NOT INTERRESTED:
        ## filter(type"audio") works fine and gets only audio, (no visuals)
        ## but still it's mp4 what is being downloaded, and will 
        ## be open by your video media player, so you have the choice
        ## it is good to NOTE that the downloaded mp4 will have the size of an mp3
        ## SURE YOU CAN CONVERT THIS FILE TO AUDIO, BUT UNDEFINED BAHAVIOR AWAYTS
        ## YOU HAVE BEEN WARNED!
        # streams = yt.streams.filter(type="audio")

        # print(streams)            #DEBUG
        # print('________________') #DEBUG

        d_video = streams[0]
        try:
            d_video.download(VIDEO_SAVE_PATH)
        except:
            print('Error while saving')

        counter += 1
        default_filename.append(d_video.default_filename)  # get default name using pytube API
        
    convert_to_audio() # toggle this line for video download

    links_file.close()
    
    pass


# get urls of videos in a given playlist url
def get_playlists_urls(playlists):
    urls = []
    for playlist in playlists:
        playlists_urls = Playlist(playlist)

        for url in playlists_urls:
            urls.append(url)

    return urls


# if you do NOT need to download a playlist, simply fill the links file
# manually and run without using this function
def fill_urls_file():
    # put your urls here, can take more than one playlist url
    # DO NOT OMMIT THE QOUTES ;)
    playlists = ['']
    urls = get_playlists_urls(playlists)

    with open('links_file.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    pass


def main():
    # fill_urls_file()
    # download()
    # print('Task Completed')
    # open('links_file.txt', 'w').close() # make sure file is empty after process

    pass


main()
