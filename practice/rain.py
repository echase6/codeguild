"""Rain database processor.

Accesses City of Portland rain total database and returns various information
about rain totals.
"""
import urllib.request
import re
import os.path


def get_daily_totals(filename):
    """Return a dict of days and daily amounts, as rows from the file."""
    totals = {}
    with open(filename) as f:
        for i in range(11):
            _ = f.readline()
        for line in f:
            day_stats = line.split()[0:2]
            if day_stats[1] != '-':  # skip entries if there is missing data
                totals.update({day_stats[0]: int(day_stats[1])})
    return totals


def find_wettest_stats(totals):
    """Return wettest day (or year) and the amount on the wettest day (or year).

    >>> find_wettest_stats({'30-MAR-2016': 0, '29-MAR-2016': 5})
    ('29-MAR-2016', 5)
    """
    totals_dict = {totals[k]: k for k in totals}
    largest = max(totals_dict)
    return totals_dict[largest], largest


def calc_yearly_total_stats(totals):
    """Return a dictionary of years and sum amounts.

    >>> calc_yearly_total_stats({'30-MAR-2016': 1, '29-MAR-2016': 5,
    ...                         '30-MAR-2015': 0, '29-MAR-2015': 5})
    {'2015': 5, '2016': 6}
    """
    years_unique = set()
    for date in totals:
        year = date.split('-')[2]
        years_unique.add(year)
    yearly_totals = {}
    for year in years_unique:
        yearly_totals.update({year: sum([totals[date] for date in totals
                              if date.split('-')[2] == year])})
    return dict(sorted(yearly_totals.items()))


def calc_daily_avg_stats(totals):
    """Return a dictionary of days and average amounts.

    >>> calc_daily_avg_stats({'30-MAR-2016': 1, '29-MAR-2016': 5,
    ...                      '30-MAR-2015': 3, '29-MAR-2015': 3})
    {'30-MAR': 2.0, '29-MAR': 4.0}
    """
    days_unique = set()
    for date in totals:
        day = '-'.join(date.split('-')[0:2])
        days_unique.add(day)
    daily_avg = {}
    for day in days_unique:
        daily_stats = ([totals[date] for date in totals
                        if '-'.join(date.split('-')[0:2]) == day])
        daily_avg.update({day: (sum(daily_stats) / len(daily_stats))})
    return daily_avg


def find_avg_amt_on_day(date, averages):
    """Return the amount associated with a particular day from a dict.

    >>> find_avg_amt_on_day('29-MAR', {'30-MAR': 1.0, '29-MAR': 5.0})
    5.0
    """
    return averages[date]


def get_inquiry_date():
    """Return the user's selection of a date for subsequent inquiry."""
    return input('What date would you like to check (DD-MMM): ').upper()


def output_most_rain_stats(day, day_amt, year, year_amt):
    """Print the wettest day and year statistics.

    >>> output_most_rain_stats('29-MAR-2015', 25, '2012', 5520)
    Wettest day was 29-MAR-2015, amount was 0.25"
    Wettest year was 2012, amount was 55.2"
    """
    print('Wettest day was {}, amount was {}"'.format(day, day_amt/100))
    print('Wettest year was {}, amount was {}"'.format(year, year_amt/100))


def output_wettest_doy_stats(day, amt):
    """Print the wettest day of the year amount

    >>> output_wettest_doy_stats('29-MAR', 25)
    Wettest day of the year is 29-MAR with 0.25"
    """
    print('Wettest day of the year is {} with {:.2f}"'.format(day, amt/100))


def output_inquiry_stats(date, amt):
    """Print the average amount for a requested day of year

    >>> output_inquiry_stats('29-MAR', 25)
    Average rainfall on 29-MAR is 0.25"
    """
    print('Average rainfall on {} is {:.2f}"'.format(date, amt/100))


def read_store_html_source(site_name, file_name):
    """Read and store local copy of html source, if the copy does not exist."""
    if not os.path.isfile(file_name):
        with urllib.request.urlopen(site_name) as rain_file:
            web_text = rain_file.read().decode('utf-8')
        with open(file_name, "w+") as file:
            file.writelines(web_text)


def read_html_file(filename):
    """Read and return a list of the names and files of the rain gages."""
    with open(filename) as file:
        file_contents = file.read()
    names = re.findall(r"<td>.* Rain Gage", file_contents)
    files = re.findall(r"[a-z,_]*\.rain\">", file_contents)
    name_list = [string[4:-10] for string in names]
    file_list = [string[0:-2] for string in files]
    name_file_list = zip(name_list, file_list)
    return list(name_file_list)


def get_gauge_file_name(names):
    """Get the user selection of a rain gage, after showing a gage list."""
    for i, name in enumerate(names):
        print(str(i + 1).ljust(2), name[0][0:19].ljust(21), end='')
        if (i + 1) % 3 == 0:
            print()
    print()
    num = int(input('What gauge number do you want to process: '))
    return names[num-1][1]


def load_rain_file():
    """Load and store the .rain file for the user-selected gage."""
    web_filename = 'http://or.water.usgs.gov/non-usgs/bes/'
    website_local_copy_filename = 'rain_website_file.txt'
    read_store_html_source(web_filename, website_local_copy_filename)
    gauge_names_files = read_html_file(website_local_copy_filename)
    gauge_filename = get_gauge_file_name(gauge_names_files)
    read_store_html_source(web_filename + gauge_filename, gauge_filename)
    return gauge_filename


def calc_print_most_rain_stats(daily_totals):
    """Calculate and print the wettest day & year, plus amounts."""
    wtst_day, wtst_day_amt = find_wettest_stats(daily_totals)
    yearly_totals = calc_yearly_total_stats(daily_totals)
    wtst_year, wtst_year_amt = find_wettest_stats(yearly_totals)
    output_most_rain_stats(wtst_day, wtst_day_amt, wtst_year, wtst_year_amt)


def calc_print_most_rain_doy(daily_totals):
    """Calculate and print the average wettest day of year."""
    wettest_doy, wettest_doy_amt = find_wettest_stats(daily_totals)
    output_wettest_doy_stats(wettest_doy, wettest_doy_amt)


def calc_print_inquiry_rain(daily_averages):
    """Find and print average rain on date user requests."""
    inquiry_date = get_inquiry_date()
    avg_amt_on_day = find_avg_amt_on_day(inquiry_date, daily_averages)
    output_inquiry_stats(inquiry_date, avg_amt_on_day)


def main():
    gauge_filename = load_rain_file()
    daily_totals = get_daily_totals(gauge_filename)
    daily_averages = calc_daily_avg_stats(daily_totals)
    calc_print_most_rain_stats(daily_totals)
    calc_print_most_rain_doy(daily_averages)
    calc_print_inquiry_rain(daily_averages)


if __name__ == '__main__':
    main()
