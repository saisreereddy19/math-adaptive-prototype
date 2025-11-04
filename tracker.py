import pandas as pd
import time

class PerformanceTracker:
    def __init__(self):
        self.records = []
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        return round(time.time() - self.start_time, 2)

    def log_result(self, difficulty, correct, response_time):
        self.records.append({
            "difficulty": difficulty,
            "correct": int(correct),
            "response_time": response_time
        })

    def get_summary(self):
        if not self.records:
            return None
        df = pd.DataFrame(self.records)
        accuracy = round(df["correct"].mean() * 100, 2)
        avg_time = round(df["response_time"].mean(), 2)
        return accuracy, avg_time, df
