"""Задача 45: оценяване на π чрез случайни точки."""

import math
import random


def estimate_pi(n, seed=None):
    if n <= 0:
        raise ValueError("Броят точки трябва да е положителен.")

    generator = random.Random(seed)
    inside = 0
    for _ in range(n):
        x = generator.random()
        y = generator.random()
        if x * x + y * y <= 1:
            inside += 1

    return inside, 4 * inside / n


if __name__ == "__main__":
    for n in (100, 1000, 10000, 100000):
        inside, value = estimate_pi(n, seed=42)
        error = abs(value - math.pi)
        print(f"N={n:6d}, K={inside:6d}, "
              f"pi≈{value:.6f}, грешка={error:.6f}")
