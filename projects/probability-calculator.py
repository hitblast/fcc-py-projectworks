import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    balls_drawn = []

    if number >= len(self.contents):
      return self.contents

    for i in range(number):
      ball_picked = random.choice(self.contents)
      balls_drawn.append(ball_picked)
      self.contents.pop(self.contents.index(ball_picked))

    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_desired_results = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)

    actual = hat_copy.draw(num_balls_drawn)
    actual_dict = {ball: actual.count(ball) for ball in set(actual)}

    result = True
    for key, value in expected_balls.items():
      if key not in actual_dict or actual_dict[key] < expected_balls[key]:
        result = False
        break

    if result:
      num_desired_results += 1

  return num_desired_results/num_experiments
