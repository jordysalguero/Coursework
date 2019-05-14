#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd


# ## Mars News

# In[2]:


def init_browser():
    executable_path = {"executable_path": "C:/Users/jordy/Documents/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)
    


# In[3]:


mars_info = {}


# In[6]:


def mars_news ():
    #Initialize Browser
    browser = init_browser()
    
    #visit the Mars news website
    mars_news_url = "https://mars.nasa.gov/news/"

    browser.visit(mars_news_url)

    time.sleep(1)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get title and paragraph
    news_title = soup.find('div', class_="content_title").find_all('a')[0].text
    news_paragraph = soup.find('div', class_="article_teaser_body").text
    
    #Dictionary entry for mars news
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_paragraph
    
    return mars_info

    #Quite browser
    browser.quit()


# ## Mars Space Image

# In[7]:


def mars_image():
    
    #Initialize Browser
    browser = init_browser()
    
    mars_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_image_url)

    # HTML Object
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_image, 'html.parser')

    # Retrieve background-image url from style tag
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + featured_image_url

    # Display full link to featured image
    featured_image_url
    
    #Dictionary entry for mars image
    mars_info['featured_image_url'] = featured_image_url
    
    return mars_info

    #Quit Browser
    browser.quit()


# ## Mars Twitter

# In[8]:


def mars_twitter():
    
    #Initialize Browser
    browser = init_browser()

    #visit the Mars Weather Twitter Account
    mars_twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter_url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Retrieve Weather information
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    #Dictionary entry for mars image
    mars_info["mars_weather"] = mars_weather
    
    return mars_info

    browser.quit()


# ## Mars Facts Webpage

# In[12]:


def mars_facts():
    
    #visit the Mars Facts webpage and scrape using Pandas
    mars_facts_url = "https://space-facts.com/mars/"

    #read the url with pandas
    mars_facts = pd.read_html(mars_facts_url)

    #Read table in html
    mars_facts_df = mars_facts[0]

    mars_facts_df.columns = ["Description", "Value"]

    mars_facts_df.set_index("Description", inplace = True)

    data = mars_facts_df.to_html()
    
    #Dictionary entry for mars facts
    mars_info["mars_facts_df"] = data
    
    return mars_info


# ## USGS Astrogeology

# In[13]:


def mars_hemispheres():

    # Initialize Browser
    browser = init_browser()

    # Visit website using splinter
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    html= browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Gather information
    items = soup.find_all('div', class_="item")

    hemi_url = []

    # Main URL
    hemisphere_url_main = "https://astrogeology.usgs.gov"

    # Loop items
    for i in items:
        # Title
        title = i.find('h3').text

        #link for image website
        img_url = i.find('a', class_='itemLink product-item')['href']

        # Visit each img link
        browser.visit(hemisphere_url_main + img_url)

        img_url_html = browser.html

        #Parse through the items
        soup = bs(img_url_html, "html.parser")

        #get img source
        final_img_url = hemisphere_url_main + soup.find('img', class_ = "wide-image")['src']

        # Append the information 
        hemi_url.append({"title": title, "img_url": final_img_url})

    mars_info['hemi_url'] = hemi_url

    return mars_info