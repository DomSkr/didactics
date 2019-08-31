import numpy
import matplotlib.pyplot as plot
from datetime import datetime

# create random numbers generator
seed = int(datetime.now().timestamp())
numpy.random.seed(seed)

# create random dataset
n_points = 200
x = numpy.random.random(n_points)
y = 2 + 3 * x + numpy.random.random(n_points)

# plot
plot.scatter(x, y, s=10)
plot.xlabel('x')
plot.ylabel('y')
plot.show()