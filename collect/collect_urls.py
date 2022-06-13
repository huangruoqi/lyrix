from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

url = 'https://www.9ku.com/geshou/gangtaizuhe-all-all.htm'
driver = webdriver.Chrome('C:/tools/python_tools/chromedriver.exe')
driver.get(url)

while 1:
    try:
        loadmore = driver.find_element_by_css_selector('a.loadMoreBtn')
        loadmore.click()
        print('clicked')
    except Exception as e:
        print(e)
        break
    time.sleep(1)

soup = bs(driver.page_source, 'html.parser')
singers = soup.select('#body')[0].select('li a.t-t')
name_link_list = [(singer.string, singer['href']) for singer in singers]
print("Number of singers found:",len(name_link_list))

previous_singers = set()
prev_file = open('urls.txt', 'r', encoding='utf8')
for line in prev_file:
    temp = line.split('#')
    if (len(temp)==2):
        previous_singers.add(temp[0])
prev_file.close()

table = {}
curr_file = open('urls.txt', 'a', encoding='utf8')
for name, link in name_link_list:
    if name not in previous_singers and table.get(name) == None:
        table[name] = link

for name in table:
    curr_file.write(f'{name}#{table[name]}\n')
curr_file.close()