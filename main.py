import requests
import re
import os


def convertaudio(link, name):
    # convert audio m3u8 to mp3 with ffmpeg
    
    os.system(f'ffmpeg -http_persistent false -i {link} -vcodec copy -c copy {name}.mp3')
    # ADD .exe TO "ffmpeg" IN COMMAND IF U USE WINDOWS


def getlink(url):
    # get location of m3u8 file
    
    parse = re.findall('[-0-9]+|[0-9]+', url)

    url = requests.get("https://api.vk.com/method/audio.getById", params={
        'access_token': 'token',
        'v': '5.131',
        'audios': f'{parse[0]}_{parse[1]}'
    }).json()['response'][0]['url']

    return url

link = getlink("https://vk.com/audio474499284_456546163_c6dd1155f75286e225")
convertaudio(link)
