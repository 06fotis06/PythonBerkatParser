import requests
from bs4 import BeautifulSoup as bs
import urllib.parse
import time
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Введи то, что нужно найти, пробел, количество страниц.\n Пример: iphone 14 pro max 3")




@dp.message_handler()
async def echo(message: types.Message):
    a = message.text.split()
    g = m(' '.join(a[:-1]),int(a[-1]))
    for i in range(len(g[0])):
    	await message.answer(f'{g[0][i]}\n{g[1][i]}\n{g[2][i]}')
    	
    
	   
	   
def search(i, name):
    h = []
    p = []
    u = []
    
    base_url = "https://berkat.ru/search/board"
    query = name
    encoded_query = urllib.parse.quote(query, safe='')
    url = f"{base_url}?q={encoded_query}&page={i}"
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h3', class_='board_list_item_title')
    m = 0
    for name in vacancies_names:
    	v_n = soup.find_all('p', class_='board_list_item_text')
    	n = v_n[m]
    	h.append(name.a.string)
    	p.append(n.string)
    	u.append('https://berkat.ru'+ name.a['href'])
    	m += 1
    	print([h, p, u])
    return [h, p, u]

def m(name,c):
	h1 = []
	p1 = []
	u1 = []
	for i in range(1,c+1):
		s = search(i,name)
		h1 += s[0]
		p1 += s[1]
		u1 += s[2]
	return [h1,p1,u1]
	
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
		
