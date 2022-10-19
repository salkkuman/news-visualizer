from google.colab import drive
drive.mount('/content/gdrive')

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

import requests
from bs4 import BeautifulSoup
url = "https://www.investing.com/news/stock-market-news"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html')
elements = soup.find_all("a", class_="title", title=True)
for EachPart in elements:
    print(EachPart.get_text())
L_titles = []
for EachPart in elements:
    L_titles.append(EachPart.get_text())
L_titles = list(set(L_titles))
print(L_titles)
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('english'))

all_titles = ""
for title in L_titles:
    title_to_add = ' '.join([word for word in title.split() if word not in stopwords.words("english")])
    all_titles += " " + title_to_add
    
print(all_titles)

import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=800, height=400).generate(all_titles)

plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('market_news.png')
plt.show()