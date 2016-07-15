"""Rain database processor.

Accesses City of Portland rain total database and returns various information
about rain totals.
"""

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
    """Return a list of lists of years and sum amounts."""
    years = set()
    yearly_totals = []
    for date, amount in totals:
        year = date.split('-')[2]
        years.add(year)
    for year in years:
        yearly_totals += [[year, sum([amt for date, amt in totals
                                   if date.split('-')[2] == year])]]
    return yearly_totals


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
    # wettest_avg_day = find_wettest_avg_day(daily_totals)
    # inquiry_date = get_inquiry_date()
    # average_amount_on_day = find_avg_amt_on_day(inquiry_date)
    output_most_rain_stats(wettest_day, wettest_day_amt, wettest_year, wettest_year_amt)
    return


if __name__ == '__main__':
    main()
