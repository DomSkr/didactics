from numpy import *
import matplotlib.pyplot as plot


def calculate_error(c, b, a, points):
    error = 0
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        error += (y - (a * x ** 2 + b * x + c)) ** 2
    return error / float(len(points))


def gradient_step(c_current, b_current, a_current, points, learningRate):
    # TODO: implement gradient regression
    new_c = c_current
    new_b = b_current
    new_a = a_current
    return [new_c, new_b, new_a]


def gradient_descent_runner(points, starting_b, starting_a, starting_c, learning_rate, num_iterations):
    c = starting_c
    b = starting_b
    a = starting_a

    dd = arange(0, 100, 0.1)
    p = poly1d([0, 0, 0])

    fig = plot.figure()
    ax = fig.add_subplot(111)

    unzipped = list(zip(*points))

    ax.scatter(list(unzipped[0]), list(unzipped[1]))
    line1, = ax.plot(dd, p(dd), 'r-')

    plot.pause(0.5)
    for i in range(num_iterations):
        c, b, a = gradient_step(c, b, a, array(points), learning_rate)

        line1.set_ydata(poly1d([a, b, c])(dd))
        print(i)
        plot.xlabel('x')
        plot.ylabel('y')
        plot.pause(0.1)
    return [c, b, a]


if __name__ == '__main__':
    n_points = 200
    x = 100 * random.random(n_points)
    y = x ** 2 + 1000 * random.random(n_points)
    points = list(zip(x, y))

    learning_rate = 0.000000001
    num_iterations = 100
    initial_b = 0
    initial_a = 0
    initial_c = 0

    # y=ax^2 + bx + c so initial is y=0

    print("Starting gradient descent at b = {0}, a = {1}, c = {2} error = {3}".format(initial_b, initial_a, initial_c,
                                                                                      calculate_error(initial_c,
                                                                                                      initial_b,
                                                                                                      initial_a,
                                                                                                      points)))
    print("Running...")
    [c, b, a] = gradient_descent_runner(points, initial_b, initial_a, initial_c, learning_rate, num_iterations)
    print("After {0} iterations c = {1}, b = {2}, a = {3}, error = {4}".format(num_iterations, c, b, a,
                                                                               calculate_error(c, b, a, points)))
