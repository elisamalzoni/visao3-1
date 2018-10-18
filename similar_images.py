import func_bovw
import func_poi
import pickle
import sys

argimg = sys.argv[1]
argfuncsim = sys.argv[2]
argshowimg = False
if len(sys.argv) > 3:
    argshowimg = sys.argv[3]

if argfuncsim == 'poi':
    p1 = ['Caltech_cars','Caltech_motorbikes_side', 'TUGraz_bike', 'TUGraz_person']
    d1 = 57

    # descbanco = pickle.load(open("desc.p", 'rb'))
    # desc = [row[0] for row in descbanco][0]
    list_higher3 = func_poi.sim_3(argimg, p1)
    func_poi.print_sim(argimg, list_higher3)
    if argshowimg == 'show':
        func_poi.show_sim(argimg, list_higher3)

if argfuncsim == 'bovw':
    v = pickle.load(open("vocab.p", 'rb'))
    d = pickle.load(open('path_desc.p','rb'))

    func_bovw.print_sim(argimg, d, v)
    if argshowimg == 'show':
        func_bovw.show_sim(argimg, d, v)
