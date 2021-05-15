from bs4 import BeautifulSoup
import re
from .pdog import pdoghtml

dog_time_re=re.compile(',n="(.*?)"')

class DogInfo(object):

    def __init__(self,doghtml):
        self.pubtime=int(dog_time_re.findall(doghtml)[0])
        dog=BeautifulSoup(doghtml)
        self.title = str(dog.find('meta',attrs={"property": "og:title"})['content'])
        self.description = str(dog.find(attrs={"property": "og:description"})['content'])
        self.author = str(dog.find(attrs={'name':"author"})['content'])
        c_dog=dog.find('div',attrs={"class": "rich_media_content"})
        self.cdog=str(c_dog)
        self.pdog=pdoghtml(c_dog.children)