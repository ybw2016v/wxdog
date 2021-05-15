
def pdoghtml(edog):
    resdog=''
    for hdog in edog:
        # print(hdog)
        # iio=input()
        if hdog.name=='img':
            rdog='<img data-src="{}" src="{}">'.format(hdog['data-src'],hdog['data-src'])
            resdog = resdog + rdog
        elif hasattr(hdog,'contents'):
            pdog = pdoghtml(hdog.children)
            if pdog != '' and pdog.replace(" ", "")!='':
                if hdog.name=='p':
                    resdog = resdog +  '<p>{}</p>'.format(pdog)
                elif hdog.name=='span':
                    resdog = resdog +  '<span>{}</span>'.format(pdog)
                elif hdog.name=='strong':
                    resdog = resdog +  '<strong>{}</strong>'.format(pdog)
                else:
                    resdog = resdog +  pdog
        else:
            resdog = resdog +  str(hdog)
    return resdog
