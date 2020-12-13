from bs4 import BeautifulSoup
from splinter import Browser
import pandas

def init_browser():
    driver = 'C:\\Users\\Mason\\Desktop\\chromedriver'
    executable_path = {'executable_path': driver}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    mars_dict = {}
    # SCRAPES FEATURED NEWS STORY #
    
    browser = init_browser()
    
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    
    
    browser.visit(nasa_url)
    html = browser.html
    nasa_soup = BeautifulSoup(html, 'html.parser')
    
    content_list = nasa_soup.find_all('div', class_='content_title')
    news_title = content_list[1]
    
    p = nasa_soup.find('div', class_='article_teaser_body')
    news_p = p.get_text()
    
    browser.quit()
    
    # SCRAPES FEATURED IMAGE #
    
    browser = init_browser()
    
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    
    browser.visit(jpl_url)
    
    img_button = browser.find_by_css('a[class="button fancybox"]')
    img_button.click()
    
    info_button = browser.find_by_css('div[class="buttons"] a[class="button"]')
    info_button.click()
    
    detail_button = browser.find_by_id('image_detail')
    detail_button.click() 
    
    featured_image_url = browser.url
    
    browser.quit()
    
    # SCRAPES MARS FACTS TABLE INTO HTML TABLE #
    
    mars_facts_url = 'https://space-facts.com/mars/'
    
    facts_tables = pandas.read_html(mars_facts_url)
    facts_table = facts_tables[2]
    facts_table.columns = ['', 'Mars']
    facts_table.set_index
    html_table = facts_table.to_html(index=False)
    html_table.replace('\n', '')
    
    # SCRAPES HEMISPHERE TITLES AND IMAGE HREFS INTO DICTIONARY #
    
    browser = init_browser()
    
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    usgs_url = 'https://astrogeology.usgs.gov/'
    
    browser.visit(mars_url)
    hemi_html = browser.html
    
    hemi_soup = BeautifulSoup(hemi_html, 'html.parser')
    
    all_hemis = hemi_soup.find('div', class_='collapsible results')
    indv_hemis = all_hemis.find_all('div', class_='item')
    
    hemisphere_image_urls = []
    
    for hemi_item in indv_hemis:
        hemi = hemi_item.find('div', class_="description")
        hemi_title = hemi.h3.text
        title = hemi_title.replace(' Enhanced', '')
        
        hemi_link = hemi.a["href"]    
        
        browser.visit(usgs_url + hemi_link)
        img_html = browser.html
        
        img_soup = BeautifulSoup(img_html, 'html.parser')
        
        img_link = img_soup.find('div', class_='downloads')
        img_url = img_link.find('li').a['href']
    
        img_dict = {}
        img_dict['title'] = title
        img_dict['img_url'] = img_url
        
        hemisphere_image_urls.append(img_dict)
        
    browser.quit()

    mars_dict = {
        "title": news_title.text,
        "text": news_p,
        "image": featured_image_url,
        "table": str(html_table),
        "hemispheres": hemisphere_image_urls
    }
    
    return mars_dict