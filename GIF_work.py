from PIL import Image
from PIL import ImageSequence
import imageio
import os
def getFrames(im):
    '''提取每一帧'''
    if False == im.is_animated :
        return;
    index = 1
    for frame in ImageSequence.Iterator(im):
        frame = frame.convert('RGB')
        frame.save("g%d.jpg" % index)
        compressImg('g%d.jpg'% index)
        index = index + 1
    return index
def compressImg(ImgName):
    '''压缩图片'''
    im = Image.open(ImgName)
    im.convert('RGB')
    # if max(im.size[0], im.size[1]) < 900:
    re_im=im.resize((1200, 900))
    re_im.save('f-'+ImgName, quality=95)
    # return 'OK'
def compressGif(ind,dur):
    '''合成GIF'''
    images = []
    for i in range(1, ind):
        images.append(imageio.imread('f-g%d.jpg' % i))
    imageio.mimsave('nice.gif', images, duration = dur)
def calDuration(im):
    '''计算帧率'''
    return (im.info)['duration'] / 1000
def removeImg(ind):
    '''移除图片'''
    for i in range(1,ind):
        af = 'f-g' + str(i) + '.jpg'
        f = 'g' + str(i) + '.jpg'
        if os.path.exists(af):
            os.remove(af)
        if os.path.exists(f):
            os.remove(f)
im=Image.open("E:\\PIXIV\\trans.gif")
index=getFrames(im)
compressGif(index,calDuration(im))
removeImg(index)