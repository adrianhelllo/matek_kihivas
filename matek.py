import random
import time

playing = False
min_operand, max_operand = 2, 12
min_start, max_start = -15, 15
operations = ['+', '-', '*', '/']
op_done = 0
oper_str = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply by',
    '/': 'divide by'}

begin = input("Welcome to my game! I will think of a number, and your task will be to figure out that number from the given operations. Enter anything here when you're ready: ")
playing = True

starting_num = random.randint(min_start, max_start)

def rand_oper(num: int):
    operand = random.randint(min_operand, max_operand)
    current = num
    op_done += 1
    print("Alright, I will think of a number now...")
    print("I have now decided on a number.")

    op = random.choice(operations) 
    current = eval(f"{current} {op} {operand}")

    print(f"{'First' if op_done == 1 else 'Next'} let's {oper_str[op]}")















