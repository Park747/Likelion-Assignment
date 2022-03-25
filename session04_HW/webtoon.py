import requests
from bs4 import BeautifulSoup

Webtoon_URL = f'https://comic.naver.com/webtoon/weekdayList?week=thu'
webtoon_html = requests.get(Webtoon_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

webtoon_img_list = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_img_list.find_all("li")

def extract_info(webtoon_list):
    result = []
    
    for webtoon in webtoon_list:
        title = webtoon.find("dl").find("a").string
        author = webtoon.find("dd",{"class":"desc"}).find("a").string
        rating = webtoon.find("div",{"class":"rating_type"}).find("strong").string
        webtoon_info = {
            'title' : title,
            'author' : author,
            'rating' : rating
        }
        result.append(webtoon_info)
    return result





# title = webtoon_list[0].find("dl").find("a").string
# author = webtoon_list[0].find("dd",{"class":"desc"}).find("a").string
# rating = webtoon_list[0].find("div",{"class":"rating_type"}).find("strong").string



# result = {
#     'title': title,
#     'author': author,
#     'rating' : rating
# }

# print(result)