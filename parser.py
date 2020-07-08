from bs4 import BeautifulSoup
import requests

url = 'https://auto.ria.com/newauto/marka-skoda/'
Headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
marka = int(input('Вкажіть марку машини. 1. Skoda 2. Jeep 3. BMW  ---->'))
if marka == 1:
	li = int(input('Укажите страницу для парсинга. Всего есть 11 страниц. Укажите цифру от 1 к 11  --->'))
	print('Вы указали страницу: ' + str(li) + ' Начинаю работу.' + '\n' + '\n')
	urls = 'https://auto.ria.com/newauto/marka-skoda/?page=' + str(li) + '&show_in_search=1&markaId=70'
	if li == 1:
		urls = 'https://auto.ria.com/newauto/marka-skoda/'
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
		if cars == []:
			print('Ошибка. Данной страницы нету.\nВы указали неверный номер страницы')
		else:
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
	li = int(input('Укажите страницу для парсинга. Всего есть 107 страниц. Укажите цифру от 1 к 107  --->'))
	print('Вы указали страницу: ' + str(li) + ' Начинаю работу.' + '\n' + '\n')
	urls = 'https://auto.ria.com/legkovie/jeep/?page=' + str(li)
	if li == 1:
		urls = 'https://auto.ria.com/legkovie/jeep/'
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
		if cars == []:
			print('Ошибка. Данной страницы нету.\nВы указали неверный номер страницы')
		else:
			print(str(cars) + '\n' + '\n' + 'Работа завершена успешно.')
			return
	def parse():
		try:
			html = get_html(urls)
			get_content(html.text)
		except NameError:
			print('Ошибка. Данной страницы нету.' + '\n' + 'Вы указали неверную страницу.')
	parse()
elif marka == 3:
	li = int(input('Укажите страницу для парсинга. Всего есть 12 страниц. Укажите цифру от 1 к 12  --->'))
	print('Вы указали страницу: ' + str(li) + ' Начинаю работу.' + '\n' + '\n')
	urls = 'https://auto.ria.com/newauto/marka-bmw/?page=' + str(li) + '&show_in_search=1&markaId=9'
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
		if cars == []:
			print('Ошибка. Данной страницы нету.\nВы указали неверный номер страницы')
		else:
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

