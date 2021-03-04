import numpy as np
from StarWars.decisiontree import DecisionTree

class HubbleValue():

    def __init__(self, decision_answer):
        self.decision_answer = decision_answer
        self.hubble = ''

    def final(self):


        if 'bar_no' in self.decision_answer and 'arm_no' in self.decision_answer and 'odd_no' in self.decision_answer:
            self.hubble = 'S0'

        elif 'bar_yes' in self.decision_answer and 'arm_yes' in self.decision_answer and 'tight' in self.decision_answer:
            self.hubble = 'SBa/SBb'

        elif 'bar_yes' in self.decision_answer and 'arm_yes' in self.decision_answer and 'medium' in self.decision_answer:
            self.hubble = 'SBb/SBc'

        elif 'bar_yes' in self.decision_answer and 'arm_yes' in self.decision_answer and 'loose' in self.decision_answer:
            self.hubble = 'SBc/SBd'

        elif 'bar_yes' in self.decision_answer and 'arm_no' in self.decision_answer:
            self.hubble = 'SB0'


        elif 'bar_no' in self.decision_answer and 'arm_yes' in self.decision_answer and 'tight' in self.decision_answer:
            self.hubble = 'Sa/Sb'


        elif 'bar_no' in self.decision_answer and 'arm_yes' in self.decision_answer and 'medium' in self.decision_answer:
            self.hubble = 'Sb/Sc'

        elif 'bar_no' in self.decision_answer and 'arm_yes' in self.decision_answer and 'loose' in self.decision_answer:
            self.hubble = 'Sc/Sd'


        elif 'tight' in self.decision_answer:
            self.hubble = 'Sa/Sb'

        elif 'medium' in self.decision_answer:
            self.hubble = 'Sb/Sc'

        elif 'loose' in self.decision_answer:
            self.hubble = 'Sc/Sd'


        #Cat 9
        elif 'boxy' in self.decision_answer:
            self.hubble = 'SB'

        elif 'rounded' in self.decision_answer:
            self.hubble = 'S'

        #Cat 7
        elif 'completely_round' in self.decision_answer:
            self.hubble = 'E0-E2'

        elif 'in_between' in self.decision_answer:
            self.hubble = 'E3-E5'

        elif 'cigar_shaped' in self.decision_answer:
            self.hubble = 'E6-E7'

        #Cat 8
        elif 'ring' in self.decision_answer:
            self.hubble = 'ring'

        elif 'lens_or_arc' in self.decision_answer:
            self.hubble = 'lens or an arc'

        elif 'disturbed' in self.decision_answer:
            self.hubble = 'disturbed'

        elif 'irregular' in self.decision_answer:
            self.hubble = 'irregular'

        elif 'other' in self.decision_answer:
            self.hubble = 'irregular'

        elif 'merger' in self.decision_answer:
            self.hubble = 'merger'

        elif 'dust_lane' in self.decision_answer:
            self.hubble = 'dust lane'


        elif 'no_bulge2' in self.decision_answer:
            self.hubble = 'Sc/Sd'


        else:
            f'Send another picture please, this may not be a galaxy!'

        print(self.decision_answer)
        return self.hubble

if __name__ == "__main__":
    prediction = np.array([0.0061849 , 0.2533387, 0.09984358, 0.00634132, 0.9516694,
       0.31117438, 0.918507952, 0.92126181, 0.801901462, 0.15705012,
       0.19438594, 0.03589064, 0.21429499, 0.078570501, 0.19592663,
       0.2217514 , 0.05080319, 0.03898825, 0.01447876, 0.02751926,
       0.02383724, 0.06303088, 0.04324729, 0.00319327, 0.06603167,
       0.01039219, 0.02341971, 0.08231398, 0.7125346, 0.3151208,
       0.1228107, 0.07996398, 0.01434553, 0.00636853, 0.664883,
       0.        ])
    tree = DecisionTree(prediction)
    result = tree.cat1()
    #decision_answer = ['smooth', 'completely_round', 'odd_yes', 'dust_lane']
    trainer = HubbleValue(result)
    result = trainer.final()
    print(result)
