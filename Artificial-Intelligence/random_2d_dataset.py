import numpy
import matplotlib.pyplot as plot

# create random dataset
n_points = 200
x = numpy.random.random(n_points)
y = 2 + 3 * x + numpy.random.random(n_points)

# plot
plot.scatter(x, y, s=10)
plot.xlabel('x')
plot.ylabel('y')
plot.show()
