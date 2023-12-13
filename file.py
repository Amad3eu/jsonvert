import json
import csv


with open('json.json') as user_file:
  file_contents = user_file.read()
  

parsed_json = json.loads(file_contents)

org = 0
part = 0



with open('organizer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "email", "whatsapp", "ni"]
    writer.writerow(field)


    part = 0
    for i in parsed_json:
        try:
            if int(parsed_json[i]['roles']['isOrganizator']) == 1 and int(parsed_json[i]['status']) == 1:
                name = parsed_json[i]['personalData']['name']
                email = parsed_json[i]['personalData']['email']
                whats = parsed_json[i]['personalData']['whatsapp']
                ni = parsed_json[i]['personalData']['national_identification']
                writer.writerow([name, email, whats, ni])
        except:
            print('oi')


with open('participants.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "email", "whatsapp", "ni"]
    writer.writerow(field)


    part = 0
    for i in parsed_json:
        try:
            if int(parsed_json[i]['roles']['isBuyer']) == 1 and int(parsed_json[i]['status']) == 1:
                name = parsed_json[i]['personalData']['name']
                email = parsed_json[i]['personalData']['email']
                whats = parsed_json[i]['personalData']['whatsapp']
                ni = parsed_json[i]['personalData']['national_identification']
                writer.writerow([name, email, whats, ni])
        except:
            print('oi')