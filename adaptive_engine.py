# src/adaptive_engine.py
import random
import math

class AdaptiveEngine:
    def __init__(self, start_level="Easy"):
        # difficulty: 1=Easy, 2=Medium, 3=Hard
        self.levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        self.difficulty = {"Easy": 1, "Medium": 2, "Hard": 3}[start_level]

        # initialize theta near the chosen level so first few updates aren't extreme
        init_theta_map = {"Easy": -0.6, "Medium": 0.0, "Hard": 0.6}
        self.theta = init_theta_map.get(start_level, 0.0)

        self.history = []  # (question, user_answer, correct_answer, is_correct)

        # how much theta changes on correct/incorrect
        self.theta_delta = 0.2  # smaller => less jumpy

    def generate_question(self):
        """Generate a math question based on current difficulty with safer ranges."""
        d = self.difficulty

        if d == 1:  # Easy: +, -, small numbers
            op = random.choice(["+", "-"])
            a, b = random.randint(1, 10), random.randint(1, 10)

        elif d == 2:  # Medium: +, -, * with moderate numbers (restrict multiplication operands)
            op = random.choice(["+", "-", "*"])
            if op == "*":
                a, b = random.randint(2, 12), random.randint(2, 12)   # avoid huge products
            else:
                a, b = random.randint(10, 30), random.randint(1, 20)

        else:  # Hard: larger multiplication & safe division (make divisible)
            op = random.choice(["*", "/"])
            if op == "*":
                a, b = random.randint(10, 50), random.randint(5, 20)
            else:  # division - ensure nicer quotients
                b = random.randint(1, 10)
                q = random.randint(2, 12)
                a = b * q

        question = f"{a} {op} {b}"
        correct = round(eval(question), 2)
        return question, correct

    def update_adaptive_level(self, is_correct):
        """Update theta and convert to difficulty (probability -> level)."""
        if is_correct:
            self.theta += self.theta_delta
        else:
            self.theta -= self.theta_delta

        # map theta to a probability and choose level thresholding
        prob = 1 / (1 + math.exp(-self.theta))

        # thresholds chosen to make changes gradual
        if prob < 0.4:
            self.difficulty = 1
        elif prob < 0.75:
            self.difficulty = 2
        else:
            self.difficulty = 3

    def add_result(self, q, ans, correct, is_correct):
        self.history.append((q, ans, correct, is_correct))

    def get_summary(self):
        total = len(self.history)
        correct_count = sum(1 for x in self.history if x[3])
        accuracy = (correct_count / total) * 100 if total > 0 else 0.0
        final_level = self.levels[self.difficulty]
        return {
            "total": total,
            "correct": correct_count,
            "accuracy": accuracy,
            "final_level": final_level,
            "history": self.history
        }
