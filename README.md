# 🧮 Math Adventures — AI-Powered Adaptive Learning Prototype

An AI-powered adaptive math learning prototype designed for children (ages 5–10).  
It helps learners practice basic math operations — addition, subtraction, multiplication, and division — while **dynamically adjusting the difficulty** based on performance.

---

## 🎯 Objective
To demonstrate how adaptive learning systems personalize educational content using simple machine learning logic.  
This prototype adjusts puzzle difficulty automatically to maintain an optimal challenge level for each learner.

---

## 🧠 Core Features
- **Four math operations**: Addition, Subtraction, Multiplication, Division  
- **Adaptive difficulty engine** using lightweight ML logic (logistic-style learning model)  
- **Automatic tracking** of correctness and performance  
- **Dynamic question generation** across 3 levels: Easy, Medium, Hard  
- **Session summary** showing accuracy and final level after 10 questions  

---

## 🧩 Folder Structure
math-adaptive-prototype/
│
├── README.md
├── requirements.txt
└── src/
├── main.py
├── adaptive_engine.py
├── puzzle_generator.py
└── tracker.py

---

## ⚙️ Installation & Running

### 1. Clone Repository
```bash
git clone https:/saisreereddy19/github.com//math-adaptive-prototype.git
cd math-adaptive-prototype

pip install -r requirements.txt

python main.py

🧮 Math Adventures — AI-Powered Adaptive Learning

Enter your name: Teena
Choose starting difficulty:
1. Easy
2. Medium
3. Hard
Enter choice (1-3): 1

Welcome Teena! Let's start with Easy puzzles 🚀

Q: 5 + 3
Your answer: 8
✅ Correct!

Q: 9 - 2
Your answer: 7
✅ Correct!

... (continues up to 10 questions)

📊 Session Summary
Total Questions: 10
Correct Answers: 8
Accuracy: 80.00%
Final Difficulty Reached: Medium

Adaptive Logic Summary

A logistic-style adaptive model tracks a “skill score” (θ).
Each correct answer increases θ, and incorrect decreases it slightly.
Difficulty transitions happen when θ crosses thresholds:

Probability Range	Difficulty
< 0.4	Easy
0.4 – 0.75	Medium
> 0.75	Hard

This makes progression gradual and keeps learners in their comfort-challenge balance.
