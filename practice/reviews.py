"""" Reviews"""

import json
import statistics

def gather_user_input():
    """Get business name, user name, and user city from a user"""
    # business_name = input('Which business would you like to return all reviews for?')
    # user_name = input('Which user would you like to return all reviews for?')
    # city_name = input('Which city would you like to return the average score for?')
    business_name = 'Voodoo Donuts'
    user_name = 'Bobby'
    city_name = 'Portland'
    return business_name, user_name, city_name

def import_file(file):
    """Import file into lines."""
    with open(file) as f:
        input_file = f.readlines()
    return [json.loads(line) for line in input_file]


def import_from_json():
    """Imports a json file and converts it to python
    """
    business_data = import_file('business_data.txt')
    user_data = import_file('user_data.txt')
    review_data = import_file('review_data.txt')
    return business_data, user_data, review_data


def return_reviews_for_business(reviews_data, company_name):
    """Return all the reviews for a selected business."""
    reviews_list = [review for review in reviews_data if company_name == review['business_name']]
    return reviews_list


def return_reviews_from_user(reviews_data, user_name):
    """Return all the reviews from a selected user."""
    reviews_list = [review for review in reviews_data if user_name == review['user_name']]
    return reviews_list

def print_table(table_to_print, field):
    """Prints a list of dictionaries"""
    for item in table_to_print:
        for j in field:
            print(item[j], end='  ')
        print()


def return_mean_rating_for_business(reviews_data, company_name):
    """Return mean rating for a selected business."""
    reviews_list = return_reviews_for_business(reviews_data, company_name)
    score_list = [review['rating'] for review in reviews_list]
    mean_rating = statistics.mean(score_list)
    return mean_rating


def return_users_from_city(user_data, city_name):
    """Returns the names of all users in a given city"""
    return [user['user_name'] for user in user_data if city_name == user['hometown']]


def return_mean_review_from_city(user_data, review_data, city_name):
    """Return mean review for all users from a particular city."""
    users_in_city = return_users_from_city(user_data, city_name)
    score_list = [review['rating'] for review in review_data if review['user_name'] in users_in_city]
    return statistics.mean(score_list)


def main():
    business_data, user_data, review_data = import_from_json()
    business_name, user_name, city_name = gather_user_input()
    reviews_for_business = return_reviews_for_business(review_data, business_name)
    print_table(reviews_for_business, ['user_name', 'rating', 'text'])
    mean_rating = return_mean_rating_for_business(review_data, business_name)
    reviews_from_user = return_reviews_from_user(review_data, user_name)
    print_table(reviews_from_user, ['user_name', 'rating', 'text'])
    mean_rating_from_city = return_mean_review_from_city(user_data, review_data, city_name)
    print('Mean rating for {} {:.2f}'.format(user_name, mean_rating))
    print('Mean rating for {} {:.2f}'.format(city_name, mean_rating_from_city))


if __name__ == '__main__':
    main()