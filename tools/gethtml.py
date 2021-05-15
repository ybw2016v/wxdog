import requests as r

dog_head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 dogcraft/wxdog neko.red'}

def get_dog_html(dogid):
    dog_r=r.get('https://mp.weixin.qq.com/s/{}'.format(dogid),headers=dog_head)
    return dog_r.text