#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests,webbrowser
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# scraping the website
google_search = requests.get("https://www.imdb.com/list/ls068010962/")
soup=BeautifulSoup(google_search.text, 'html.parser')

#image links
images = soup.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')

#Extracting important information from webpage    
import numpy as np
import urllib
import cv2

images = soup.find_all('img', {'src':re.compile('.jpg')})
sno=[]
Actor=[]
Movie=[]
Img=[]
About=[]
Image=[]
soup=BeautifulSoup(google_search.text, 'html.parser')
for link in soup.find_all('div',class_="lister-item mode-detail"):
    Sno=link.h3.span.text
    sno.append(Sno)
    actorname=link.h3.a.text
    Actor.append(actorname)
    movie=link.p.a.text
    Movie.append(movie)
    img=link.div.a.img['src']
    Img.append(img)
    about=link.find("p").findNext("p").get_text()
    About.append(about)
    

#converting to dataframe
import pandas as pd
test_df = pd.DataFrame({'Sno': sno,'Actor': Actor,'Movie': Movie,'Link': Img, 'About':About})
print(test_df.info())
test_df


#Save into excel file
test_df.to_excel("output.xlsx",

             sheet_name='Sheet_name_1')
#to extract images from webpage and show in new tab
import numpy as np
import urllib.request
import cv2
from bs4 import BeautifulSoup
import requests
import ssl


Image=[]
images=[]

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image
for url in Img:
    print("downloading %s" % (url))
    image = url_to_image(url)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    Image.append(image)
#for downloading images and saving in a seperate folder    
soup=BeautifulSoup(google_search.text, 'html.parser')
Img=[]
for link in soup.find_all('div',class_="lister-item mode-detail"):
    img=link.div.a.img['src']
    Img.append(img)

test_dff = pd.DataFrame({'Links': Img})
test_dff.to_csv('mycsv.csv')


#function to download image
def url_to_jpg(i,url,file_path):
    filename='image-{}.jpg'.format(i)
    full_path='{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)
    
    print('{} saved.'.format(filename))
    return None
FILENAME='mycsv.csv'
FILE_PATH='images/'
urls = pd.read_csv(FILENAME)
for i,url in enumerate(urls.values):
    url_to_jpg(i,url[1],FILE_PATH)
    

