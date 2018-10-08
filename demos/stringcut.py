#operate string of imgdata ,get the new string after ','

def cutstr(sStr1,sStr2):
    nPos = sStr1.index(sStr2)
    
    return sStr1[(nPos+1):]

if __name__ == '__main__':
    print (cutstr('qwe,qw123123e2134123',','))


