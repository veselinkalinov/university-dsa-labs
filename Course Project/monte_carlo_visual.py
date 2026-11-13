"""Самостоятелна динамична демонстрация със стандартния tkinter."""

import random
import tkinter as tk


class MonteCarloDemo:
    def __init__(self, window):
        self.window = window
        self.job = None
        window.title("Monte Carlo — оценяване на π")
        self.canvas = tk.Canvas(window, width=440, height=440,
                                bg="white")
        self.canvas.pack(padx=12, pady=12)
        self.info = tk.Label(window, font=("Arial", 12))
        self.info.pack(pady=6)
        controls = tk.Frame(window)
        controls.pack(pady=10)
        self.step_button = tk.Button(controls, text="Стъпка +100",
                                     command=self.step)
        self.step_button.pack(side=tk.LEFT, padx=4)
        self.auto_button = tk.Button(controls, text="Автоматично",
                                     command=self.toggle)
        self.auto_button.pack(side=tk.LEFT, padx=4)
        tk.Button(controls, text="Ново изпълнение",
                  command=self.reset).pack(side=tk.LEFT, padx=4)
        self.reset()

    def reset(self):
        if self.job is not None:
            self.window.after_cancel(self.job)
        self.job = None
        self.running = False
        self.auto_button.config(text="Автоматично", state=tk.NORMAL)
        self.step_button.config(state=tk.NORMAL)
        self.generator = random.Random(42)
        self.n = 0
        self.inside = 0
        self.canvas.delete("all")
        self.canvas.create_rectangle(20, 20, 420, 420)
        # Центърът на четвърт окръжността е в (20, 420).
        self.canvas.create_arc(-380, 20, 420, 820, start=0,
                               extent=90, style=tk.ARC, width=2)
        self.info.config(text="N=0   K=0   Оценката още не е определена")

    def step(self):
        for _ in range(min(100, 10000 - self.n)):
            x = self.generator.random()
            y = self.generator.random()
            hit = x * x + y * y <= 1
            self.n += 1
            self.inside += int(hit)
            px = 20 + 400 * x
            py = 420 - 400 * y
            color = "#176b8a" if hit else "#b54b35"
            self.canvas.create_oval(px-1, py-1, px+1, py+1,
                                    fill=color, outline="")
        value = 4 * self.inside / self.n
        self.info.config(text=f"N={self.n}   K={self.inside}   π≈{value:.6f}")
        if self.n == 10000:
            self.running = False
            self.auto_button.config(text="Готово", state=tk.DISABLED)
            self.step_button.config(state=tk.DISABLED)

    def tick(self):
        self.job = None
        self.step()
        if self.running:
            self.job = self.window.after(50, self.tick)

    def toggle(self):
        self.running = not self.running
        if self.running:
            self.auto_button.config(text="Пауза")
            self.tick()
        else:
            if self.job is not None:
                self.window.after_cancel(self.job)
            self.job = None
            self.auto_button.config(text="Автоматично")


if __name__ == "__main__":
    window = tk.Tk()
    demo = MonteCarloDemo(window)
    window.mainloop()
