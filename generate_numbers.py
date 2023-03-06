import random

def generate_phonenumbers(file_number):

    for _ in range(10):
        
        telefoonnummer = '0'
        for _ in range(0,9):
            if _ == 0:
                telefoonnummer += (str(random.randrange(1, 9)))
            else:
                telefoonnummer += str(random.randrange(0,9))

        with open(f'telefoonnummers/bestand_{file_number}.txt', 'a') as file:
            file.write(telefoonnummer + '\n')

for _ in range(1,10):
    generate_phonenumbers(_)