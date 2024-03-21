import random

def guess_number():
    """
    Guess the randomly generated number.
    
    Returns:
        int: Number of guesses it took to guess the correct number.
    """
    # 生成一个 1 到 100 之间的随机整数
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# 调用 guess_number 函数开始游戏
guess_number()
