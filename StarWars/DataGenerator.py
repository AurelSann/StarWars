import numpy as np
from PIL import Image
import pandas as pd
import tensorflow as tf
from data import load_images

class DataGenerator(tf.keras.utils.Sequence):

    def __init__(self, df, batch_size=64, shuffle=True, ):
        self.batch_size = batch_size
        self.df = df
        self.indices = self.df.index.tolist()
        self.shuffle = shuffle
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
        return X, y
