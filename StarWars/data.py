'''Get DataFrame from Aurelien Bucket'''

import pandas as pd
from google.cloud import storage
import numpy as np
from PIL import Image


BUCKET_DATA_PATH = "gs://lw-verspieren-starwars/data/"


def rename(GalaxyID):
    return str(GalaxyID)+'.jpg'

def get_data(y, nrows): # add nrows to sample
    '''returns a DataFrame with nrows from s3 bucket'''

    if y == 'train':
        # Loading DataFrames
        df_y = pd.read_csv(f'{BUCKET_DATA_PATH}training_solutions_rev1.csv', nrows=nrows)
        df_images =  pd.read_csv(f'{BUCKET_DATA_PATH}images_liste_train.csv', nrows=nrows)

        # Checking images corresponds to df
        list_images = list(df_images['0'])
        df_Galaxy_ID = pd.DataFrame([list_images[i].replace('.jpg','') for i in range(len(list_images))]).rename(columns={0:'GalaxyID'}).astype('int64')
        df = df_y.merge(df_Galaxy_ID, on='GalaxyID', how='inner')

        # Preparing df
        df['image'] = df_images['0']
        df_data = df.drop(columns=['GalaxyID'])

        return df_data

    if y == 'test':
        # Loading DataFrame
        df_y = pd.read_csv(f'{BUCKET_DATA_PATH}central_pixel_benchmark.csv', nrows=nrows)

        # Preparing df
        df_y['image'] = df_y['GalaxyID'].apply(rename)
        df_data = df_y.drop(columns=['GalaxyID'])

        return df_data
    return print("Please provide 'train' or 'test' ")

def get_full_data():
    '''returns a DataFrame with all data'''
    # Loading train
    df_y = pd.read_csv(f'{BUCKET_DATA_PATH}training_solutions_rev1.csv')
    df_images =  pd.read_csv(f'{BUCKET_DATA_PATH}images_liste_train.csv')

    # Checking images corresponds to df
    list_images = list(df_images['0'])
    df_Galaxy_ID = pd.DataFrame([list_images[i].replace('.jpg','') for i in range(len(list_images))]).rename(columns={0:'GalaxyID'}).astype('int64')
    df_train = df_y.merge(df_Galaxy_ID, on='GalaxyID', how='inner')

    # Loading train
    df_test = pd.read_csv(f'{BUCKET_DATA_PATH}central_pixel_benchmark.csv')
    return {'train':df_train, 'test':df_test}

def load_image(image):
    '''returns one image'''
    folder = f'train_bucket/images_traindata_images_train_{image}'
    img = Image.open(folder)
    img_array = np.array(img)
    return np.resize(img_array, (224,224,3))

def load_images(df):
    '''returns array of images'''
    img_list = []
    for _, row in df.iterrows():
        img = load_image(row["image"])
        img_list.append(img)
    return np.stack(img_list)

