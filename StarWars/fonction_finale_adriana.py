import numpy as np

class DecisionTree():

    def __init__(self, prediction):
        self.prediction = prediction
        self.decision_answer = []


    def cat1(self):
        '''cat1 : what does it look like ?'''

        smooth = self.prediction[0]
        #df['Class1.1']

        feature_or_disk = self.prediction[1]
        #df['Class1.2']

        star = self.prediction[2]
        #df['Class1.3']

        if smooth > feature_or_disk:
            #go to cat 7
            self.decision_answer.append('smooth')
            self.cat7()

        elif star > smooth or star > feature_or_disk:
        #STOP --> étoile
            print("c'est une étoile")

        else:
        #feature_or_disk > all:
            #go to class 2
            self.decision_answer.append('feature_or_disk')
            self.cat2()

        return self.decision_answer

    def cat2(self):
        '''cat2 : featureordisk --> could this be a disk view edge-on ?'''

        edgeon_yes = self.prediction[3]
        #df['Class2.1']
        edgeon_no = self.prediction[4]
        #df['Class2.2']

        if edgeon_yes > edgeon_no:
            #go to cat 9
            self.decision_answer.append('edgeon_yes')
            self.cat9()

        else:
            #edgeon_no> edgeon_yes
            self.decision_answer.append('edgeon_no')
            #go to cat 3
            self.cat3()

        return self.decision_answer


    def cat3(self):
        '''cat 3 : featureordisk --> edgeon_no --> is there a sign of bar feature ?'''

        bar_yes = self.prediction[5]
        #df['Class3.1']
        bar_no = self.prediction[6]
        #df['Class3.2']

        #all : go to cat 4
        if bar_yes > bar_no:
            self.decision_answer.append('bar_yes')
            self.cat4()

        else:
            #bar_no > bar_yes
            self.decision_answer.append('bar_no')
            self.cat4()

        return self.decision_answer



    def cat4(self):
        '''cat4 : featureordisk --> no --> bar_yes/no --> spiral arm pattern ?'''

        arm_yes = self.prediction[7]
        #df['Class4.1']
        arm_no = self.prediction[8]
        #df['Class4.2']

        if arm_yes > arm_no:
            #go to cat10
            self.decision_answer.append('arm_yes')
            self.cat10()

        else:
            #arm_yes > arm_no
            self.decision_answer.append('arm_no')
            #go to cat5
            self.cat5()

        return self.decision_answer


    def cat5(self):
        '''cat5 : prominence of central buldge ?
    featureordisk --> edgeon_no --> bar_yes/no --> arm_no
    featureordisk --> edgeon_no --> --> bar_yes/no --> arm_yes --> all arms sizes --> all number of arms'''

        no_bulge = self.prediction[9]
        #df['Class5.1']
        noticeable_bulge = self.prediction[10]
        #df['Class5.2']
        obvious_bulge = self.prediction[11]
        #df['Class5.3']
        dominant_bulge = self.prediction[12]
        #df['Class5.4']

    #all: go to cat 6
        if no_bulge > noticeable_bulge and no_bulge > obvious_bulge and no_bulge > dominant_bulge:
            self.decision_answer.append('no_bulge')
            self.cat6()

        elif noticeable_bulge > no_bulge and noticeable_bulge > obvious_bulge and noticeable_bulge > dominant_bulge:
            self.decision_answer.append('noticeable_bulge')
            self.cat6()

        elif obvious_bulge > no_bulge and obvious_bulge > noticeable_bulge and obvious_bulge > dominant_bulge:
            self.decision_answer.append('obvious_bulge')
            self.cat6()

        else:
            #dominant_bulge > all
            self.decision_answer.append('dominant_bulge')
            self.cat6()


        return self.decision_answer


    def cat6(self):
        '''cat6 - is there anything odd ?
    #featureordisk --> edgeon_no --> bar_yes/no --> arm_no --> all
    #Smooth --> class 7 : all
    #featureordisk --> edgeon_yes --> class 9 :all'''

        odd_yes = self.prediction[13]
        #df['Class6.1']
        odd_no = self.prediction[14]
        #df['Class6.2']

        if odd_yes > odd_no:
            #go to cat 8
            self.decision_answer.append('odd_yes')
            self.cat8()

        else:
            self.decision_answer.append('odd_no')
            #stop

        return self.decision_answer

    '''DEUXIEME CHEMIN'''

    def cat7(self):
        #cat7 : Smooth - how rounded is it ?
        completely_round = self.prediction[15]
        #df['Class7.1']
        in_between = self.prediction[16]
        #df['Class7.2']
        cigar_shaped = self.prediction[17]
        #df['Class7.3']

    #all: go to cat6
        if completely_round > in_between and completely_round > cigar_shaped:
            self.decision_answer.append('completely_round')
            self.cat6()

        elif in_between > completely_round and in_between > cigar_shaped:
            self.decision_answer.append('in_between')
            self.cat6()

        else:
            #cigar_shaped > all
            self.decision_answer.append('cigar_shaped')
            self.cat6()

        return self.decision_answer


    def cat8(self):
        #cat8 : featureordisk --> edgeon_no --> bar_yes/no --> arm_no --> all --> odd_yes --> ring,
        #disturber or irregular ?

        ring = self.prediction[18]
        #df['Class8.1']
        lens_or_arc = self.prediction[19]
        #df['Class8.2']
        disturbed = self.prediction[20]
        #df['Class8.3']
        irregular = self.prediction[21]
        #df['Class8.4']
        other = self.prediction[22]
        #df['Class8.5']
        merger = self.prediction[23]
        #df['Class8.6']
        dust_lane = self.prediction[24]
        #df['Class8.7']

        #all: stop
        if ring > lens_or_arc and ring > disturbed and ring > irregular and ring > other and ring > merger and ring > dust_lane:
            self.decision_answer.append('ring')
            #stop

        elif lens_or_arc > ring and lens_or_arc > disturbed and lens_or_arc > irregular and lens_or_arc > other and lens_or_arc > merger and lens_or_arc > dust_lane:
            self.decision_answer.append('lens_or_arc')
            #stop

        elif disturbed > lens_or_arc and disturbed > ring and disturbed > irregular and disturbed > other and disturbed > merger and disturbed > dust_lane:
            self.decision_answer.append('disturbed')
            #stop

        elif irregular > lens_or_arc and irregular > disturbed and irregular > ring and irregular > other and irregular > merger and irregular > dust_lane:
            self.decision_answer.append('irregular')
            #stop

        elif other > lens_or_arc and other > disturbed and other > irregular and other > ring and other > merger and other > dust_lane:
            self.decision_answer.append('other')
            #stop

        elif merger > lens_or_arc and merger > disturbed and merger > irregular and merger > other and merger > ring and merger > dust_lane:
            self.decision_answer.append('merger')
            #stop

        else:
            #dust_lane > all
            self.decision_answer.append('dust_lane')
            #stop
        return self.decision_answer



    def cat9(self):
        #cat9 : featureordisk --> edgeon_yes --> if there a bulge, if yes what shape ?

        rounded = self.prediction[25]
        #df['Class9.1']
        boxy = self.prediction[26]
        #df['Class9.2']
        no_bulge2 = self.prediction[27]
        #df['Class9.3']

    # all: go to cat6
        if rounded > boxy and rounded > no_bulge2:
            self.decision_answer.append('rounded')
            self.cat6()

        elif boxy > rounded and boxy > no_bulge2:
            self.decision_answer.append('boxy')
            self.cat6()

        else:
            #no_bulge2 > all
            self.decision_answer.append('no_bulge2')
            self.cat6()

        return self.decision_answer



    def cat10(self):
        #cat10 : featureordisk --> edgeon_no --> bar_yes/no --> arm_yes --> how tights are the arms ?

        tight = self.prediction[28]
        #df['Class10.1']
        medium = self.prediction[29]
        #df['Class10.2']
        loose = self.prediction[30]
        #df['Class10.3']

    #all: go to cat 11
        if tight > medium and tight > loose:
            self.decision_answer.append('tight')
            #cat11()

        elif medium > tight and medium > loose:
            self.decision_answer.append('medium')
            #cat11()

        else:
            #loose > all
            self.decision_answer.append('loose')
            #cat11()

        return self.decision_answer



    def cat11(self):
    #cat 11: featureordisk --> edgeon_no --> bar_yes/no --> arm_yes --> all arms sizes --> how many arms ?

        one_arm = self.prediction[31]
        #df['Class11.1']
        two_arms = self.prediction[32]
        #df['Class11.2']
        three_arms = self.prediction[33]
        #df['Class11.3']
        four_arms = self.prediction[34]
        #df['Class11.4']
        more_than_four_arms = self.prediction[35]
        #df['Class11.5']
        cant_tell_arms = self.prediction[36]
        #df['Class11.6']

    #all: go to cat5
        if one_arm > two_arms and one_arm > three_arms and one_arm > four_arms and one_arm > more_than_four_arms and one_arm > cant_tell_arms:
            self.decision_answer.append('one_arm')
            self.cat5()

        elif two_arms > one_arm and two_arms > three_arms and two_arms > four_arms and two_arms > more_than_four_arms and two_arms > cant_tell_arms:
            self.decision_answer.append('two_arms')
            self.cat5()

        elif three_arms > one_arm and three_arms > two_arms and three_arms > four_arms and three_arms > more_than_four_arms and three_arms > cant_tell_arms:
            self.decision_answer.append('three_arms')
            self.cat5()

        elif four_arms > one_arm and four_arms > three_arms and four_arms > two_arms and four_arms > more_than_four_arms and four_arms > cant_tell_arms:
            self.decision_answer.append('four_arms')
            self.cat5()

        elif more_than_four_arms > one_arm and more_than_four_arms > three_arms and more_than_four_arms > four_arms and more_than_four_arms > two_arms and more_than_four_arms > cant_tell_arms:
            self.decision_answer.append('more_than_four_arms')
            self.cat5()

        else:
            #cant_tell_arms > all
            self.decision_answer.append('cant_tell_arms')
            self.cat5()


        return self.decision_answer

if __name__ == "__main__":
    prediction = np.array([0.5061849 , 0.02533387, 0.09984358, 0.40634132, 0.09516694,
       0.31117438, 0.18507952, 0.22126181, 0.01901462, 0.15705012,
       0.19438594, 0.03589064, 0.21429499, 0.78570501, 0.19592663,
       0.2217514 , 0.05080319, 0.03898825, 0.01447876, 0.02751926,
       0.02383724, 0.06303088, 0.04324729, 0.00319327, 0.06603167,
       0.01039219, 0.02341971, 0.08231398, 0.07125346, 0.03151208,
       0.01228107, 0.07996398, 0.01434553, 0.00636853, 0.00664883,
       0.        ])
    trainer = DecisionTree(prediction)
    result = trainer.cat1()
    print(result)
