
contacts = {
   'number': 4,
   'students': 
      [
         {'name': 'Sarah Holderness', 'email': 'sarah@exampole.com'},
         {'name': 'Harry Potter', 'email': 'harry@exampole.com'},
         {'name': 'Hermione Granger', 'email': 'hermione@exampole.com'},
         {'name': 'Ron Weasley', 'email': 'ron@exampole.com'}
      ]
}

print("Student emails:")
for student in contacts['students']:
   print(student['email'])

