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
            if day_stats[1] != '-':  # skip entries if there is missing data
                totals += [[day_stats[0], int(day_stats[1])]]
    return totals


def find_wettest_stats(totals):
    """Return wettest day (or year) and the amount on the wettest day (or year).

    >>> find_wettest_stats([['30-MAR-2016', 0], ['29-MAR-2016', 5]])
    ['29-MAR-2016', 5]
    """
    return max(totals, key=itemgetter(1))


def calc_yearly_total_stats(totals):
    """Return a list of lists of years and sum amounts.

    >>> calc_yearly_total_stats([['30-MAR-2016', 1], ['29-MAR-2016', 5],
    ...                         ['30-MAR-2015', 0], ['29-MAR-2015', 5]])
    [['2015', 5], ['2016', 6]]
    """
    years = set()
    for date, amount in totals:
        year = date.split('-')[2]
        years.add(year)
    yearly_totals = []
    for year in years:
        yearly_totals += [[year, sum([amt for date, amt in totals
                                   if date.split('-')[2] == year])]]
    return sorted(yearly_totals)  # sorted only to make the doctest work


def calc_daily_avg_stats(totals):
    """Return a list of lists of days and average amounts.

    >>> calc_daily_avg_stats([['30-MAR-2016', 1], ['29-MAR-2016', 5],
    ...                      ['30-MAR-2015', 3], ['29-MAR-2015', 3]])
    [['29-MAR', 4.0], ['30-MAR', 2.0]]
    """
    days = set()
    for date, amount in totals:
        day = '-'.join(date.split('-')[0:2])
        days.add(day)
    daily_avg = []
    for day in days:
        daily_stats = ([amt for date, amt in totals
                         if '-'.join(date.split('-')[0:2]) == day])
        daily_avg += [[day, (sum(daily_stats) / len(daily_stats))]]
    return sorted(daily_avg, key=itemgetter(1), reverse = True)


def find_avg_amt_on_day(date, averages):
    """Return the amount associated with a particular day from a list.

    >>> find_avg_amt_on_day('29-MAR', [['30-MAR', 1.0], ['29-MAR', 5.0]])
    5.0
    """
    averages_dict = dict(averages)
    return averages_dict[date]


def get_inquiry_date():
    """Return the user's selection of a date for subsequent inquiry."""
    return input('What date would you like to check (DD=MMM): ')


def output_most_rain_stats(day, day_amt, year, year_amt):
    """Print the wettest day and year statistics.

    >>> output_most_rain_stats('29-MAR-2015', 25, '2012', 5520)
    Wettest day was 29-MAR-2015, amount was 0.25"
    Wettest year was 2012, amount was 55.2"
    """
    print('Wettest day was {}, amount was {}"'.format(day, day_amt/100))
    print('Wettest year was {}, amount was {}"'.format(year, year_amt/100))
    return


def output_wettest_doy_stats(day, amt):
    """Print the wettest day of the year amount

    >>> output_wettest_doy_stats('29-MAR', 25)
    Wettest day of the year is 29-MAR with 0.25"
    """
    print('Wettest day of the year is {} with {:.2f}"'.format(day, amt / 100))
    return


def output_inquiry_stats(date, amt):
    """Print the average amount for a requested day of year

    >>> output_inquiry_stats('29-MAR', 25)
    Average rainfall on 29-MAR is 0.25"
    """
    print('Average rainfall on {} is {:.2f}"'.format(date, amt / 100))
    return


def main():
    filename = get_filename()
    daily_totals = get_daily_totals(filename)
    wtst_day, wtst_day_amt = find_wettest_stats(daily_totals)
    yearly_totals = calc_yearly_total_stats(daily_totals)
    wtst_year, wtst_year_amt = find_wettest_stats(yearly_totals)
    output_most_rain_stats(wtst_day, wtst_day_amt, wtst_year, wtst_year_amt)
    daily_averages = calc_daily_avg_stats(daily_totals)
    wettest_doy, wettest_doy_amt = find_wettest_stats(daily_averages)
    output_wettest_doy_stats(wettest_doy, wettest_doy_amt)
    inquiry_date = get_inquiry_date()
    avg_amt_on_day = find_avg_amt_on_day(inquiry_date, daily_averages)
    output_inquiry_stats(inquiry_date, avg_amt_on_day)
    return


if __name__ == '__main__':
   main()
