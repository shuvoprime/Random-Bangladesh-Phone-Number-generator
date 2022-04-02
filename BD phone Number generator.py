
import random
def random_phone_num_generator():
    mno_serial = "011"
    rest = []
    for i in range(1, 9):
        rest.append(random.randint(0, 9))
    return mno_serial + "".join(map(str, rest))
 
while True:
    try:
        n = int(input("HOW MANY PHONE NUMBERS YOU WANT TO GENERATE?:  "))
        break
    except ValueError:
        print("Are you JOKING???  it must be an integer!")

print(" Randomlly Printing "+ str(n) +" numbers which contains unused MNO = 011 ")

for i in range(0,n): 
    print(random_phone_num_generator())