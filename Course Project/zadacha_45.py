# Задача 45: оценка на числото π по метода Monte Carlo
import math
import random


def estimate_pi(n_points):
    inside = 0
    for _ in range(n_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / n_points, inside


if __name__ == "__main__":
    print("Брой точки | В кръга | Оценка за π | Грешка")
    for n in [100, 1000, 10000, 100000]:
        random.seed(42)
        pi_estimate, inside = estimate_pi(n)
        error = abs(pi_estimate - math.pi)
        print(f"{n:>10} | {inside:>7} | {pi_estimate:.5f}     | {error:.5f}")
    print("math.pi =", f"{math.pi:.5f}")

    # Същото при 10 различни семена - средна абсолютна грешка
    print()
    print("Средна грешка при 10 различни семена:")
    for n in [100, 1000, 10000, 100000]:
        errors = []
        for seed in range(10):
            random.seed(seed)
            pi_estimate, _ = estimate_pi(n)
            errors.append(abs(pi_estimate - math.pi))
        print(f"{n:>10} | {sum(errors) / len(errors):.5f}")
