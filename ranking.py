"""
Harrison Kaiser
2017 December 10
This program ranks the countries by life expectancy
"""

from utils import *

def sorted_ranking_data(data, year):
    """
    This function sorts ranking data and returns it in a list
    :param data: list - information about countries
    :param year: int - year that the user would like to rank life expectancy data
    :return: list - sorted ranking data
    """
    unsorted = []
    for nation in data:
        if nation.le_data[year] == 0.0:
            continue
        else:
            ca = CountryValue(nation.name, nation.le_data[year])
            unsorted.append(ca)
    sorted = quickSort(unsorted)
    return sorted

def top_ten(data, year):
    """
    This function prints the top ten life expectancies for a given year
    :param data: list - sorted ranking data
    :param year: int - year to rank data by
    """
    print("Top 10 Life Expectancy for", year)
    i = 1
    for nation in data:
        if i == 11:
            break
        print(str(i) + ": " + nation.country + " " + str(nation.value))
        i = i + 1

def bottom_ten(data, year):
    """
    This function prints the bottom ten life expectancies for a given year
    :param data: list - sorted ranking data
    :param year: int - year to rank data by
    """
    print("Bottom 10 Life Expectancy for", year)
    i = len(data)
    x = 0
    for nation in reversed(data):
        if x == 10:
            break
        print(str(i) + ": " + nation.country + " " + str(nation.value))
        x = x + 1
        i = i - 1

def filter1(data, region, income):
    """
    This function filters the data by region and income
    :param data: list - information about all countries read from the files
    :param region: string - region to filter out
    :param income: string - income group to filter out
    :return: list - filtered countries
    """
    data1 = filter_region(data, region)
    return filter_income(data1, income)

def loop_ranking():
    """
    This function asks the user for year, region, and income group
    Then it prints the top ten and bottom ten for the sorted ranked data
    """
    while True:
        year = input("Enter year of interest (-1 to quit): ")
        if int(year) == -1:
            break
        elif int(year) < 1960 or int(year) > 2015:
            print("Valid years are 1960-2015")
        else:
            region = input("Enter region (type ’all’ to consider all): ")
            if is_region(region) == False:
                print(region + " is not a valid region")
            else:
                income = input("Enter income category (type ’all’ to consider all): ")
                data = filter1(read_data("worldbank_life_expectancy"), region, income)
                sorted = sorted_ranking_data(data, int(year))
                print("")
                top_ten(sorted, year)
                print("")
                bottom_ten(sorted, year)

def main():
    loop_ranking()

if __name__ == '__main__':
    main()