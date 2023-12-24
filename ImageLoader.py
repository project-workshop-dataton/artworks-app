import urllib.request
import urllib
import re
import imghdr
from io import BytesIO
from PIL import Image, ImageOps, ImageFont
from urllib.parse import quote
from pyppeteer import launch
import bs4
import shutil
from requests_html import AsyncHTMLSession
from PIL import ImageDraw
import requests
import asyncio
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor
work_path = "./static/images/"
def photoshop(file,id):
    img = Image.open(BytesIO(file))
    rgba = img.convert("RGBA")
    resize = ImageOps.pad(rgba, (300,200), color=(255, 255, 255, 0))
    #border = (0, 0, 0, 0)
    #final = ImageOps.expand(resize, border=border, fill='black') #задел на дополнение картинки, вместо обрезки
    resize.save(work_path+id+'.png',"PNG")
def save_image(link,id):
    #real_link = link.split(sep = "/")[-1]
    sha = re.search(r'(?<=sha=)\w+', link).group(0)
    link = re.search(r'^[^?]*', link).group(0)

    cookies = {
       'viewedCookieBanner': 'true',
       'sessionHighlightColor': '1',
       '_gorilla_csrf': 'MTcwMjk2NzQ3OXxJak5xZGxOMFYwMWFWMGN6WkVOSlpXeG1Wbk01TDJSeWIwUTRVMmhQSzNWWVQzRnlhSFZHVVRWc1YwMDlJZ289fG82bzLPqsXNSkgyo2B4Ua0pFjpQRED67R5FKTcrsdFE',
       '__cf_bm': 'yqWsQz1W8Nm.79sjixTGblHSNK6uirJC5e1VLVBQ6cU-1702996359-1-AWOMwCSgAamLYKmQ2mjYOgiruAiz/p18KujyGc+BjrsP4cUnvJ3ZSIu5fVYr79dDTVgws0jD4ePjzRvy71WNnXU=',
       'cf_clearance': 'QY8VA2sUNbBNK5F7rwcg8y7nwH4fTKymQ1odGGxxZtw-1702996360-0-1-5b856018.839d23d.60cf2c48-0.2.1702996360',
       'global': 'MTcwMjk5NjM3NHxOd3dBTkZCVU5reERVa05WVkVzMVFWWlRTVlpPUkV4S1ZFRTNWMFpWV0VKTVRWZE9OVEpGVlV0VFRGSkJXazVFVVZBMlQwWkRRVUU9fFzLITm5BB5KqEN24oXdsOG-rRvZXQMp5p7imm-O-adC',
    }
    headers = {
       'authority': 'www.moma.org',
       'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
       'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
       'referer': 'https://www.moma.org/collection/works/{}'.format(id),
       'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^118^\\^, ^\\^Opera',
       'sec-ch-ua-mobile': '?1',
       'sec-ch-ua-platform': '^\\^Android^\\^',
       'sec-fetch-dest': 'image',
       'sec-fetch-mode': 'no-cors',
       'sec-fetch-site': 'same-origin',
       'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    }

    params = (
       ('sha', sha),
    )
    r = requests.get('https://www.moma.org'+link,headers=headers, params=params, cookies=cookies)
    return r.content
    # print(response)
    # response = requests.get('https://www.moma.org/media/W1siZiIsIjE3MzI1MiJdLFsicCIsImNvbnZlcnQiLCItcXVhbGl0eSA5MCAtcmVzaXplIDIwMDB4MTUwMFx1MDAzZSJdXQ.jpg?sha=262a395eaca90eb0', headers=headers, cookies=cookies)
    # scraper = cloudscraper.create_scraper()
    # response = scraper.get("http://www.moma.org/"+str(id)).text
    # print(response)
    #s = HTMLSession()
    #s.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    # r = s.get("http://www.moma.org/"+str(id))
    # r.html.render(timeout=8000)
    # print(r.status_code)
    # print(r.content)
    # site = urllib.request.urlopen("http://www.moma.org/"+str(id))
    # soup = BeautifulSoup(site)
    # print(soup)
    # bild = soup.select('section div img')
    ## ev insert loop for cases where there are several images
    # b = bild[0]
    # if 'srcset' in b.attrs:
    #    prts = b['srcset'].split(', ')
    #    # prts[-1]
    #    pth = prts[-1].split(' ')[0]
    #    pic = io.imread('http://www.moma.org/' + pth)
    #    io.imsave(self.work_path+str(id) + '.png', pic)
    # else:
    #
    #    print("Нет картинки")
    # soup = BeautifulSoup(html, "lxml")  # give the html to soup
    # imgs = soup.findAll("a", {"class": "envira-gallery-link"})
    # for img in imgs:
    #    imgUrl = img['href']
    #    cmd = ['wget', imgUrl]
    #    subprocess.Popen(cmd)
    #
    #
    #    subprocess.Popen(cmd).communicate()

async def fetch(browser, id,index,id_list):
    try:
        page = await browser.newPage()
        await page.goto("https://www.moma.org/collection/works/" + id,{ 'waitUntil': 'domcontentloaded' })
        print("Загрузка началась")
        # await page.screenshot({'path': output_path +i+'.jpg'})
        # htmlContent = await page.content()
        # print(htmlContent)
        #selector = '#main > section.work > div.work__hero.layout\/wrapper > div.carousel > div'
        selector='#main > section.work > div.work__hero.layout\/wrapper > div.carousel'
        await page.waitForSelector(selector,{'visible': True})
        #print(index)
        #image_element = await page.querySelector(selector)
        pages = await browser.pages()
        await pages[index].bringToFront()
        # if image_element:
        #    # Use Pyppeteer's method to download the image
        #    await image_element.screenshot({'path': work_path + id + '.png'})
        #    print(f"Картинка скачана: {work_path}{id}")
        #    #photoshop(work_path + id + '.png')
        #    # Переключаемся на предыдущую страницу
        #    print("Индексы",index,len(id_list))
        await pages[index].bringToFront()
        return await page.content(), id
        #    return True
        #else:
        #    print("Не найдено.\n")
        #    await pages[index].bringToFront()
        #    return False
    except  Exception as e:
        print(e)

def parseWebpage(page,id):
    soup = bs4.BeautifulSoup(page,features="lxml")
    #print(soup.text)
    ma = soup.select_one(selector='img',class_='link/enable link/focus picture/image')
    print(ma['src'])
    return ma['src'],id
async def newrun(id_list):
    #asession = AsyncHTMLSession()
    #r = await asession.get('https://python.org/')
    #ma = await r.html.arender()
    print(id_list)
    id_list = [
        '199591',
        '199593',
        '199595'
    ]
    with ThreadPoolExecutor(max_workers=20) as executor:
        browser = await launch({"headless": False,"args": ["--start-minimized"]})
        loop = asyncio.get_event_loop()

        tasks = [
            await loop.run_in_executor(
                executor,
                fetch,
                *(browser, id,index,id_list)  # Allows us to pass in multiple arguments to `fetch`
            )
            for index,id in enumerate(id_list,start=0)
        ]
        for response in await asyncio.gather(*tasks):
            parse_data,id = parseWebpage(*response)
            print("Parse data",parse_data)
            image = save_image(parse_data,id)
            photoshop(image,id)
        await browser.close()
    # Initializes the tasks to run and awaits their results
    #for response in await asyncio.gather(*tasks):
    #    parseWebpage(response)
    #output_path = self.work_path
    #browser = await launch({"headless": False})
    #page = await browser.newPage()
    #await page.goto("https://www.moma.org/collection/works/"+i)
    #await page.screenshot({'path': output_path +i+'.jpg'})
    #htmlContent = await page.content()
    #print(htmlContent)
    #image_element = await page.querySelector('#main > section.work > div.work__hero.layout\/wrapper > div.carousel')
    #if image_element:
    #else:
    #    print("Не найдено.\n")
    #await browser.close()
    #def newrun(self,req,id):
    #    self.query = quote(req.replace(' ', '+').replace('…', '').replace('@', '').replace('(', '').replace(')', '').replace("‘", " "))
        #request_url = 'https://www.moma.org/collection/works/' + str(id)
        #request = urllib.request.Request(request_url, 2, headers=self.headers)
        #response = urllib.request.urlopen(request)
        #html = response.read().decode('utf8')
        #link = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
        #print(link)

        # asyncio.get_event_loop().run_until_complete(download_image(id))
        # async def main():
        #    browserObj = await launch({"headless": False})
        #    url = await browserObj.newPage()
        #    await url.goto('https://scrapeme.live/shop/')
    #
    #
    #    await browserObj.close()
def run(self,req,id):
    self.query = quote(req.replace(' ', '+').replace('…', '').replace('@', '').replace('(', '').replace(')', '').replace("‘"," "))
    request_url = 'https://www.bing.com/images/async?q=' + self.query \
                  + '&qft=' + 'filterui:photo-photo'+'+filterui:aspect-tall'
    request = urllib.request.Request(request_url, None, headers=self.headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf8')
    link = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
    #print(link[0::5])
    temp_load=0
    while True:
        if self.save_image(link[temp_load],id):
                break
        temp_load+=1
    #print("Скачивание Выполнено за {} итерации".format(temp_load+1))
def save_image_1(self, link,id):
    try:
        if " " in link:
            return False
        request = urllib.request.Request(link, None, self.headers)
        image = urllib.request.urlopen(request, timeout=2).read()
        if not imghdr.what(None, image):
            #print('Битая картинка т.к не удаётся определить расширение {}\n'.format(link))
            raise ValueError('Битая картинка т.к не удаётся определить расширение {}\n'.format(link))
        filename = self.work_path+str(id)+".png"
        with open(filename, 'wb') as f:
            f.write(image)
        photoshop(filename)
        return True
    except Exception as e:
        #print('403 '+link, e)
        return False
