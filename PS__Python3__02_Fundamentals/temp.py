
acronym = input("What acronym do yo want to add?\n")
defintion = input("What is the definition?\n")
with open('./software_acronyms.txt', 'a') as file:
   file.write(acronym + " - " + defintion + "\n")
   