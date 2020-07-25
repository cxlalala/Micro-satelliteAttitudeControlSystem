import numpy as np
import pandas as pd
import log
import hdf5
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 10000000

hdf5.path_hdf5s()
progress_logger = log.logger('progress_made.log')

state = np.random.rand(N)
mu, sigma = 0, 0.1
noise = np.random.normal(mu, sigma, N)
state_noise = state+noise
#print(state)
#print(noise)

progress_logger.debug('dataset_log')
hdf5.create_hdf5(state, state_noise)