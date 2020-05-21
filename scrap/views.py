from django.shortcuts import render
from django.http import JsonResponse
import requests 
import bs4


class NagarikNews:
	def __init__(self):
		self.title_list = []

	def local_news(self):
		URL = 'https://myrepublica.nagariknetwork.com/'
		
		try:
			response = requests.get(URL)
		except:
			print ('Cannot retrive info from myrepublica')

		parsed_response = bs4.BeautifulSoup(response.text,'html.parser')

		titles = parsed_response.find_all('h2')

		for title in titles[2:5]:
			self.title_list.append(title.text)

		return self.title_list

	def political_news(self):
		URL = 'https://myrepublica.nagariknetwork.com/category/politics'

		try:
			response = requests.get(URL)
		except:
			print ('Cannot retrive info from myrepublica')

		parsed_response = bs4.BeautifulSoup(response.text,'html.parser')

		titles = parsed_response.find_all('h2')

		for title in titles[2:-2]:
			self.title_list.append(title.text)

		return self.title_list

def data(request):

    if request.is_ajax():
        print("in")
        abc=NagarikNews().political_news()
        data1={
            'data':abc
        }

        return JsonResponse(data1)
    else:
        return render(request,"data.html")