from gid import gen_dog_id
from addog import addog
from sqlalchemy.orm import session
from tools.gethtml import get_dog_html
from tools.getinfo import DogInfo
import uuid
from datetime import datetime , timedelta 
from concurrent.futures import ThreadPoolExecutor

from db.db import *
from db.models import Tdog,Dog


executor = ThreadPoolExecutor(2)

idog=gen_dog_id()
url='lhSzHxzHf8EjAIdLoDPrdQ'
uid=1

new_dog=Tdog(id=idog,stime=datetime.now(),uid=1)
db_session.add(new_dog)
db_session.commit()


executor.submit(addog,idog,url)
# addog(idog,url)
# addog(idog,url)
