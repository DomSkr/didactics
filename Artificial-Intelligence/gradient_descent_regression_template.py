from numpy import *
import matplotlib.pyplot as plot


def calculate_error(b, a, points):
    error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        error += (y - (a * x + b)) ** 2
    return error / float(len(points))


def gradient_step(b_current, a_current, points, learning_rate):
    new_b = b_current
    new_a = a_current

    # TODO: implement gradient step

    return [new_b, new_a]


def gradient_descent_runner(points, starting_b, starting_a, learning_rate, num_iterations):
    b = starting_b
    a = starting_a

    dd = arange(0, 100, 0.1)
    p = poly1d([a, b])

    fig = plot.figure()
    ax = fig.add_subplot(111)
    ax.scatter(points[:, 0], points[:, 1])
    line1, = ax.plot(dd, p(dd), 'r-')

    plot.pause(0.5)
    for i in range(num_iterations):
        b, a = gradient_step(b, a, array(points), learning_rate)

        line1.set_ydata(poly1d([a, b])(dd))
        plot.xlabel('x')
        plot.ylabel('y')
        plot.pause(0.1)
    return [b, a]


if __name__ == '__main__':
    points = genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    num_iterations = 100
    initial_b = 0
    initial_a = 0

    # y=ax+b so initial is y=0

    print("Starting gradient descent at b = {0}, a = {1}, error = {2}"
          .format(initial_b, initial_a, calculate_error(initial_b, initial_a, points)))
    print("Running...")
    [b, a] = gradient_descent_runner(points, initial_b, initial_a, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, a = {2}, error = {3}"
          .format(num_iterations, b, a, calculate_error(b, a, points)))
