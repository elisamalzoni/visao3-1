import func_bovw
import pickle

p = ["Faces", "garfield", "platypus", "nautilus", "elephant", "gerenuk"]
d = func_bovw.le_descritores_imagens(p)
cc, km = func_bovw.cria_vocabulario(d[1])
contagem = func_bovw.cria_contagem(p, km)
        

pickle.dump(km, open("vocab.p", "wb"))
pickle.dump(d, open("path_desc.p", "wb"))
pickle.dump(contagem, open("count.p", "wb"))

