import copy
import random

class Hat() :
    def __init__(self, **balls) :
        self.balls = balls

        self.contents = []
        for ball, numbers in self.balls.items() :
            self.contents.extend(ball for i in range(numbers))
        

    def draw(self, how_many) :
        draw_result = []
        for ball in range(how_many) :
            try :
                b = self.contents.pop(random.randint(0, len(self.contents)-1))
            except :
                continue
            draw_result.append(b)
        print('balls drawn', draw_result)
        return draw_result
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :
    success = 0
    # po wykonaniu każdego eksperymentu hat powinien wrócić do stanu z przed eksperymentu
    
    hat_copy = copy.deepcopy(hat)
    for i in range(num_experiments) :
        
        drawned_balls = hat.draw(num_balls_drawn)

        part_success = 0
        
        for color, number in expected_balls.items() :

            if drawned_balls.count(color) >= number :
                part_success += 1
        
        if part_success == len(expected_balls) :
            success +=1
        
        hat = copy.deepcopy(hat_copy)
        print('hat_co po eksp',hat_copy.contents)
    print(success)
    print('red', drawned_balls.count('red'))
    print('green', drawned_balls.count('green'))
    try :
        probability = success / num_experiments
        print(probability)

        return probability
    except ZeroDivisionError :
        probability = 0
        print(probability)
        return probability
    

hat = Hat(black=6, red=4, green=3)

experiment(hat=hat, expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=500)

#hat.draw(5)


