# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:15:43 2019
@author: Reza Azad
"""
from __future__ import division
import numpy as np
import scipy.io as sio
import scipy.misc as sc
import glob
import random
#from sklearn.model_selection import train_test_split

# Parameters
height = 256
width  = 256
channels = 3

############################################################# Prepare ph2 data set #################################################
Dataset_add = '../data/dataset_PH2_test/'
Tr_add = 'images'

Tr_list = glob.glob(Dataset_add+ Tr_add+'/*.bmp')
# It contains 200 training samples
Data_train    = np.zeros([200, height, width, channels])
Label_train   = np.zeros([200, height, width])

print('Reading Ph2')

random.shuffle(Tr_list)

for idx in range(len(Tr_list)):
    print(idx+1)
    print(Tr_list[idx])
    img = sc.imread(Tr_list[idx])

   
    img = np.double(sc.imresize(img, [height, width, channels], interp='bilinear', mode = 'RGB'))
    Data_train[idx, :,:,:] = img

    
    b = Tr_list[idx]  

    #print(b)  

    a = b[0:len(Dataset_add)]
    b = b[len(b)-10: len(b)-4] 

    # print(a)
    # print(b)


    add = (a+ 'masks/' + b +'_lesion.bmp')    
    img2 = sc.imread(add)
    img2 = np.double(sc.imresize(img2, [height, width], interp='bilinear'))
    Label_train[idx, :,:] = img2    
         
print('Reading Ph2 finished')

################################################################ Make the train and test sets ########################################    
# We consider 80 samples for training, 20 samples for validation and 100 samples for testing


Test_img       = Data_train[0:200,:,:,:]

Test_mask       = Label_train[0:200,:,:]


np.save('data_test' , Test_img)

np.save('mask_test' , Test_mask)
