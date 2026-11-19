# Динамична визуализация на метода Monte Carlo (оценка на π)
# Стартиране:  python monte_carlo_visualization.py
# Със запис на GIF и PNG, без прозорец:
#   python monte_carlo_visualization.py --save
import math
import random
import sys

import matplotlib

SAVE = "--save" in sys.argv
if SAVE:
    matplotlib.use("Agg")
    random.seed(42)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

TOTAL_POINTS = 3000
POINTS_PER_FRAME = 30

inside_x, inside_y = [], []
outside_x, outside_y = [], []
history_n, history_pi = [], []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

# Ляв график: квадратът и четвърт кръгът
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_aspect("equal")
arc_x = [math.cos(i * math.pi / 200) for i in range(101)]
arc_y = [math.sin(i * math.pi / 200) for i in range(101)]
ax1.plot(arc_x, arc_y, color="black", linewidth=1.5)
inside_plot, = ax1.plot([], [], "o", color="tab:blue", markersize=3,
                        label="В четвърт кръга")
outside_plot, = ax1.plot([], [], "o", color="tab:red", markersize=3,
                         label="Извън кръга")
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2)
title = ax1.set_title("")

# Десен график: как се променя оценката
ax2.set_xlim(0, TOTAL_POINTS)
ax2.set_ylim(2.6, 3.7)
ax2.axhline(math.pi, color="green", linestyle="--", label="π = 3.14159")
estimate_line, = ax2.plot([], [], color="tab:blue", label="Оценка")
ax2.set_xlabel("Брой точки")
ax2.set_ylabel("Оценка за π")
ax2.legend(loc="upper right")


def init():
    return ()


def update(frame):
    for _ in range(POINTS_PER_FRAME):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    n = len(inside_x) + len(outside_x)
    pi_estimate = 4 * len(inside_x) / n
    history_n.append(n)
    history_pi.append(pi_estimate)

    inside_plot.set_data(inside_x, inside_y)
    outside_plot.set_data(outside_x, outside_y)
    estimate_line.set_data(history_n, history_pi)
    title.set_text(f"Точки: {n}   Оценка: π ≈ {pi_estimate:.4f}")


plt.tight_layout()

animation = FuncAnimation(fig, update, frames=TOTAL_POINTS // POINTS_PER_FRAME,
                          init_func=init, interval=100, repeat=False)

if SAVE:
    animation.save("monte_carlo.gif", writer=PillowWriter(fps=10))
    fig.savefig("monte_carlo_final.png", dpi=150)
    print("Точки:", len(inside_x) + len(outside_x), "Оценка:", history_pi[-1])
else:
    plt.show()
