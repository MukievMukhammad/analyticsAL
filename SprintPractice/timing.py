import numpy as np
import matplotlib.pyplot as plt

from sql import sql_query


def plot(x, y):
    fig, ax = plt.subplots()

    ax.bar(x, y)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure

    # plt.show()
    plt.savefig('source/timing6.png')


if __name__ == '__main__':
    result = sql_query("""select time, count(time) from ready_for_analysis group by time;""")

    # plot(np.array([row[0] for row in result]),
    #      np.array([row[1] for row in result]))

    y = [row[1] for row in result]
    x = [row[0] for row in result]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    x = [x[i] for i in range(len(x) - 1)]
    y = [(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]

    print(len(x))
    print(len(y))

    plot(x=np.array([x[i] for i in range(len(x) - 1)]),
         y=np.array([(y[i] + y[i + 1]) / 2 for i in range(len(y) - 1)]))
