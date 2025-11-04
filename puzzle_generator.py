import random

def generate_puzzle(difficulty):
    """Generate a math puzzle based on difficulty level."""
    if difficulty == "Easy":
        num_range = (1, 10)
    elif difficulty == "Medium":
        num_range = (10, 50)
    else:
        num_range = (50, 100)

    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    a = random.randint(*num_range)
    b = random.randint(*num_range)

    # avoid division by zero and ensure divisible numbers
    if op == '/':
        b = random.randint(1, num_range[1])
        a = b * random.randint(1, 10)

    question = f"{a} {op} {b}"
    answer = round(eval(question), 2)
    return question, answer
