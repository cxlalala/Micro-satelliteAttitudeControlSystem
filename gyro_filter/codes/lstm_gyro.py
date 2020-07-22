'''
info:  by cx
'''
import numpy as np
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow.keras.layers import LSTM,Dense,Masking,Input,Dropout,Flatten,Reshape
from tensorflow.keras.layers import Layer

def lstm_model():
    input_net = Input(shape=(5,1),name='main_input')
    net = LSTM(1000,input_shape=(5,1),name='lstm_1',return_sequences=True)(input_net)
    net = LSTM(1000,name='lstm_2',return_sequences=True)(net)
    net = Dense(1,activation='linear',name='main_output')(net)
    model = Model(input_net, net)
    model.compile(optimizer='adam',loss={'main_output': 'mse'},loss_weights={'main_output': 1.},metrics=['accuracy'])
    return model

