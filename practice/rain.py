"""Rain database processor.

Accesses City of Portland rain total database and returns various information
about rain totals.
"""
import urllib.request
import re
import os.path
import statistics
from operator import itemgetter
from itertools import groupby


def get_file_contents(filename):
    """Extract file contents and return such in a list of strings."""
    with open(filename) as f:
        contents = f.readlines()
    return contents


def get_daily_totals(contents):
    r"""Return a dict of days and daily amounts, as rows from the file.

    >>> sorted(get_daily_totals(['1.', '2.', '3.', '4.', '5.', '6.',
    ...                  '7.', '8.', '9.', '10.', '11.',
    ...                  '25-MAR-2016    0', '26-MAR-2016      1']).items())
    [('25-MAR-2016', 0), ('26-MAR-2016', 1)]
    """
    totals = {}
    for line in contents[11:]:  # skip header lines
        day_stats = line.split()[0:2]
        if day_stats[1] != '-':  # skip entries if there is missing data
            totals.update({day_stats[0]: int(day_stats[1])})
    return totals


def find_wettest_stats(dates_totals):
    """Return wettest day (or year) and the amount on the wettest day (or year).

    >>> find_wettest_stats({'30-MAR-2016': 0, '29-MAR-2016': 5})
    ('29-MAR-2016', 5)
    """
    return max(dates_totals.items(), key=itemgetter(1))


def calc_yearly_total_stats(totals):
    """Return a dictionary of years and sum amounts.

    >>> sorted(calc_yearly_total_stats({'29-MAR-2015': 1, '30-MAR-2015': 5,
    ...                         '29-MAR-2016': 0, '30-MAR-2016': 5}).items())
    [('2015', 6), ('2016', 5)]
    """
    yearly_data = sorted([[k.split('-')[2], v]
                          for k, v in totals.items()])
    yearly_totals = {key: sum([value[1] for value in values])
                     for key, values in groupby(yearly_data, lambda x: x[0])}
    return yearly_totals


def calc_daily_avg_stats(totals):
    """Return a dictionary of days and average amounts.

    >>> sorted(calc_daily_avg_stats({'30-MAR-2016': 1, '29-MAR-2016': 5,
    ...                      '30-MAR-2015': 3, '29-MAR-2015': 3}).items())
    [('29-MAR', 4), ('30-MAR', 2)]
    """
    daily_data = sorted([['-'.join(k.split('-')[0:2]), v]
                        for k, v in totals.items()])
    daily_averages = {key: statistics.mean([value[1] for value in values])
                      for key, values in groupby(daily_data, lambda x: x[0])}
    return daily_averages


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
    """Print the wettest day of the year amount.

    >>> output_wettest_doy_stats('29-MAR', 25)
    Wettest day of the year is 29-MAR with 0.25"
    """
    print('Wettest day of the year is {} with {:.2f}"'.format(day, amt/100))


def output_inquiry_stats(date, amt):
    """Print the average amount for a requested day of year.

    >>> output_inquiry_stats('29-MAR', 25)
    Average rainfall on 29-MAR is 0.25"
    """
    print('Average rainfall on {} is {:.2f}"'.format(date, amt/100))


def read_store_html_source(site_name, file_name):
    """Read and store local copy of html source, if the copy does not exist."""
    if not os.path.isfile(file_name):
        print('Loading copy of {}...'.format(file_name))
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
    """Calculate and print the wettest day & year, plus amounts.

    >>> calc_print_most_rain_stats({'30-MAR-2016': 1, '29-MAR-2016': 15,
    ...                             '30-MAR-2015': 3, '29-MAR-2015': 2})
    Wettest day was 29-MAR-2016, amount was 0.15"
    Wettest year was 2016, amount was 0.16"
    """
    wtst_day, wtst_day_amt = find_wettest_stats(daily_totals)
    yearly_totals = calc_yearly_total_stats(daily_totals)
    wtst_year, wtst_year_amt = find_wettest_stats(yearly_totals)
    output_most_rain_stats(wtst_day, wtst_day_amt, wtst_year, wtst_year_amt)


def calc_print_most_rain_doy(daily_totals):
    """Calculate and print the average wettest day of year.

    >>> calc_print_most_rain_doy({'30-MAR': 1, '29-MAR': 15})
    Wettest day of the year is 29-MAR with 0.15"
    """
    wettest_doy, wettest_doy_amt = find_wettest_stats(daily_totals)
    output_wettest_doy_stats(wettest_doy, wettest_doy_amt)


def calc_print_inquiry_rain(daily_averages, inquiry_date):
    """Find and print average rain on date user requests.

    >>> calc_print_inquiry_rain({'30-MAR': 1, '29-MAR': 15}, '29-MAR')
    Average rainfall on 29-MAR is 0.15"
    """
    avg_amt_on_day = daily_averages[inquiry_date]
    output_inquiry_stats(inquiry_date, avg_amt_on_day)


def main():
    gauge_filename = load_rain_file()
    contents = get_file_contents(gauge_filename)
    daily_totals = get_daily_totals(contents)
    daily_averages = calc_daily_avg_stats(daily_totals)
    calc_print_most_rain_stats(daily_totals)
    calc_print_most_rain_doy(daily_averages)
    inquiry_date = get_inquiry_date()
    calc_print_inquiry_rain(daily_averages, inquiry_date)


if __name__ == '__main__':
    main()
