"""
Harrison Kaiser
2017 December 10
"""

from utils import *

def sorted_drop_data(data):
    """
    This function sorts the biggests drops in life expectancy for each country
    :param data: list - information about all filtered countries
    :return: list - sorted drops in life expectancies for each country
    """
    unsorted = []
    for nation in data:
        le = nation.le_data
        smallest = 0
        for year in le.keys():
            first_year = year
            first_value = le[first_year]
            for i in range((year+1), 2016):
                second_year = i
                second_value = le[second_year]
                if first_value == 0.0:
                    break
                elif second_value == 0.0:
                    continue
                elif first_value > second_value:
                    value = second_value - first_value
                    if value < smallest:
                        smallest = value
                        first = (first_year, first_value)
                        second = (second_year, second_value)
                    else:
                        continue
        if smallest < 0:
            country = Range(nation.name, first[0], second[0], first[1], second[1])
            unsorted.append(country)
        else:
            continue
    sorted = quickSortGrowth(unsorted)
    return sorted

def main():
    """
    Prints the top ten drops in life expectancies of all countries
    """
    print("Worst Life expectancy drops: 1960 to 2015")
    top_ten = sorted_drop_data(filter_region(read_data("worldbank_life_expectancy"), "all"))
    print(top_ten[-1].country)
    print(top_ten[-2].year1)
    top_ten = top_ten[:10]
    i = 1
    for nation in top_ten:
        diff = nation.value2 - nation.value1
        print(str(i) + ": " + nation.country + " from " + str(nation.year1) + " (" + str(nation.value1) + ")" + " to " + str(nation.year2) + " (" + str(nation.value2) + "): " + str(diff))
        i = i + 1

if __name__ == '__main__':
    main()
