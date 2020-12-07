# THIS SCRIPT DOES NOT RUN #

from bs4 import BeautifulSoup
from splinter import Browser

driver = 'C:\\Users\\Mason\\Desktop\\chromedriver'
executable_path = {'executable_path': driver}
browser = Browser('chrome', **executable_path, headless=False)
nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


browser.visit(nasa_url)
html = browser.html
nasa_soup = BeautifulSoup(html, 'html.parser')

content_list = nasa_soup.find_all('div', class_='content_title')
news_title = content_list[1]
print(news_title.string)

news_p = nasa_soup.find('div', class_='article_teaser_body').string
print(news_p)

browser.quit()


# THESE WORK INDIVIDUALLY #

from splinter import Browser

driver = 'C:\\Users\\Mason\\Desktop\\chromedriver'
executable_path = {'executable_path': driver}
browser = Browser('chrome', **executable_path, headless=False)

jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

browser.visit(jpl_url)

img_button = browser.find_by_css('a[class="button fancybox"]')
img_button.click()

info_button = browser.find_by_css('div[class="buttons"] a[class="button"]')
info_button.click()

detail_button = browser.find_by_id('image_detail')
detail_button.click() 

featured_image_url = browser.url
print(featured_image_url)

browser.quit()

# THESE WORK INDIVIDUALLY #

import pandas

mars_facts_url = 'https://space-facts.com/mars/'

facts_table = pandas.read_html(mars_facts_url)
print(facts_table[0]) #THIS MAY NOT BE IN THE CORRECT FORMAT!!!

# THIS DOES NOT WORK QUITE YET #

from splinter import Browser

driver = 'C:\\Users\\Mason\\Desktop\\chromedriver'
executable_path = {'executable_path': driver}
browser = Browser('chrome', **executable_path, headless=False)

usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(usgs_url)

hemisphere_image_urls = []
hemispheres = []

hemi_buttons = browser.find_by_css('img[class="thumb"]')


'''
for hemi in hemi_buttons:
    browser.visit(usgs_url)
    hemi.click()
    browser.find_by_text('Sample').click()
    img_url = browser.url
    browser.quit()
'''
    
# THIS GETS HEMISPHERE NAMES #
hemi_buttons = browser.find_by_tag('h3') # img[class="thumb"]


for hemi in hemi_buttons:
    hemi = hemi.text
    hemi = hemi.replace(' Hemisphere Enhanced', '')
    hemispheres.append(hemi)

print(hemispheres)