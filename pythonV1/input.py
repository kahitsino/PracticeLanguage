import time
import random

ikaw = 'Ikaw: '
ako = 'Ako: '

# Para sa Maraming Sagot Loop One
with open('sagot/sagot.txt', 'r') as file:
	sagot = [line.strip() for line in file]

# Para sa Maraming Sagot Loop Two
with open('sagot/sagot2.txt', 'r') as file:
	sagot2 = [line.strip() for line in file]

# Para sa Random na Reply Loop One
with open('reply/reply.txt', 'r') as file:
	reply = [line.strip() for line in file]

# Random Print sa Unahan
with open('reply/random_print.txt') as file:
	random_print = [line.strip() for line in file]



while True:
    print(f'{ikaw}{random.choice(random_print)}')
    txt = input(f'{ako}')
    
    if txt.lower() in [r.lower() for r in sagot]:
	    time.sleep(2)
	    print(f'{ikaw}{random.choice(reply)}')
	    break


while True:
    txt = input(f'{ako}')
    
    if txt.lower() in [r.lower() for r in sagot2]:
    	time.sleep(2)
    	print(f'{ikaw}Ah..')
    	break
