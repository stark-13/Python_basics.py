import random

number = random.randint(1,10)
def user_input():
    user = int(input("Enter your answer: "))
    return user

def check():
    if user_input() == number:
        return "Correct Answer"
    else:
        return f"Incorrect Answer. Answer: {number}"

def answer():
    ans = check()
    print(ans)

answer()