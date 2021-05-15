from tools.gethtml import get_dog_html
from tools.getinfo import DogInfo
import uuid
from datetime import datetime , timedelta 

from db.db import *
from db.models import Tdog,Dog

def addog(dogid,dogurl):
    """
    处理并插入数据
    """
    dog_html=get_dog_html(dogurl)
    dog_info=DogInfo(dog_html)
    rdog=Tdog.query.filter(Tdog.id==dogid).first()
    rdog.url="https://mp.weixin.qq.com/s/{}".format(dogurl)
    rdog.title=dog_info.title
    # rdog.ctext=dog_info.cdog
    rdog.pubtime=dog_info.pubtime
    rdog.stime=datetime.now()
    rdog.ak=str(uuid.uuid4())
    rdog.ptext=dog_info.pdog
    rdog.author=dog_info.author
    rdog.desp=dog_info.description
    # new_dog=Tdog(id=dogid,url="https://mp.weixin.qq.com/s/{}".format(dogurl),pubtime=dog_info.pubtime,stime=datetime.now(),ak=str(uuid.uuid4()),uid=uidog,title=dog_info.title,ctext=dog_info.cdog,,author=dog_info.author,desp=dog_info.description)
    # db_session.add(new_dog)
    db_session.commit()
