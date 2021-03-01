import numpy as np

class HubbleValue():

    def __init__(self, hubble):
        self.decision_answer = decision_answer

    def final(self, decision_answer):

        hubble = ''

        #Cat 10
        if 'tight' in self.decision_answer:
            hubble = 'Sa/Sb'

        if 'medium' in self.decision_answer:
            hubble = 'Sb/Sc'

        if 'loose' in self.decision_answer:
            hubble = 'Sc/Sd'

        if 'no_bulge2' in self.decision_answer:
            hubble = 'Sc/Sd'

        #Cat 9
        if 'boxy' in self.decision_answer:
            hubble = 'SB'

        if 'rounded' in self.decision_answer:
            hubble = 'S'

        #Cat 7
        if 'completely_round' in self.decision_answer:
            hubble = 'E0-E2'

        if 'in_between' in self.decision_answer:
            hubble = 'E3-E5'

        if 'cigar_shaped' in self.decision_answer:
            hubble = 'E6-E7'

        #Cat 8
        if 'ring' in self.decision_answer:
            hubble = 'ring'

        if 'lens_or_arc' in self.decision_answer:
            hubble = 'lens or an arc'

        if 'disturbed' in self.decision_answer:
            hubble = 'disturbed'

        if 'irregular' in self.decision_answer:
            hubble = 'irregular'

        if 'other' in self.decision_answer:
            hubble = 'irregular'

        if 'merger' in self.decision_answer:
            hubble = 'merger'

        if 'dust_lane' in self.decision_answer:
            hubble = 'dust lane'

        #Cat 5
        if 'no_bulge' in self.decision_answer:
            hubble = 'Sc/Sd'

        if 'bar_yes' and 'arm_no' and 'noticeable_bulge' in self.decision_answer:
            hubble = 'SB0'

        if 'bar_yes' and 'arm_no' and 'obvious_bulge' in self.decision_answer:
            hubble = 'SB0'

        if 'bar_yes' and 'arm_no' and 'dominant_bulge' in self.decision_answer:
            hubble = 'SB0'

        if 'bar_no' and 'arm_no' and 'noticeable_bulge' in self.decision_answer:
            hubble = 'S0'

        if 'bar_no' and 'arm_no' and 'obvious_bulge' in self.decision_answer:
            hubble = 'S0'

        if 'bar_no' and 'arm_no' and 'dominant_bulge' in self.decision_answer:
            hubble = 'S0'

        else:
            f'Send another picture please!'

        return f'This galaxy has the following characteristics: {self.decision_answer}.\
     According to Hubble classification, this would be {hubble} type.'

if __name__ == "__main__":
    decision_answer = ['smooth', 'completely_round', 'odd_yes', 'dust_lane']
    trainer = HubbleValue(decision_answer)
    result = trainer.final()
    print(result)
