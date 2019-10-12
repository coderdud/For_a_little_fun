import wikipedia as wiki
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

def compare_countries(country_1='United States',country_2='Japan'):
    
    '''get the data from internet and show them on screen!!'''
    # the intial url for the information source
    url = 'https://www.worldometers.info/'
    
    
    # read the first table as datafram
    df = pd.read_html(url+ 'world-population/population-by-country/')
    df = df[0]
    # change the country column to be same in all tables
    df = df.rename(columns={'Country (or dependency)': 'Country'})
    # remove unuseful column
    df = df.drop('#',1)
    # set the key as country name
    df = df.set_index('Country')
    
    
    # read the second table as datafram
    df1 = pd.read_html(url+'gdp/gdp-by-country/')
    df1 = df1[0]
    # remove unuseful column
    df1 = df1.drop('#',1)
    # set the key as country name
    df1 = df1.set_index('Country')
    
    # join two tables
    df_all = df.join(df1,on='Country')
    
    # select the countries to be compared
    new_df = df_all.loc[[country_1, country_2],['Population (2019)','GDP per capita']]
    
    # make background image for visializing result
    img = Image.new('RGB', (300, 80), color = (0, 0, 0))
    
    # draw the results on background image
    d = ImageDraw.Draw(img)
    d.text((10,10), str(new_df), fill=(255,255,0))
    img = img.resize((1290,720))
#     plt.imshow(img)
#     plt.show
    return img
