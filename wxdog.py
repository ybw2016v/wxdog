import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime , timedelta
from sqlalchemy import or_

from flask import Flask, abort, jsonify, redirect, request, url_for,render_template,make_response
from flask.globals import session
from flask_redis import FlaskRedis
from flask_restful import Api, Resource, abort, reqparse

from db.db import *
from db.models import Tdog,Dog
from gid import gen_dog_id
from addog import addog
from tools.tooldog import *


parser = reqparse.RequestParser()
parser.add_argument('c', type=str, help='内容')
parser.add_argument('p', type=str, help='密码')
# parser.add_argument('t', type=int, help='过期时间（h）')
# parser.add_argument('r', type=float, help='显示概率')
parser.add_argument('i', type=str, help='访问token')
# parser.add_argument('g', type=int, help='是否生成图片')
parser.add_argument('y', type=int, help='页数')

executor = ThreadPoolExecutor(4)

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)

class lsdogs(Resource):
    def post(self):
        args = parser.parse_args()
        c=args['y']
        tokend =args["i"]
        asp=Dog.query.filter(Dog.token==tokend).first()
        if asp is None:
            return {'r':'403','data':None}
        try:
            page=int(c) if (c is not None) else 0
            sdl=Tdog.query.order_by(Tdog.pubtime.desc()).filter(Tdog.url!=None).limit(10).offset(page*10)
            nnu=Tdog.query.count()
        except :
            return "error"
        oop=[]
        for sdp in sdl:
            oop.append(sdp.ddog())
        return {"n":nnu,"p":page,"data":oop}

class plsdogs(Resource):
    def get(self):
        try:
            sdl=Tdog.query.order_by(Tdog.pubtime.desc()).filter(Tdog.ak!=None).limit(4)
        except :
            return "error"
        oop=[]
        for sdp in sdl:
            oop.append(sdp.ddog())
        return {"data":oop}
    def post(self):
        try:
            sdl=Tdog.query.order_by(Tdog.pubtime.desc()).filter(Tdog.ak!=None).limit(4)
        except :
            return "error"
        oop=[]
        for sdp in sdl:
            oop.append(sdp.ddog())
        return {"data":oop}

class addogs(Resource):
    def post(self):
        args = parser.parse_args()
        c = args["c"]
        i = args['i']
        udog=Dog.query.filter(Dog.token==i).first()
        if (udog is None) or (c == None) :
            return {"r":403}
        else:
            olddog = Tdog.query.filter(Tdog.url.like('%{}%'.format(c))).first()
            print(c)
            if olddog is not None:
                return {"r":"重复"}
            else:
                dogid=gen_dog_id()
                dogurl = "https://mp.weixin.qq.com/s/{}".format(c)
                new_dog=Tdog(id=dogid,stime=datetime.now(),uid=1,url=dogurl)
                db_session.add(new_dog)
                db_session.commit()
                # addog(dogid,c)
                executor.submit(addog,dogid,c)
                return {'r':"ok",'id':dogid}

class logindog(Resource):
    def post(self):
        args = parser.parse_args()
        dusername = args["c"]
        passwd = args["p"]
        pd5=get_md5('{}^_^{}>_<'.format(dusername,passwd))
        asp=Dog.query.filter(Dog.password==pd5).filter(Dog.username==dusername).first()
        if asp is None:
            return {'r':'bad','i':None}
        else:
            return {'r':'s','i':asp.token}

class rmdog(Resource):
    def post(self):
        args = parser.parse_args()
        c = args["c"]
        i = args['i']
        udog=Dog.query.filter(Dog.token==i).first()
        if (udog is None) or (c == None) :
            return {"r":403}
        else:
            asp=Tdog.query.filter(Tdog.id==c).first()
            db_session.delete(asp)
            db_session.commit()
            return {'r':'s','id':c}

class doginfos(Resource):
    def post(self):
        args = parser.parse_args()
        tokend =args["i"]
        asp=Dog.query.filter(Dog.token==tokend).first()
        if asp is None:
            return {'r':'403','data':None}
        else:
            return {'r':'s','data':asp.ddog()}

api.add_resource(addogs, '/api/create/')
api.add_resource(lsdogs, '/api/list/')
api.add_resource(plsdogs, '/api/plist/')
api.add_resource(logindog, '/api/login/')
api.add_resource(rmdog, '/api/remove/')
api.add_resource(doginfos, '/api/user/')

@app.route('/rss.xml')
def rssdog():
    sdl=Tdog.query.order_by(Tdog.pubtime.desc()).filter(Tdog.ak!=None).limit(10)
    itemsdog=[]
    timedoge=str(datetime.now())
    for dogs in sdl:
        itemsdog.append(dogs.ddog())
    # print(itemsdog)
    rspdog = make_response(render_template('rss.xml',datedog=timedoge,items=itemsdog))
    rspdog.headers['Content-Type']='application/xml; charset=utf-8'

    return rspdog


@app.route('/xhrss.xml')
def xhrssdog():
    sdl=Tdog.query.order_by(Tdog.pubtime.desc()).filter(Tdog.ak!=None).limit(10)
    itemsdog=[]
    timedoge=str(datetime.now())
    for dogs in sdl:
        itemsdog.append(dogs.ddog())
    # print(itemsdog)
    rspdog = make_response(render_template('xhrss.xml',datedog=timedoge,items=itemsdog))
    rspdog.headers['Content-Type']='application/xml; charset=utf-8'

    return rspdog

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')