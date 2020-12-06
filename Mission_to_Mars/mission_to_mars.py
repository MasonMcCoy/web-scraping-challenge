from bs4 import BeautifulSoup
from splinter import Browser

driver = 'C:\\Users\\Mason\\Desktop\\chromedriver'
executable_path = {'executable_path': driver}
browser = Browser('chrome', **executable_path, headless=False)
nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

browser.visit(nasa_url)
html = browser.html
nasa_soup = BeautifulSoup(html, 'html.parser')

content_list = nasa_soup.find_all('div', class_='content_title')
news_title = content_list[1]
print(news_title.string)

news_p = nasa_soup.find('div', class_='article_teaser_body').string
print(news_p)


jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)

img_button = browser.find_by_name('full_image')
img_button.click()

# featured_image_url =