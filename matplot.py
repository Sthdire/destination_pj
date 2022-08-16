import matplotlib.pyplot as plt

from db_methods import get_values


def graf_img():
    squares = []
    fig, ax = plt.subplots()

    h = []
    s = 0
    rows = get_values()
    for row in rows:
        h.append(s)
        s += 1
        squares.append(row[3])

    ax.plot(h, squares)
    plt.savefig('static/img/graf', transparent=True)

