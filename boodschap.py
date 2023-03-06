from datetime import datetime

logo = '''
 _        ,
(_\______/________
   \-|-|/|-|-|-|-|/
    \==/-|-|-|-|-/
     \/|_|_|_|_|/
      \__|
       \_|________
        (_)     (_)
'''

braindump = input('Wat heb je allemaal nodig vandaag? ') #Schrijf hier alle producten, gescheiden door een komma

lijst = set()
for item in braindump.split(','):
    lijst.add(item.replace(' ', '').lower())

with open('mijnlijst.txt', "w") as file:
    file.write(logo + '\n')
    file.write('\nBoodschappenlijst:\n')
    for item in lijst:
        file.write(f'- {item.capitalize()}\n')
    file.write(f'\n\nLast updated: {datetime.now()}\n')
    
