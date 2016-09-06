"""pantheon Models."""

import csv


with open('pantheon/pantheon.tsv') as csvfile:
    pantheon_reader = csv.DictReader(csvfile, delimiter= '\t')
    people = [person for person in pantheon_reader]

print(people)

COUNTRY_CODE_TO_COUNTRY = {
        person['countryCode'].upper(): person['countryName'].title()
        for person in people
        if person['countryName'].strip() != ''
    }

COUNTRY_CODE_TO_INDUSTRY = {
    countrycode: sorted(list(set([person['industry'].title()
                           for person in people
                           if person['countryCode'] == countrycode])))
                      for countrycode in COUNTRY_CODE_TO_COUNTRY
    }




# INDUSTRIES_TO_CUR_IDS = {
#     person['industry'].title(): person['en_curid']
#         for person in people
#         if person['industry'].strip() != ''
#     }