from bs4 import BeautifulSoup as bs
# from selenium import webdriver
import requests
import os
# import time

url = 'https://www.9ku.com'

def convert(name):
    illegal = u'<>:"/\\|?*'
    for i in illegal:
        name = name.replace(i,'')
    return name.strip()

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
            title = None
            lyrics = None
            try:
                title = convert(song.select_one('font').string)
                lyrics = '\n'.join(get_lyrics(str(song.select_one('.chi')['href'])))
                songs.append({'title': title, 'lyrics': lyrics})
                print(title)
            except:
                continue

    # save lyrics
    path = os.path.join('singers', convert(name))
    try:
        if not os.path.isdir(path): os.mkdir(path)
    except:
        return
    for song in songs: 
        try:
            save_one(path, song)
        except:
            continue

count = get_count()
print(count)
urls_file = open('urls.txt', 'r', encoding='utf8')
index = -1
line = True
while line:
    index+=1
    line = urls_file.readline()
    if index <= count: continue
    namelink = line.split('#')
    print(namelink, 'started!')
    if len(namelink)!=2: continue
    save_songs(namelink[0], namelink[1])
    save_count(index)
    print(namelink, 'finished!')
urls_file.close()