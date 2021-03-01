import numpy as np
from StarWars.decisiontree import DecisionTree

class HubbleValue():

    def __init__(self, decision_answer):
        self.decision_answer = decision_answer
        self.hubble = ''

    def final(self):

        #Cat 10
        if 'tight' in self.decision_answer:
            self.hubble = 'Sa/Sb'

        if 'medium' in self.decision_answer:
            self.hubble = 'Sb/Sc'

        if 'loose' in self.decision_answer:
            self.hubble = 'Sc/Sd'

        if 'no_bulge2' in self.decision_answer:
            self.hubble = 'Sc/Sd'

        #Cat 9
        if 'boxy' in self.decision_answer:
            self.hubble = 'SB'

        if 'rounded' in self.decision_answer:
            self.hubble = 'S'

        #Cat 7
        if 'completely_round' in self.decision_answer:
            self.hubble = 'E0-E2'

        if 'in_between' in self.decision_answer:
            self.hubble = 'E3-E5'

        if 'cigar_shaped' in self.decision_answer:
            self.hubble = 'E6-E7'

        #Cat 8
        if 'ring' in self.decision_answer:
            self.hubble = 'ring'

        if 'lens_or_arc' in self.decision_answer:
            self.hubble = 'lens or an arc'

        if 'disturbed' in self.decision_answer:
            self.hubble = 'disturbed'

        if 'irregular' in self.decision_answer:
            self.hubble = 'irregular'

        if 'other' in self.decision_answer:
            self.hubble = 'irregular'

        if 'merger' in self.decision_answer:
            self.hubble = 'merger'

        if 'dust_lane' in self.decision_answer:
            self.hubble = 'dust lane'

        #Cat 5
        if 'no_bulge' in self.decision_answer:
            self.hubble = 'Sc/Sd'

        if 'bar_yes' and 'arm_no' and 'noticeable_bulge' in self.decision_answer:
            self.hubble = 'SB0'

        if 'bar_yes' and 'arm_no' and 'obvious_bulge' in self.decision_answer:
            self.hubble = 'SB0'

        if 'bar_yes' and 'arm_no' and 'dominant_bulge' in self.decision_answer:
            self.hubble = 'SB0'

        if 'bar_no' and 'arm_no' and 'noticeable_bulge' in self.decision_answer:
            self.hubble = 'S0'

        if 'bar_no' and 'arm_no' and 'obvious_bulge' in self.decision_answer:
            self.hubble = 'S0'

        if 'bar_no' and 'arm_no' and 'dominant_bulge' in self.decision_answer:
            self.hubble = 'S0'

        else:
            f'Send another picture please, this may not be a galaxy!'

        return f'This galaxy has the following characteristics: {self.decision_answer}.\
     According to Hubble classification, this would be {self.hubble} type.'

if __name__ == "__main__":
    prediction = np.array([0.5061849 , 0.02533387, 0.09984358, 0.40634132, 0.09516694,
       0.31117438, 0.18507952, 0.22126181, 0.01901462, 0.15705012,
       0.19438594, 0.03589064, 0.21429499, 0.78570501, 0.19592663,
       0.2217514 , 0.05080319, 0.03898825, 0.01447876, 0.02751926,
       0.02383724, 0.06303088, 0.04324729, 0.00319327, 0.06603167,
       0.01039219, 0.02341971, 0.08231398, 0.07125346, 0.03151208,
       0.01228107, 0.07996398, 0.01434553, 0.00636853, 0.00664883,
       0.        ])
    tree = DecisionTree(prediction)
    result = tree.cat1()
    #decision_answer = ['smooth', 'completely_round', 'odd_yes', 'dust_lane']
    trainer = HubbleValue(result)
    result = trainer.final()
    print(result)
