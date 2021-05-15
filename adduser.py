from db.db import *
from db.models import Dog
from tools.tooldog import *


import sys

dname = sys.argv[1]


if len(sys.argv)<=2:
    dpass= sys.argv[1]
else:
    dpass=123456

psd5=get_md5('{}^_^{}>_<'.format(dname,dpass))

newdog=Dog(username=dname,password=psd5)

tokendog=newdog.new_token()

print('{}\n{}\n{}\n{}'.format(dname,dpass,tokendog,psd5))

db_session.add(newdog)
db_session.commit()

