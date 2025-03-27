import random
import time

playing = False
MIN_OPERAND, MAX_OPERAND = 2, 12
MIN_START, MAX_START = -15, 15
operations = ['+', '-', '*', '/']
diff = {
    'easy': 5,
    'medium': 6,
    'hard': 8,
    'nightmare': 12
}
op_done = 0
oper_strs = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply by',
    '/': 'divide by'}

begin = input("Welcome to my game! I will think of a number, and your task will be to figure out that number from the given operations. Enter anything here when you're ready: ")
playing = True

starting_num = random.randint(MIN_START, MAX_OPERAND)

def print_decision(operation: str, operand: int, turn: int):
    oper_str = oper_strs[operation]
    
    print(f"{'Next' if turn != 0 else 'First'}, I {oper_str} {operand}.")


def rand_oper(num: int, turn: int) -> int:
    operation = random.choice(operations)
    operand = random.randint(MIN_OPERAND, MAX_START)

    print_decision(operation, operand, turn)

    return eval(f"{num}{operation}{operand}")



def ind_turn():
    user_diff = input("Choose your difficulty // [easy, medium, hard, nightmare]: ")
    
    while user_diff not in diff.keys():
        print("Please enter a valid difficulty.")
        user_diff = input("Choose your difficulty // [easy, medium, hard, nightmare]: ")

    for turn in range(diff[user_diff]):
        if turn == 0:
            turn_res = rand_oper(starting_num, turn)
        else:
            turn_res = rand_oper(turn_res, turn)

    print(f"The result of the operations is {turn_res}. Figure out the original number!")
    return turn_res


def main():
    pass















