import json

# JSON : Java Script Object Notation

text_file = 'data.txt'
json_file = 'data.json'

list = []

list.append({'vorname': 'Peter', 'nachname': 'Parker'})
list.append({'vorname': 'Bruce', 'nachname': 'Banner'})
list.append({'vorname': 'Carol', 'nachname': 'Danvers'})

# Normalen Text schreiben
def write_data_in_file(data, file):
    with open(file, 'a') as data_file:
        data_file.write(data + '\n')
        data_file.close()

#write_data_in_file('Das ist der Text...', text_file)

# Inhalt der Datei auslesen
def read_data_from_file(file):
    with open(file, 'r') as data_file:
        content = data_file.read()
        data_file.close()
        return content

#print(read_data_from_file(text_file))


# JSON schreiben
def write_json_in_file(data, file):
    with open(file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

#write_json_in_file(list, json_file)

# JSON auslesen
def read_json_from_file(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)
    
data = read_json_from_file(json_file)

for obj in data:
    print(f"{obj['vorname']} {obj['nachname']}")

# JSON-File updaten
data.append({'vorname': 'Natasha', 'nachname': 'Romanov'})
write_json_in_file(data, json_file)
