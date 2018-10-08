from compare import getRep
import numpy as np
import os
import requests
np.set_printoptions(precision=2)

# test


def facedis(stu_id):
    path = os.path.abspath('.')
    
    img1 = 'real_time.png'
    #img2 = stu_id+'.jpg'
    img_url ="https://mxueli.xjtudlc.com/Upload/StudentPicture/10698/zp/1809/199/zp1069819918090002.jpg"
    r = requests.get(img_url)
    with open('img2.jpg', 'wb') as f:
        f.write(r.content)  
    img2 = 'img2.jpg'
    p_path =os.path.join(path,'info',img2)
    print p_path
    print os.path.exists(p_path)
    #if os.path.exists(p_path):
    if os.path.exists(img2):
        #d = getRep(img1) - getRep(p_path)
        d = getRep(img1) - getRep(img2)
        print("Comparing {} with {}.".format(img1, img2))
        print(
            "  + Squared l2 distance between representations: {:0.3f}".format(np.dot(d, d)))
        return np.dot(d, d)
    else:
        raise Exception("no photos in files")

if __name__ == '__main__':
    facedis()

