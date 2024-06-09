import os
import pickle
import json

def model_run_grad(s1, s2, s3, s4):
    l_input = [int(s1), int(s2), int(s3), int(s4)]
    return model_run(l_input)

def model_run(l_input):
    #l_input = [1,1,1,1]
    with open('/app/iris_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    return model.predict([l_input])[0]


