import time
import random

ikaw = 'Ikaw: '
ako = 'Ako: '

with open('sagot.txt', 'r') as file:
    sagot = {line.strip() for line in file}

with open('reply.txt', 'r') as file:
    reply = {line.strip() for line in file}


attempt = 0
max_attempts = 3

while attempt < max_attempts:
    attempt += 1
    print(f'{ikaw}Hi')
    user_input = input(f'{ako}')
    
    if user_input.lower() in [r.lower() for r in sagot]:
        time.sleep(2)
        print(f'{ikaw}{random.choice(reply)}')
        break