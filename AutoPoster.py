import facebook
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def fun():
	graph = facebook.GraphAPI(access_token='EAAD2He03WHsBAOhIP3iiXkimCjSxLa5rGubZCBmCUNPx7lhNznDyGSQSJLJpyxj162HH1FThhI4iVTS6ZBCZCLtAbkUXpP0oDEIwPr2x44D8ViDe2Kas783dF0gOu8jVPFF81fusZAXeZAFoZAHMsnzZBnwEANHq38UyGIKZCgIljb6CXXmlXm2d', version="2.7")
	while True:
		try:
			f=open("memory.txt","r")
			data=f.readlines()
			f.close()
		except:
			f=open("memory.txt","w")
			f.close()
			f=open("memory.txt","r")
			data=f.readlines()
			f.close()

		f=open("memory.txt","a")
		news_url="https://news.google.com/news/rss"
		Client=urlopen(news_url)
		xml_page=Client.read()
		Client.close()
		soup_page=soup(xml_page,"xml")
		news_list=soup_page.findAll("item")
		for news in news_list:
			flag=True
			for x in data:
				x=x.rstrip("\n")
				if str(x)==str(news.title.text):
					flag=False

			if flag==True:
				print(news.title.text)
				f.write(news.title.text)
				f.write("\n")
				titles=news.title.text
				titles=titles.split("-")
				titles=titles[1]
				attachment =  {
				   
				        'link': f'{news.link.text}',
				    }

				graph.put_wall_post(message=f"""\"{str(titles)} \" \n {news.link.text}""", attachment=attachment, profile_id='424511987973777')
				time.sleep(3)


import time
import sys
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    fun()


fun()
while True:
	countdown(600)








