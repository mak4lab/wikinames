import gzip
from csv import DictReader, DictWriter

languages = input('Which languages should be included in the table? (type language codes separated by commas. See: https://www.wikidata.org/wiki/Help:Wikimedia_language_codes/lists/all)\n').split(',')

languages.sort()
print('Include Languages: ', languages)

output_filename = input("What name should we give the output file?\n")
print("Will save to " + output_filename)

input_file = gzip.open('./wiki_names.csv.gz', mode='rt')
reader = DictReader(input_file)

output_file = open(output_filename, 'w')
writer = DictWriter(output_file, fieldnames=languages)

writer.writeheader()
for row in reader:
    new_row = {}
    for language in languages:
        new_row[language] = row[language]

    writer.writerow(new_row)

input_file.close()
output_file.close()
