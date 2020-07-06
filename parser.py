from bs4 import BeautifulSoup
import requests

url = 'https://auto.ria.com/newauto/marka-skoda/'
Headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
marka = int(input('Вкажіть марку машини. 1. Skoda 2. Jeep ---->'))
li = int(input('Укажите страницу для парсинга. Всего есть 8 страниц укажите цифру от 1 к 8  --->'))
print('Вы указали страницу: ' + str(li) + ' Начинаю работу.' + '\n' + '\n')
if marka == 1:
	if li == 1:
		urls = 'https://auto.ria.com/newauto/marka-skoda/'
	elif li == 2:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=2&show_in_search=1&markaId=70'
	elif li == 3:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=3&show_in_search=1&markaId=70'
	elif li == 4:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=4&show_in_search=1&markaId=70'
	elif li == 5:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=5&show_in_search=1&markaId=70'
	elif li == 6:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=6&show_in_search=1&markaId=70'
	elif li == 7:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=7&show_in_search=1&markaId=70'
	elif li == 8:
		urls = 'https://auto.ria.com/newauto/marka-skoda/?page=8&show_in_search=1&markaId=70'
	def get_html(url):
		r = requests.get(urls, headers = Headers)
		return r
	def get_content(html):
		soup = BeautifulSoup(html, 'html.parser')
		items = soup.find_all('div', class_ = 'proposition_area')
		cars = []
		for item in items:
			cars.append({
				'Назва': item.find('div', class_ = 'proposition_title').find_next('strong').get_text(strip = True),
				'Ціна': item.find('span', class_ = 'grey size13').get_text(),
				'Місто': item.find('div', class_ = 'proposition_region grey size13').find_next('strong').get_text(),
				'Адрес для пошуку': HOST + item.find('div', class_ = 'proposition_title').find_next('a').get('href')
				})
		print(str(cars) + '\n' + '\n' + 'Работа завершена успешно.')
		return
	def parse():
		try:
			html = get_html(urls)
			get_content(html.text)
		except NameError:
			print('Ошибка. Данной страницы нету.' + '\n' + 'Вы указали неверную страницу.')
	parse()
elif marka == 2:
	if li == 1:
		urls = 'https://auto.ria.com/legkovie/jeep/'
	elif li == 2:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=2'
	elif li == 3:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=3'
	elif li == 4:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=4'
	elif li == 5:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=5'
	elif li == 6:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=6'
	elif li == 7:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=7'
	elif li == 8:
		urls = 'https://auto.ria.com/legkovie/jeep/?page=8'
	def get_html(url):
		r = requests.get(urls, headers = Headers)
		return r
	def get_content(html):
		soup = BeautifulSoup(html, 'html.parser')
		items = soup.find_all('div', class_ = 'content')
		cars = []
		for item in items:
			cars.append({
				'Назва': item.find('span', class_ = 'blue bold').get_text(strip = True),
				'Ціна': item.find('span', class_ = 'i-block').find_next('span').get_text() + ' грн',
				'Місто': item.find('li', class_ = 'item-char view-location').get_text(),
				'Адрес для пошуку': item.find('a', class_ = 'address').get('href')
				})
		print(str(cars) + '\n' + '\n' + 'Работа завершена успешно.')
		return
	def parse():
		try:
			html = get_html(urls)
			get_content(html.text)
		except NameError:
			print('Ошибка. Данной страницы нету.' + '\n' + 'Вы указали неверную страницу.')
	parse()
else:
	print('Указана неверная марка машины')

