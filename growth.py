"""
Harrison Kaiser
2017 December 10
This program ranks countries by absolute growth in life expectancies over a specified range of years
"""

from utils import *

def growth_rate(val1, val2):
    """
    This function calculates the difference in life expectancies
    :param val1: float - life expectancy value
    :param val2: float - life expectancy value
    :return: float - difference of the two values
    """
    rate = (val2 - val1)
    return rate

def sorted_growth_data(data, year1, year2):
    """
    This function sorts the growth rates for specified range of years
    :param data: list - inforomation about all countries
    :param year1: int - starting year
    :param year2: int - ending year
    :return: 
    """
    unsorted = []
    for nation in data:
        if nation.le_data[year1] == "" or nation.le_data[year2] == "":
            continue
        elif nation.le_data[year1] == 0.0 or nation.le_data[year2] == 0.0:
            continue
        else:
            ca = CountryValue(nation.name, growth_rate(nation.le_data[year1], nation.le_data[year2]))
            unsorted.append(ca)
    sorted = quickSort(unsorted)
    return sorted

def filter1(data, region, income):
    """
    This function filters out the countries by income group and region
    :param data: list - information about all countries
    :param region: string - name of region
    :param income: string - name of income group
    :return: list - information about all filtered countries
    """
    data1 = filter_region(data, region)
    return filter_income(data1, income)

def top_ten(data, year1, year2):
    """
    This function prints the top ten growth rates in life expectancies for a specified range of years
    :param data: list - information about all filtered countries
    :param year1: int - starting year
    :param year2: int - ending year
    """
    print("Top 10 Life Expectancy Growth: " + str(year1) + " to " + str(year2))
    i = 1
    for nation in data:
        if i == 11:
            break
        print(str(i) + ": " + nation.country + " " + str(nation.value))
        i = i + 1

def bottom_ten(data, year1, year2):
    """
    This function prints the top ten growth rates in life expectancies for a specified range of years
    :param data: list - information about all filtered countries
    :param year1: int - starting year
    :param year2: int - ending year
    """
    print("Bottom 10 Life Expectancy Growth: " + str(year1) + " to " + str(year2))
    i = len(data)
    x = 0
    for nation in reversed(data):
        if x == 10:
            break
        print(str(i) + ": " + nation.country + " " + str(nation.value))
        x = x + 1
        i = i - 1

def loop_growth():
    """
    This function asks the user for the range of years to be ranked and for region and income group
    prints the top ten and bottom ten
    """
    while True:
        year1 = input("Enter starting year of interest (-1 to quit): ")
        year2 = input("Enter ending year of interest (-1 to quit): ")
        if int(year1) == -1 or int(year2) == -1:
            break
        elif (int(year1) < 1960 or int(year1) > 2015) or (int(year2) < 1960 or int(year2) > 2015):
            print("Valid years are 1960-2015")
        else:
            region = input("Enter region (type ’all’ to consider all): ")
            income = input("Enter income category (type ’all’ to consider all): ")
            data = filter1(read_data("worldbank_life_expectancy"), region, income)
            sorted = sorted_growth_data(data, int(year1), int(year2))
            print("")
            top_ten(sorted, year1, year2)
            print("")
            bottom_ten(sorted, year1, year2)

def main():
    loop_growth()

if __name__ == '__main__':
    main()
