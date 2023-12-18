import random
import urllib.request
import urllib
import re
import imghdr
from PIL import Image, ImageOps, ImageFont
from PIL import ImageDraw
def photoshop(filename,name):
    img = Image.open(filename)
    rgba = img.convert("RGBA")
    resize = ImageOps.pad(rgba, (200,300), color=(255, 255, 255, 0))
    #border = (0, 0, 0, 0)
    #final = ImageOps.expand(resize, border=border, fill='black') #задел на дополнение картинки, вместо обрезки
    resize.save(filename,"PNG")
class ImageLoader:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko)'
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.3,*;q=0.7',
      'Accept-Encoding': 'none',
      'Accept-Language': 'ru,en;q=0.9',
      'Connection': 'keep-alive'}
        self.download_count = 0
        self.work_path = "./images/"
    def run(self,req,amount = 1):
        self.query = req.replace(' ', '+').replace('…', '').replace('@', '').replace('(', '').replace(')', '').replace("‘"," ")
        request_url = 'https://www.bing.com/images/async?q=' + self.query \
                      + '&qft=' + 'filterui:photo-photo'+'+filterui:aspect-tall'
        request = urllib.request.Request(request_url, None, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf8')
        link = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
        #print(link[0::5])
        temp_load=0
        while True:
            if self.save_image(link[temp_load],self.query):
                    break
            temp_load+=1
        #print("Скачивание Выполнено за {} итерации".format(temp_load+1))


    def save_image(self, link,req):
        try:
            if " " in link:
                return False
            request = urllib.request.Request(link, None, self.headers)
            image = urllib.request.urlopen(request, timeout=2).read()
            if not imghdr.what(None, image):
                #print('Битая картинка т.к не удаётся определить расширение {}\n'.format(link))
                raise ValueError('Битая картинка т.к не удаётся определить расширение {}\n'.format(link))
            filename = self.work_path+str(self.download_count)+".png"
            with open(filename, 'wb') as f:
                f.write(image)
            photoshop(filename,req.replace("+"," ")) #второй аргумент тут не нужен, передаётся на всякий (содержит текст запроса название картины + автор)
            self.download_count += 1
            return True
        except Exception as e:
            #print('403 '+link, e)
            return False