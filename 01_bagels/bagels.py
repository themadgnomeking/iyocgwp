#! python3
import random

from numpy import mat

# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues
# The game offers one of the following hints in response to your guess: 
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place 
# “Bagels” if your guess has no correct digits. 
# You have 10 tries to guess the secret number.

#num_to_guess = str(num1) + str(num2) + str(num3)
num_to_guess = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

test_num = input("pick your 3 digit number: ")

guess_result = ''

pico_count = 0
fermi_count = 0
bagels_count = 0

while test_num != num_to_guess:

    count = 0
    num_count = -1
    for i in num_to_guess:
        num_count += 1
        for j in test_num:
            if count <= 2:
                if num_count == 0:
                    if count == 0 and i == j:
                        pico_count += 1
                    elif (count == 1 and i == j) or (count == 2 and i == j):
                        fermi_count += 1
                    else:
                        bagels_count += 1
                if num_count == 1:
                    if count == 1 and i == j:
                        pico_count += 1
                    elif (count == 0 and i == j) or (count == 2 and i == j):
                        fermi_count += 1
                    else:
                        bagels_count += 1
                if num_count == 2:
                    if count == 2 and i == j:
                        pico_count += 1
                    elif (count == 0 and i == j) or (count == 1 and i == j):
                        fermi_count += 1
                    else:
                        bagels_count += 1 
                count +=1   
            if count >= 3:
                count = 0

  

                
            

print("random number: " + num_to_guess)
print("player number: " + test_num)
print("Pico Count: " + str(pico_count))
print("Fermi Count: " + str(fermi_count))
print("Bagel Count: " + str(bagels_count))
