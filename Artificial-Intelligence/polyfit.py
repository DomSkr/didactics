import numpy
import matplotlib.pyplot as plot

# create random dataset
n_points = 200
x = numpy.random.random(n_points)
y = 2 + 5 * x + numpy.random.random(n_points)

z = numpy.polyfit(x, y, 1)
p = numpy.poly1d(z)
dd = numpy.arange(0, 1, 0.01)
plot.plot(dd, p(dd), 1)

# plot
plot.scatter(x, y, s=10)
plot.xlabel('x')
plot.ylabel('y')
plot.show()
