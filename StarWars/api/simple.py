
from fastapi import FastAPI, File, UploadFile
import numpy as np
from StarWars.decisiontree import DecisionTree
from StarWars.scientistvalue import HubbleValue

app = FastAPI()


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):

    # convert image to array
    file_array = convert(file)

    # make prediction
    pred = make_pred(file_array)

    pred = np.array([0.5061849, 0.02533387, 0.09984358, 0.40634132, 0.09516694,
                     0.31117438, 0.18507952, 0.22126181, 0.01901462, 0.15705012,
                     0.19438594, 0.03589064, 0.21429499, 0.78570501, 0.19592663,
                     0.2217514, 0.05080319, 0.03898825, 0.01447876, 0.02751926,
                     0.02383724, 0.06303088, 0.04324729, 0.00319327, 0.06603167,
                     0.01039219, 0.02341971, 0.08231398, 0.07125346, 0.03151208,
                     0.01228107, 0.07996398, 0.01434553, 0.00636853, 0.00664883,
                     0])

    # decision tree
    result = process_decision_tree(pred)

    # scientific denomination
    denom = process_scientific_denomination(result)

    return {"denom": denom}


def convert(file):
    file_array = "todo"
    return file_array


def make_pred(file_array):
    pred = "todo"
    return pred


def process_decision_tree(pred):
    tree = DecisionTree(pred)
    result = tree.cat1()
    return result


def process_scientific_denomination(result):
    trainer = HubbleValue(result)
    final = trainer.final()
    return final
