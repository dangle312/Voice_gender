# -*- coding: utf-8 -*-
#train_models.py

import cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GMM 
from speakerfeatures import extract_features
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")




#path to training data
source   = "trainingData/"

#path where training speakers will be saved
dest = "trainModels/"

train_file = "trainingData.txt"

file_paths = open(train_file,'r')

count = 1


# Extracting features for each speaker (8 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    
    
    # read the audio
    sr,audio = read(source + path)

    # extract 10 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)

    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 8 files of speaker are concatenated, then do model training
    if count == 8:
        gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)

        # dumping the trained gaussian model
        picklefile = path.split("/")[0]+".gmm"

        cPickle.dump(gmm,open(dest + picklefile,'w'))
        print '+ done:',picklefile
        features = np.asarray(())
        print 'complete'
        count = 0
    count = count + 1
