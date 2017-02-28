#!/usr/bin/env python
############################################
#        bendahmane.amine@gmail.com        #
############################################

import numpy as np
import cPickle
from sklearn.svm import SVC

X = np.array([[10], [11], [10], [11], [9], [10], [11], [10], [11], [9],
			  [18], [17], [18], [19], [18], [19], [17], [20], [17], [18]])
y = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
			  10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

model = SVC()
model.fit(X, y) 

pretrained_model_path = "pretrained-smart-lamp.model"
with open(pretrained_model_path, 'wb') as f:
    cPickle.dump(model, f)