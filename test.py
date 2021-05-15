from bs4 import BeautifulSoup
from tools.pdog2 import pdoghtml
import re 
# rmp = re.compile('<p></p>')
# rmp

ppo = BeautifulSoup(open('ppu.html'))

cdog=ppo.find('div',attrs={"class": "rich_media_content"})

llo = pdoghtml(cdog.children)

print(llo)