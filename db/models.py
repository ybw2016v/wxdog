from sqlalchemy import Column, Integer, String, Text ,Boolean
from sqlalchemy.sql.sqltypes import DateTime, Float
from .db import Base
import random
import string

class Tdog(Base):
    __tablename__ = 'texts'
    id = Column(String(16), primary_key=True)
    url = Column(String(512), unique=False)
    pubtime= Column(String(16), unique=False)
    stime= Column(DateTime, unique=False)
    uid= Column(String(16), unique=False)
    ak= Column(String(256), unique=False)
    title = Column(String(512), unique=False)
    ctext = Column(Text, unique=False)
    ptext = Column(Text, unique=False)
    author = Column(String(256), unique=False)
    desp = Column(Text, unique=False)

    


    def __repr__(self):
        return '<User %r>' % (self.text)
    
    def ddog(self):
        return {"id":str(self.id),"ctext":self.ctext,"ptext":self.ptext,"title":self.title,'url':self.url,'pubtime':self.pubtime+'000',"author":self.author,"desp":self.desp,'uid':self.uid,'ak':self.ak,'stime': self.stime.astimezone().isoformat(timespec='milliseconds')  if (self.stime is not  None) else None}
    def pddog(self):
        return {"id":str(self.id),"title":self.title,'url':self.url,'pubtime':self.pubtime+'000',"author":self.author,"desp":self.desp,'uid':self.uid,'ak':self.ak,'stime': self.stime.astimezone().isoformat(timespec='milliseconds')  if (self.stime is not  None) else None}

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=30), unique=True)
    password = Column(String(length=128), unique=False)
    outlink = Column(String(length=20), unique=False)
    token = Column(String(length=20), unique=False)
    aurl = Column(String(512), unique=False)
    text = Column(Text, unique=False)
    isadmin = Column(Boolean,default=False)

    def new_token(self,ntoken=None):
        """
        docstring
        """
        if ntoken is None:
            self.token=''.join(random.sample(string.ascii_letters + string.digits, 10))
        else:
            self.token=ntoken
        return self.token

    def ddog(self):
        return {"id":self.id,"text":str(self.text),'aurl':self.aurl,'username':self.username,'outlink':self.outlink}

    def __repr__(self):
        return '%r' % (self.ddog())
