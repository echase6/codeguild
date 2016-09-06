"""pantheon Logic."""

from . import models

def get_people_by_code_and_industry(code, industry):
    return [
        person
        for person in models.people
        if person['countryCode'].upper() == code and person['industry'].title() == industry
    ]

def get_person_by_cur_id(cur_id):
    for person in models.people:
        if person['en_curid'] == cur_id:
            return person