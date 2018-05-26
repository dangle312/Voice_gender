import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GMM
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")


#path to training data
source   = "trainingData/"

modelpath = "trainModels/"

f = "test0.wav"        


gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

models = []
for i in range(len(gmm_files)):
    file = open(gmm_files[i], 'rb')
    models.insert(i, cPickle.load(file))


genders   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]

print f.split("\\")[-1]

sr,audio = read(f)
vector   = extract_features(audio,sr)

log_likelihood = np.zeros(len(models)) 

for i in range(len(models)):
    gmm    = models[i]         #checking with each model one by one
    scores = np.array(gmm.score(vector))
    log_likelihood[i] = scores.sum()
winner = np.argmax(log_likelihood)
print "\tdetected as - ", genders[winner],"\n"