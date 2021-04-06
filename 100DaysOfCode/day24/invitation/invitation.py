"""pseudo-code:
1. read from a list of people
    iterate over it 
2. replace a specific space holder within a word doc with a name of a person in the list
3. save as a new word document with person name
 

 """

from docx import Document
import csv

# read from csv file and add to a list
people_invited= []
with open('list.csv', 'r', newline='') as csvfile:
    listReader = csv.reader(csvfile, delimiter='\t')
    for row in listReader:
        if 'firstname' not in row:
            row = ' '.join(row)
            people_invited.append(row)
print(people_invited)






# read from docx and replace XXXX
document = Document('starting_letter.docx')
for p in document.paragraphs:
    if 'XXXX' in p.text:
        for name in people_invited:
            ' '.join(name)
            p.text = p.text.replace('XXXX',name)
            document.save(f'Letters/invitation{name}.docx')

