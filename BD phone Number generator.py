
import random
def random_phone_num_generator():
    mno_serial = "011"
    rest = []
    for i in range(1, 9):
        rest.append(random.randint(0, 9))
    return mno_serial + "".join(map(str, rest))
 
n = int(input("HOW many numbers to generate?? :  "))
for i in range(0,n):
    print(random_phone_num_generator())

