"""Rain database processor.

Accesses City of Portland rain total database and returns various information
about rain totals.
"""
from operator import itemgetter

def get_filename():
    """Return the filename of the database."""
    return 'sunnyside.rain'


def get_daily_totals(filename):
    """Return a list of days and daily amounts, as rows from the file."""
    totals = []
    with open(filename) as f:
        for i in range(11):
            ignored_line = f.readline()
        for line in f:
            day_stats = line.split()[0:2]
            if day_stats[1] != '-':  # remove entries where there is missing data
                totals += [[day_stats[0], int(day_stats[1])]]
    return totals


def find_wettest_stats(totals):
    """Return wettest day (or year) and the amount on the wettest day (or year).

    >>> find_wettest_stats([['30-MAR-2016', 0], ['29-MAR-2016', 5]])
    ('29-MAR-2016', 5)
    """
    amounts = [i[1] for i in totals]
    max_amount = max(amounts)
    max_index = amounts.index(max_amount)
    day_max_amount = totals[max_index][0]
    return day_max_amount, max_amount


def calc_yearly_total_stats(totals):
    """Return a list of lists of years and sum amounts.

    >>> calc_yearly_total_stats([['30-MAR-2016', 1], ['29-MAR-2016', 5], ['30-MAR-2015', 0], ['29-MAR-2015', 5]])
    [['2015', 5], ['2016', 6]]
    """
    years = set()
    yearly_totals = []
    for date, amount in totals:
        year = date.split('-')[2]
        years.add(year)
    for year in years:
        yearly_totals += [[year, sum([amt for date, amt in totals
                                   if date.split('-')[2] == year])]]
    return sorted(yearly_totals)  # sorted only to make the doctest work


def find_daily_avg(totals):
    days = set()
    daily_avg = []
    for date, amount in totals:
        day = '-'.join(date.split('-')[0:2])
        days.add(day)
    daily_avg = []
    for day in days:
        daily_stats = ([amt for date, amt in totals
                         if '-'.join(date.split('-')[0:2]) == day])
        daily_avg += [[day, (sum(daily_stats) / len(daily_stats))]]
    return sorted(daily_avg, key=itemgetter(1), reverse = True)


def find_wettest_doy(averages):
    return sorted(averages, key=itemgetter(1), reverse = True)[0]


def find_avg_amt_on_day(date, averages):
    averages_dict = dict(averages)
    return averages_dict[date]


def get_inquiry_date():
    return input('What date would you like to check (DD=MMM): ')


def output_most_rain_stats(day, day_amt, year, year_amt):
    print('Wettest day was {}, amount was {}"'.format(day, day_amt/100))
    print('Wettest year was {}, amount was {}"'.format(year, year_amt/100))
    return


def main():
    filename = get_filename()
    daily_totals = get_daily_totals(filename)
    wettest_day, wettest_day_amt = find_wettest_stats(daily_totals)
    yearly_totals = calc_yearly_total_stats(daily_totals)
    wettest_year, wettest_year_amt = find_wettest_stats(yearly_totals)
    daily_averages = find_daily_avg(daily_totals)
    wettest_doy = find_wettest_doy(daily_averages)
    print('Wettest day of the year is {} with {:.2f}"'.format(wettest_doy[0], wettest_doy[1] / 100))
    inquiry_date = get_inquiry_date()
    avg_amt_on_day = find_avg_amt_on_day(inquiry_date, daily_averages)
    print('Average rainfall on {} is {:.2f}"'.format(inquiry_date, avg_amt_on_day / 100))
    output_most_rain_stats(wettest_day, wettest_day_amt, wettest_year, wettest_year_amt)
    return


if __name__ == '__main__':
   main()
