import numpy as np
import h5py
import os
import log
import random
from tensorflow.keras.models import load_model
import lstm_gyro
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import MinMaxScaler

# path
cwd = os.getcwd()
model_path = cwd+'/model/'
hdf5s_path = os.path.abspath(r'..')+'/dataset'+'/hdf5s/'

progress_logger = log.logger('tester.log')

# read data
f = h5py.File(hdf5s_path+'pre_dataset.hdf5', 'r')
state = f['/state'][:]
state_noise = f['/state_noise'][:]
print(state_noise.shape)

f = h5py.File(hdf5s_path+'dataset.hdf5', 'r')
valstate = f['/state'][:]
valstate_noise = f['/state_noise'][:]
print(valstate_noise.shape)

# predict
my_model = lstm_gyro.lstm_model()
my_model.load_weights(model_path+'latest.weights.hdf5')
progress_logger.debug('start')
predict_y = my_model.predict(state_noise)
progress_logger.debug('end')
predict_y = predict_y.reshape(predict_y.shape[0],1)
valpredict_y = my_model.predict(valstate_noise)
valpredict_y = valpredict_y.reshape(valpredict_y.shape[0],1)

e_pretrain = np.abs(state-state_noise)
e_train = np.abs(state-predict_y[:,0])
e_prevaltrain = np.abs(valstate-valstate_noise)
e_valtrain = np.abs(valstate-valpredict_y[:,0])

e_pretrain = e_pretrain.reshape(e_pretrain.shape[0],1)
e_train = e_train.reshape(e_train.shape[0],1)
e_prevaltrain = e_prevaltrain.reshape(e_prevaltrain.shape[0],1)
e_valtrain = e_valtrain.reshape(e_valtrain.shape[0],1)

c_pretrain = 0
c_train = 0
c_prevaltrain = 0
c_valtrain = 0

for i in range(0, state.shape[0]):
    c_pretrain = c_pretrain+e_pretrain[i,0]
    c_train = c_train+e_train[i,0]
    c_prevaltrain = c_prevaltrain+e_prevaltrain[i,0]
    c_valtrain = c_valtrain+e_valtrain[i,0]

print(c_train, c_pretrain, c_valtrain, c_prevaltrain)

# history
f = h5py.File(model_path+'history_class_1.hdf5','r')
loss = f['/history/loss'][:]
val_loss = f['/history/val_loss'][:]
f.close()

plt.figure()
plt.plot([i for i in range(loss[:].shape[0])], loss[:])
plt.grid()
plt.figure()
plt.plot([i for i in range(loss[:].shape[0])], val_loss[:])
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid()

# vision
plt.figure()
plt.plot([i for i in range(state[:].shape[0])], state[:])
plt.plot([i for i in range(predict_y[:].shape[0])], predict_y[:])
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid()
plt.show()

