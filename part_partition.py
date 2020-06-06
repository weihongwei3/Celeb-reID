import os
import cv2

name = 'gallery'
# name = 'query'
# name = 'train'

path = './' + name + '/'

new_path1 = './' + name + '_1_1/'
if not os.path.exists(new_path1):
    os.mkdir(new_path1)

new_path2 = './' + name + '_1_2/'
if not os.path.exists(new_path2):
    os.mkdir(new_path2)

new_path3 = './' + name + '_1_3/'
if not os.path.exists(new_path3):
    os.mkdir(new_path3)

new_path4 = './' + name + '_2_1/'
if not os.path.exists(new_path4):
    os.mkdir(new_path4)

new_path5 = './' + name + '_2_2/'
if not os.path.exists(new_path5):
    os.mkdir(new_path5)

# im_list = dir([path, '*.jpg'])
im_list = os.listdir(path)

for i in range(len(im_list)):
    im = cv2.imread(path + im_list[i])

    # [h, w, c] = size(im)
    h, w = im.shape[:2]

    im_1_1 = im[0:h // 3, :]
    im_1_2 = im[h // 3:(h // 3) * 2, :]
    im_1_3 = im[(h // 3) * 2:h, :]

    im_2_1 = im[0:h // 2, :]
    im_2_2 = im[h // 2:h, :]

    cv2.imwrite(new_path1 + im_list[i], cv2.resize(im_1_1, (224, 224)))
    cv2.imwrite(new_path2 + im_list[i], cv2.resize(im_1_2, (224, 224)))
    cv2.imwrite(new_path3 + im_list[i], cv2.resize(im_1_3, (224, 224)))
    cv2.imwrite(new_path4 + im_list[i], cv2.resize(im_2_1, (224, 224)))
    cv2.imwrite(new_path5 + im_list[i], cv2.resize(im_2_2, (224, 224)))
