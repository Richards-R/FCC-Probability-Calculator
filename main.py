# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=3, red=4, green=5)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 2},
    num_balls_drawn=7,
    num_experiments=50)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)




















































































