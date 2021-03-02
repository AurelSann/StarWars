
from tensorflow import keras
import numpy as np
from PIL import Image

model = keras.models.load_model('final_model.h5')


class ImagePrediction():
    def __init__(self, image):
        self.image = image
        self.open = Image.open(self.image)
        self.array = np.array(self.open)
        self.resize = np.resize(self.array, (224, 224, 3))
        self.reshape = self.resize.reshape(-1, 224, 224, 3)  #Reshape de l'image en vecteur de 4 dimensions
        self.prediction = model.predict(self.reshape)[0]  #prediction a partir du modele --> vecteur de 37 classes
