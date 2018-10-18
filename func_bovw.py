import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from sklearn.cluster import KMeans

def computa_descritores(imgd):
    img = cv2.imread(imgd)
    surf = cv2.xfeatures2d.SURF_create()
    kp, des = surf.detectAndCompute(img, None)
    return des

def le_descritores_imagens(pastas, max_items=10):
    listacaminhos = []
    m = []
    for p in pastas:
        dire = sorted(os.listdir('./101_ObjectCategories/'+ p ))[:max_items]
        for f in dire:
            caminho = '101_ObjectCategories/{}/{}'.format(p,f)
            
            des = computa_descritores(caminho)
            
            listacaminhos.append(caminho)
            m.append(des)
            
    matrizes = np.vstack(m)
    
    return (listacaminhos, matrizes)

def cria_vocabulario(descritores,sz=300):
    km = KMeans(n_clusters=sz, random_state=0)
    km.fit(descritores)
    
    return km.cluster_centers_,km

def representa_histograma(img,vocab):
    des = computa_descritores(img)
    
    v = vocab.predict(des)
    
    c = [1 for i in range(vocab.n_clusters)] # todos comecam com frequencia 1
    for i in range(len(v)):
        c[int(v[i])] += 1
    
    return c, plt.bar(range(vocab.n_clusters), c)

def c_histograma(img,vocab):
    des = computa_descritores(img)
    
    v = vocab.predict(des)
    
    c = np.ones(vocab.n_clusters)#[1 for i in range(vocab.n_clusters)] # todos comecam com frequencia 1
    for i in range(len(v)):
        c[int(v[i])] += 1
    
    return c

def cria_contagem(pastas, vocab, max_items=10):
    lista_caminhos = []
    hb = []
    for p in pastas:
        dire = sorted(os.listdir('./101_ObjectCategories/'+ p ))[:max_items]
        for f in dire:
            caminho = '101_ObjectCategories/{}/{}'.format(p,f)
            
            h = c_histograma(caminho, vocab)

            hb.append([h, caminho])
    return hb
        

def x2_dist(hist1, hist2, vocab):
    x2 = 0
    for i in range(vocab.n_clusters):
        x2 += ((hist1[i] - hist2[i])**2)/hist2[i]
    return x2

def sim_5(imgd, path_desc, vocab, hist_banco):
    c1 = c_histograma(imgd, vocab)
    
    distances = []
    i = 0
    
    for img in path_desc[0]:
        c = hist_banco[i]
        d = x2_dist(c1,c, vocab)
        distances.append([d,path_desc[0][i]])
        i+=1
        
    lower5 = sorted(distances, key=lambda x:x[0])[:5]
    
    return lower5

# def show_sim(img1, path_desc1, vocab1, hist_banco, list_sim):
    
#     # list_sim = sim_5(img1, path_desc1, vocab1, hist_banco)

#     imgb = cv2.imread(img1)
#     plt.title('searched_img: {}'.format(img1))
#     plt.axis('off')
#     plt.imshow(cv2.cvtColor(imgb, cv2.COLOR_BGR2RGB))
#     plt.show()
    
#     for img in [row[1] for row in list_sim]:
#         plt.axis('off')
#         plt.title('img_path: {}'.format(img))
#         plt.imshow(cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB))
#         plt.show()

def show_sim(img1, path_desc1, vocab1, hist_banco, list_sim):
    
    # list_sim = sim_5(img1, path_desc1, vocab1, hist_banco)
    plt.figure(figsize=(20,5))
    plt.subplot(2,3,1)
    imgb = cv2.imread(img1)
    plt.title('searched_img: {}'.format(img1), color='red')
    plt.axis('off')
    plt.imshow(cv2.cvtColor(imgb, cv2.COLOR_BGR2RGB))
    # plt.show()
    i = 2
    for img in [row[1] for row in list_sim]:
        plt.subplot(2,3,i)
        plt.axis('off')
        plt.title('img_path: {}'.format(img))
        plt.imshow(cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB))
        # plt.show()
        i += 1
    plt.show()
    
def print_sim(img1, path_desc1, vocab1, hist_banco, list_sim):
    
    # list_sim = sim_5(img1, path_desc1, vocab1, hist_banco)

    print('imagem buscada: ', img1)
    print('imagens similares: ')
    for img in [row[1] for row in list_sim]:
        print('- ', img)
