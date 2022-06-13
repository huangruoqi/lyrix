from bs4 import BeautifulSoup as bs
# from selenium import webdriver
import requests
import os
# import time

url = 'https://www.9ku.com'

urls_file = open('urls.txt', 'r', encoding='utf8')

def save_count(count):
    f = open('count.txt', 'w')
    f.write(str(count))
    f.close()

def get_count():
    f = open('count.txt')
    r = int(f.read().strip())
    f.close()
    return r

def get_lyrics(link):
    req = requests.get(url+link)
    soup = bs(req.text, 'html.parser')
    content = soup.select_one('#lrcgc')
    return list(content.stripped_strings)[1:]

def save_one(path, song):
    f = open(os.path.join(path, song['title']+'.lrc'), 'w', encoding='utf8')
    f.write(song['lyrics'])
    f.close()

def save_songs(name, link):
    req = requests.get(url+link)
    soup = bs(req.text, 'html.parser')
    songs = []
    
    for block in soup.select('.singerMusic ol'):
        if block['id']=='fg': continue
        for song in block.select('li'):
            title = song.select_one('font').string
            lyrics = '\n'.join(get_lyrics(str(song.select_one('.chi')['href'])))
            songs.append({'title': title, 'lyrics': lyrics})

    # save lyrics
    path = os.path.join('singers', name)
    if not os.path.isdir(path): os.mkdir(path)
    for song in songs: save_one(path, song)

count = get_count()

urls_file = open('urls.txt', 'r', encoding='utf8')
index = 0
a = urls_file.readline().split('#')
save_songs(a[0],a[1])
# for line in urls_file:
#     if index <= count: continue
#     namelink = line.split('#')
#     if len(namelink)!=2: continue
#     save_titles(namelink[0], namelink[1])
#     save_count(index)
#     index+=1
urls_file.close()