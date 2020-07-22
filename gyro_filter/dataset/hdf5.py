'''
File Name: hdf5.py
Author: ChuXuan
'''
import numpy as np
import h5py
import log
import os
import fcntl

def path_hdf5s():
    '''
    It is using for creating new folder at the current path and change the work path to the new folder.
    '''
    cwd = os.getcwd()
    if not os.path.exists(cwd+'/hdf5s'):
        os.makedirs(cwd+'/hdf5s')
    os.chdir(cwd+'/hdf5s')


def create_hdf5(state, state_noise):
    '''
    It is using for creating a hdf5 file.
    '''
    f = h5py.File('dataset.hdf5', 'w')
    f.create_dataset('/state', data=state)
    f.create_dataset('/state_noise', data=state_noise)
    f.close()
