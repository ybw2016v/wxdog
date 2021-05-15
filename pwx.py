from bs4 import BeautifulSoup



def pdogtag(edog):
    if edog.name=='img':
        rdog='<img data-src="{}" src="{}">'.format(edog['data-src'],edog['data-src'])
    elif str(edog).replace(" ", "").replace('\n', '').replace('\r', '')=='':
        rdog = ''
    elif edog.parent.name=='p' :
        if edog.string==None or edog.string=='':
            rdog = ''
        else:
            rdog='<p>{}</p>'.format(edog.string)
    elif  edog.parent.name=='span':
        if edog.string==None or edog.string=='':
            rdog = ''
        else:
            rdog='<span>{}</span>'.format(edog.string)
    elif edog.parent.name=='strong':
        rdog='<strong>{}</strong>'.format(edog.string)
    else :
        rdog=''
    # print('+{}|{}|{}'.format(edog.parent.name,rdog,str(edog)))
    return rdog

def pdoghtml(hdog):
    if hasattr(hdog,'contents') is not True :
        # print(hdog)
        
        return pdogtag(hdog)
    # elif hasattr(hdog,'children') is not True:
    #     print('+'+hdog)
    #     return ''
    elif hdog.contents==[]:
        return pdogtag(hdog)
    else:
        rdog=''
        # if hasattr(hdog,'children') is not True:
        #     return rdog
        for ndog in hdog.children:
            # print(ndog)
            rdog=rdog+pdoghtml(ndog)
        return rdog

# def pdoghtml(edog):
#     for ndog in edog.descendants:
#         print(ndog)
#     return 0
#     pass

oop=pdoghtml(cdog)
print(oop)

def pdogfile(dogfilename):
    dog=BeautifulSoup(open(dogfilename))
    title = dog.find('meta',attrs={"property": "og:title"})['content']
    description = dog.find(attrs={"property": "og:description"})['content']
    author = dog.find(attrs={'name':"author"})['content']
    cdog=dog.find('div',attrs={"class": "rich_media_content"})
    cont= pdoghtml(cdog)
    return {'title':title,'description':description,'author':author,'futext':cont}