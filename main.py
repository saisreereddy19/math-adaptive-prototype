import random
import math

class AdaptiveEngine:
    def __init__(self, start_level="Easy"):
        self.difficulty = {"Easy": 1, "Medium": 2, "Hard": 3}[start_level]
        self.levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        self.theta = 0  # learner ability
        self.history = []  # (question, user_answer, correct_answer, is_correct)

    def generate_question(self):
        """Generate a math question based on current difficulty."""
        if self.difficulty == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
        elif self.difficulty == 2:
            a, b = random.randint(10, 50), random.randint(5, 20)
            op = random.choice(["+", "-", "*"])
        else:  # Hard
            a, b = random.randint(10, 100), random.randint(2, 10)
            op = random.choice(["*", "/"])
        question = f"{a} {op} {b}"
        correct = round(eval(question), 2)
        return question, correct

    def update_adaptive_level(self, is_correct):
        """Simple logistic model: adjust difficulty based on performance."""
        if is_correct:
            self.theta += 0.3
        else:
            self.theta -= 0.3

        # Convert theta to difficulty (1–3)
        prob = 1 / (1 + math.exp(-self.theta))
        if prob < 0.4:
            self.difficulty = 1
        elif prob < 0.7:
            self.difficulty = 2
        else:
            self.difficulty = 3

    def add_result(self, q, ans, correct, is_correct):
        self.history.append((q, ans, correct, is_correct))


def main():
    print("Math Adventures AI-Powered Adaptive Learning")
    print("A fun adaptive math practice system for children (ages 5–10)!\n")

    name = input("Enter your name: ").strip()
    print("\nChoose starting difficulty:")
    print("1. Easy\n2. Medium\n3. Hard")
    choice = input("Enter choice (1-3): ").strip()

    levels = {"1": "Easy", "2": "Medium", "3": "Hard"}
    start_level = levels.get(choice, "Easy")

    print(f"\nWelcome {name}! Let's start with {start_level} puzzles 🚀\n")

    engine = AdaptiveEngine(start_level)

    for i in range(10):
        question, correct_answer = engine.generate_question()
        print(f"Q{i+1}: {question}")
        try:
            user_ans = float(input("Your answer: ").strip())
        except ValueError:
            print("Invalid input. Counting as incorrect.\n")
            user_ans = None

        is_correct = user_ans == correct_answer
        engine.add_result(question, user_ans, correct_answer, is_correct)
        engine.update_adaptive_level(is_correct)
        print()  # space between questions

    # Final summary
    correct_count = sum(1 for x in engine.history if x[3])
    total = len(engine.history)
    accuracy = (correct_count / total) * 100
    final_level = engine.levels[engine.difficulty]

    print("\nSession Summary")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {correct_count}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Final Difficulty Reached: {final_level}\n")

    print("Detailed Review:")
    for q, ans, correct, is_correct in engine.history:
        mark = "Correct" if is_correct else "Wrong"
        print(f"{mark} {q} → Your: {ans}, Correct: {correct}")

    if accuracy >= 80:
        print("\n Great job You're mastering this level!")
    elif accuracy >= 50:
        print("\n Good effort Keep practicing Medium-level puzzles.")
    else:
        print("\n Keep going! Try Easy level to build confidence.")


if __name__ == "__main__":
    main()
