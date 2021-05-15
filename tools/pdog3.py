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
            rdog='<p>{}</p>'.format(edog.string)
    elif edog.parent.name=='strong':
        rdog='<strong>{}</strong>'.format(edog.string)
    else :
        rdog=''
    return rdog

def pdoghtml(hdog):
    if hasattr(hdog,'contents') is not True :
        return pdogtag(hdog)
    elif hdog.contents==[]:
        return pdogtag(hdog)
    else:
        rdog=''
        for ndog in hdog.children:
            rdog=rdog+pdoghtml(ndog)
        return rdog