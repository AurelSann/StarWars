from fastapi import FastAPI, File
# import numpy as np
from StarWars.decisiontree import DecisionTree
from StarWars.scientistvalue import HubbleValue
from StarWars.ImagePrediction import ImagePrediction
import tensorflow

model = tensorflow.keras.models.load_model('final_model.h5')

app = FastAPI()

@app.get("/")
def root():
    return "coucou vas voir dans /docs"

@app.post("/uploadfile")
async def create_upload_file(file: bytes = File(...)):
    image_path = "image.png"
    with open(image_path, "wb") as f:
        f.write(file)
    # make prediction
    pred = image_prediction(image_path)
    # decision tree
    result = process_decision_tree(pred)
    # scientific denomination
    denom = process_scientific_denomination(result)
    return {"hubble": denom, "features": result, "pred": list([float(f) for f in pred])}

def image_prediction(image):
    prediction = ImagePrediction(image)
    pred = prediction.prediction
    return pred

def process_decision_tree(pred):
    tree = DecisionTree(pred)
    result = tree.cat1()
    return result

def process_scientific_denomination(result):
    trainer = HubbleValue(result)
    final = trainer.final()
    return final
