import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import os

def ext_descr(im):
    img = cv2.imread(im)
    orb = cv2.ORB_create()
    keypoints = orb.detect(img, None)
    keypoints, des = orb.compute(img, keypoints)
    img2 = cv2.drawKeypoints(img, keypoints, None, flags=0)
    return des, img2, keypoints

def dist(d1, d2):
    d1s = '{0:08b}'.format(d1)
    d2s = '{0:08b}'.format(d2)
    
    d = 0
    
    for i in range(len(d1s)):
        if d1s[i] != d2s[i]:
            d +=1
    return d

def reciprocal_match(desc1, desc2, max_dist):
    list_match =[]
    for i in range(desc1.shape[0]):
        menor_dist = float("inf")
        
        for j in range(desc2.shape[0]):
            dij = 0
            
            for e in range(desc1.shape[1]):
                
                d1 = desc1[i][e]
                d2 = desc2[j][e]
                d = dist(d1,d2)
                dij += d
                
            if dij < menor_dist:
                menor_dist = dij
                jm = j

            if menor_dist < max_dist:
                list_match.append(cv2.DMatch(i, jm, menor_dist))
    return list_match

def similarity_proportion_matches(im1, im2):
    d= 57
    des1, img1kp, kp1 = ext_descr(im1)
    des2, img2kp, kp2 = ext_descr(im2)
    
    m = reciprocal_match(des1, des2, d)
    
    similarity = len(m)/des1.shape[0]
    
    return similarity/100

def sim_3(im1, pastas, max_items=5):
    
    sim1 = []
    
    for p in pastas:
        dire = (os.listdir('./VOC2005_1/PNGImages/'+ p ))[:max_items]
        for f in dire:
            caminho = './VOC2005_1/PNGImages/{}/{}'.format(p,f)
            
            simi1 = similarity_proportion_matches(im1, caminho)
            
            sim1.append([simi1, caminho])


    
    higher31 = sorted(sim1, key=lambda x:x[0], reverse=True)[:3]


    return higher31

# def sim_3(img, pastas, d1, desc, max_items=5):
#     d = d1
#     sim1 = []
#     i = 0
#     for p in pastas:
#         dire = (os.listdir('./VOC2005_1/PNGImages/'+ p ))[:max_items]
#         for f in dire:
#             caminho = './VOC2005_1/PNGImages/{}/{}'.format(p,f)
            
#             simi1 = similarity_proportion_matches(img, desc[i], d1)
            
#             sim1.append([simi1, caminho])
#             i += 1

#     higher31 = sorted(sim1, key=lambda x:x[0], reverse=True)[:3]

#     return higher31

def show_sim(img1, list_sim):
    
    imgb = cv2.imread(img1)
    plt.title('searched_img: {}'.format(img1))
    plt.axis('off')
    plt.imshow(cv2.cvtColor(imgb, cv2.COLOR_BGR2RGB))
    plt.show()
    
    for img in [row[1] for row in list_sim]:
        plt.axis('off')
        plt.title('img_path: {}'.format(img))
        plt.imshow(cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB))
        plt.show()

def print_sim(img1, list_sim):
    print('imagem buscada: ', img1)
    print('imagens similares: ')

    for img in [row[1] for row in list_sim]:
        print('- ', img)
