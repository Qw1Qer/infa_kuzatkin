import os
import webbrowser
import sys
import subprocess

import pyttsx3

try:
	import requests		
except:
	pass

engine = pyttsx3.init()
engine.setProperty('rate',180)


def speaker(text):
	engine.say(text)
	engine.runAndWait()
def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://dzen.ru/', new=2)

def schedule():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.asu.ru/timetable/students/', new=2)

def film():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://vkvideo.ru/video-222609266_456240362', new=2)

def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen('C:\Program Files (x86)\Hearthstone\Hearthstone.exe')
	except:
		speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
	
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass