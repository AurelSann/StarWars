
from tensorflow import keras
import numpy as np
from PIL import Image

model = keras.models.load_model('final_model.h5')


def image_prediction(image):
    #image = f'{image_path}'
    img = Image.open(image)
    img = np.array(img)
    img = np.resize(img, (224,224,3))
    img = image.reshape(-1,224,224,3) #Reshape de l'image en vecteur de 4 dimensions
    prediction = model.predict(img)#prediction a partir du modele --> vecteur de 37 classes
    prediction = prediction[0] # on récupère le premier element de notre array

    return prediction #On sort la phrase finale : définition de la galaxie et de sa classe de Hubble
