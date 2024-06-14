import requests
import json

name = input('Enter the name of animal:\n')   # for example: Lion, Tiger, Elephanth, cheetah
key = 'RJqKfDFaKU8J8iEIfCtGJYIvrUPSvnj2rXSqPlgW'
# url_for_search_Tiger_example = 'https://api.api-ninjas.com/v1/animals?X-Api-Key=RJqKfDFaKU8J8iEIfCtGJYIvrUPSvnj2rXSqPlgW&name=Tiger'
url = 'https://api.api-ninjas.com/v1/animals'


paylaod = {'X-Api-Key': key, 'name' : name}

### first step

response = requests.get(url, params = paylaod)
# print(response.status_code)
# print(response.headers)
# print(response.text)

### second step

jsoned = response.json()
str_jsoned = json.dumps(jsoned, indent=4)

with open('Animal.json', 'w') as file:
    file.write(str_jsoned)


### third step

"""
this code works if animal atribute
is one species of variable name
"""
species = input('Enter the species of your selected animal:\n') # for example: 'Bengal Tiger' or 'Malayan Tiger'
                                                                            #  'Cape Lion' or 'Mountain Lion'                                                                   
def max_speed(animal):                                                      # it depends which animal select you first (line4)
    length = len(jsoned)
    for i in range(length):
        if animal == jsoned[i]['name']:
            return (jsoned[i]['characteristics'].get('top_speed', 'Unknown'))

def average_lifespan(animal):
    length = len(jsoned)
    for i in range(length):
        if animal == jsoned[i]['name']:
            return (jsoned[i]['characteristics'].get('lifespan', 'Unknown'))

print('Max speed:', max_speed(species))
print('lifespan:', average_lifespan(species))



### fourth step

names = []
length = len(jsoned)

for i in range(length):
    names.append(jsoned[i]['name'])


import sqlite3
conn = sqlite3.connect('AnimalData.sqlite')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS species        
               (name VARCHAR(100),
                family VARCHAR(100),
                color VARCHAR(100),
                skin VARCHAR(100),         
                speed VARCHAR(100),
                lifespan VARCHAR(100),
                id INTEGER PRIMARY KEY AUTOINCREMENT
               );''')

"""
I separete
1 column for animal species
5 column for characteristics of animal species
1 column for their ids
"""


for i in names:
    for j in range(length):
        if i == jsoned[j]['name']:
            name = i
            family = jsoned[j]['taxonomy'].get('family', 'Unknown')
            color = jsoned[j]['characteristics'].get('color', 'Unknown')
            skin = jsoned[j]['characteristics'].get('skin_type', 'Unknown')
            speed = jsoned[j]['characteristics'].get('top_speed', 'Unknown')
            lifespan = jsoned[j]['characteristics'].get('lifespan', 'Unknown')
            everything = (name, family, color, skin, speed, lifespan)
            cursor.execute('''INSERT INTO species
                           (name, family, color, skin, speed, lifespan)
                           VALUES (?, ?, ?, ?, ?, ?)''',
                           everything)

"""
as u understand this sql-python code is able to add
animal species general characteristics in database.
"""

conn.commit()
conn.close()

