import pandas as pd
from google.cloud import storage
import gcsfs
import numpy as np
import pandas as pd
from PIL import Image
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from numpy import expand_dims
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt
import tensorflow as tf
from data import load_images

class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, df, batch_size=64, shuffle=True, ):
        self.batch_size = batch_size
        self.df = df
        self.indices = self.df.index.tolist()
        self.shuffle = shuffle
        self.augmentator = ImageDataGenerator(
                              rotation_range=90,
                              width_shift_range=[-50,50],
                              height_shift_range=0.5,
                              brightness_range= [0.2, 1.9],
                              horizontal_flip=True,
                              fill_mode='nearest')
        self.on_epoch_end()
    def __len__(self):
        '''returns number of minibatches per epoch'''
        return len(self.indices) // self.batch_size
    def on_epoch_end(self):
        '''shuffles the indices '''
        self.index = np.arange(len(self.indices))
        if self.shuffle == True:
            np.random.shuffle(self.index)
    def __get_X_image(self, df):
        '''returns images'''
        X = load_images(df)
        return X
    def __get_Y(self, df):
        '''returns y'''
        return np.array(df.drop(columns=["image"]))
    def _get_data(self, batch):
        '''returns batch of images and y'''
        df_batch = self.df.query("index in @batch")
        X = self.__get_X_image(df_batch)
        y = self.__get_Y(df_batch)
        return X, y
    def __getitem__(self, index):
        '''creates batches and returns final X and y'''
        index = self.index[index * self.batch_size:(index + 1) * self.batch_size]
        batch = [self.indices[k] for k in index]
        X, y = self._get_data(batch)
        # Add Augmentator sa class attr
        X_augmented = self.augmentator.flow(X, batch_size=self.batch_size, shuffle=False)
        return next(X_augmented), y
