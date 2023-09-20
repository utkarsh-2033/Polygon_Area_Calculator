import copy
import random


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls_to_draw):
    num_balls = len(self.contents)
    if num_balls_to_draw >= num_balls:
      drawn_balls = self.contents[:]
      self.contents.clear()
      return drawn_balls
    else:
      drawn_balls = random.sample(self.contents, num_balls_to_draw)
      for ball in drawn_balls:
        self.contents.remove(ball)
      return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successful_experiments = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)

    # Check if the drawn balls match the expected balls
    is_successful = True
    for color, count in expected_balls.items():
      if drawn_balls.count(color) < count:
        is_successful = False
        break

    if is_successful:
      successful_experiments += 1

  probability = successful_experiments / num_experiments
  return probability
