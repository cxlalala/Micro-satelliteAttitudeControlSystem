import numpy as np
import h5py
import os
import log
import lstm_gyro
import random
from tensorflow import keras as K
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import multi_gpu_model
from tensorflow.keras import optimizers, callbacks

# paths and loggers
train_hdf5s_path = os.path.abspath(r'..')+'/dataset/hdf5s/'

def model_path_hdf5s():
    '''
    It is using for creating new folder at the current path and change the work path to the new folder.
    '''
    cwd = os.getcwd()
    if not os.path.exists(cwd+'/model'):
        os.makedirs(cwd+'/model')
    os.chdir(cwd+'/model')

model_path_hdf5s()
progress_logger = log.logger('model.log')

# model
my_model = lstm_gyro.lstm_model()
#parallel_model = multi_gpu_model(my_model,gpus=2)

f = h5py.File(train_hdf5s_path+'dataset.hdf5','r')
train_x = f['/state_noise'][:]
train_y = f['/state'][:]
f.close()

# fit
my_filepath = 'weights.hdf5'
#parallel_model.compile(loss='mse', optimizer=optimizers.Adam(lr=0.0001, decay=1e-5), metrics=['accuracy'])

'''
if os.path.exists(my_filepath):
    parallel_model.load_weights(my_filepath)
    # 若成功加载前面保存的参数，输出下列信息
    print("checkpoint_loaded")
'''
callbacks = [
# 把TensorBoard日志写到'logs'里面
callbacks.TensorBoard(log_dir='./logs'),
# accuracy，也就是分类精度在10个epoh之内都没提升时，降低learning rate
callbacks.ReduceLROnPlateau(monitor='loss', patience=10, verbose=1),
# accuracy在15个epoch内没有提升的时候，停止训练
callbacks.EarlyStopping(monitor='loss', patience=15, verbose=1),
ModelCheckpoint(filepath=my_filepath, verbose=1, save_weights_only=True, save_best_only=True)
]
history = my_model.fit({'main_input': train_x},{'main_output': train_y},epochs=1000,batch_size=10,verbose=1, shuffle=False, validation_split=0.2, callbacks=callbacks)
#history = my_model.fit_generator(my_generator(package_name_list, 100), steps_per_epoch=train_count, epochs=500, verbose=1, validation_data=val_my_generator(package_name_list, 100), validation_steps=val_train_count, callbacks=callbacks)
#history = parallel_model.fit_generator(my_generator(package_name_list, 100), steps_per_epoch=train_count, epochs=5, verbose=1, validation_data=val_my_generator(package_name_list, 100), validation_steps=val_train_count, callbacks=callbacks)
my_model.save_weights('latest.weights.hdf5')
progress_logger.debug("train_log")

# saves the model weights after each epoch if the validation loss decreased  
f = h5py.File('history.hdf5','w')
f.create_dataset('/history/loss', data=history.history['loss'])
#f.create_dataset('/history/acc', data=history.history['acc'])
f.create_dataset('/history/val_loss', data=history.history['val_loss'])
#f.create_dataset('/history/val_acc', data=history.history['val_acc'])
f.close()
