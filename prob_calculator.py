import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__ (self, **kwargs):
        contents = []  
        for key, value in kwargs.items():
            for count in range(0, value):
                contents.append(key)
        #print(f"predraw_sc {contents} , ({len(contents)})")

        self.contents = contents
    
    def draw(self, numberDrawing):
        if (numberDrawing >= len(self.contents)):
            return self.contents
        drawnList = []
        for count in range(numberDrawing):
            drawn_ball = random.randint(0, len(self.contents)-1)
            drawnList.append(self.contents.pop(drawn_ball))
        return drawnList
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copy = copy.copy(hat)
    probCount = 0
    for trialTurn in range(num_experiments):
        expDrawnList = copy.deepcopy(hat_copy).draw(num_balls_drawn)
        #print(f'\nexpDrawnList {expDrawnList} ,({len(expDrawnList)})')
        #print('list(expected_balls.keys())', list(expected_balls.keys()))
        for ball in list(expected_balls.keys()):
            actual = expDrawnList.count(ball)
            expected = expected_balls[ball]
            if actual < expected:
                break
        else:
            #print('FOUND THEM ALL!')
            probCount += 1

    #print('\nFINAL_probCount', probCount)
    probabilitly = probCount / num_experiments
    return probabilitly