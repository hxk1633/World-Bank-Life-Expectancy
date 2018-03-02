"""
Harrison Kaiser
2017 December 10
This program creates data structures needed for this project
"""
from rit_lib import *
from quickSort import *
from quickSortGrowth import *
from quickSortFactors import *

region_data = struct_type("region_data", (str, "name"), (str, "code"), (dict, "le_data"), (str, "income"), (str, "region"))
region_metadata = struct_type("region_metadata", (str, "code"), (str, "name"), (str, "income"))
CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))
Range = struct_type("Range", (str, "country"), (int, "year1"), (int, "year2"), (float, "value1"), (float, "value2"))
regions = {}

def read_data(filename):
    """
    This function reads the life expectancy data and stores the data in a dictionary
    :param filename: string = name of file to be read
    :return: dictionary - contains all of the information about the countries
    """
    data = "data/" + filename + "_data.txt"
    metadata = "data/" + filename + "_metadata.txt"
    file1 = open(metadata)
    file1.readline()
    for line in file1:
        line = line.strip().split(",")
        income_group = region_metadata(line[0], line[1], line[2])
        if income_group.name == '':
            regions[income_group.code] = [income_group.income, "group"]
        else:
            regions[income_group.code] = [income_group.income, income_group.name]
    file1.close()
    file2 = open(data)
    file2.readline()
    for line in file2:
        i = 2
        line = line.strip().split(",")
        year_data = {}
        for year in range(1960, 2016):
            if line[i] == '':
                year_data[year] = 0.0
            else:
                year_data[year] = float(line[i])
            i = i + 1
        region = region_data(line[0], line[1], year_data, '', '')
        regions[region.code].append(region.name)
        regions[region.code].append(region.le_data)
        regions[region.code].append(region.code)
    file2.close()
    return regions

def filter_region(data, region):
    """
    This function filters the countries by region specified in parameter
    :param data: dictionary - information read from files
    :param region: string - name of region to filter out
    :return: list - contains filtered countries and their information
    """
    filter = []
    if region == "all":
        for country in data.keys():
            if regions[country][1] == "group":
                continue
            else:
                territory = region_data(regions[country][2], country, regions[country][3], regions[country][0], regions[country][1])
                filter.append(territory)
        return filter
    elif region == '':
        return None
    else:
        for country in data.keys():
            if regions[country][1] == region:
                territory = region_data(regions[country][2], country, regions[country][3], regions[country][0], regions[country][1])
                filter.append(territory)
            else:
                continue
        return filter

def filter_income(data, income):
    """
    This function filters the countries by income
    :param data: list or dictionary - filtered region info or data originally read from files
    :param income: string - income to filter out
    :return: list - information about countries of select income group
    """
    if type(data) == list:
        filtered = []
        if income == "all":
            for nation in data:
                filtered.append(nation)
            return filtered
        else:
            for nation in data:
                if nation.income == income:
                    filtered.append(nation)
            return filtered
    else:
        filtered = []
        if income == "all":
            for country in data.keys():
                if regions[country][1] == "group":
                    continue
                else:
                    territory = region_data(regions[country][2], country, regions[country][3], regions[country][0], regions[country][1])
                    filtered.append(territory)
            return filtered
        elif income == '':
            return None

def count_groupings(data):
    """
    This function counts the groupings
    :param data: list - information about all filtered countries
    :return: int - number of groupings
    """
    count = 0
    for region in data.keys():
        if regions[region][1] == "group":
            count = count + 1
    return count

def count_regions(data):
    """
    This function counts the number of countries in each region
    :param data: list - information about filtered countries
    :return: tuple - contains counts of each region
    """
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    for region in data.keys():
        if regions[region][1] == "Middle East & North Africa":
            count1 = count1 + 1
        elif regions[region][1] == "Europe & Central Asia":
            count2 = count2 + 1
        elif regions[region][1] == "North America":
            count3 = count3 + 1
        elif regions[region][1] == "Latin America & Caribbean":
            count4 = count4 + 1
        elif regions[region][1] == "South Asia":
            count5 = count5 + 1
        elif regions[region][1] == "East Asia & Pacific":
            count6 = count6 + 1
        elif regions[region][1] == "Sub-Saharan Africa":
            count7 = count7 + 1
        else:
            continue
    return (count1, count2, count3, count4, count5, count6, count7)

def count_income(data):
    """
    This function counts the number of countries in each income category
    :param data: list - information about filtered countries
    :return: tuple - contains counts of each income category
    """
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for region in data.keys():
        if regions[region][0] == "Lower middle income":
            count1 = count1 + 1
        elif regions[region][0] == "Upper middle income":
            count2 = count2 + 1
        elif regions[region][0] == "High income":
            count3 = count3 + 1
        elif regions[region][0] == "Low income":
            count4 = count4 + 1
        else:
            continue
    return (count1, count2, count3, count4)

def print_nations(list):
    """
    This function prints the country name and country code
    :param list: information about filtered countries
    """
    for nation in list:
        print(nation.name + "(" + nation.code + ")")

def is_country(data, country):
    """
    This function tests user input
    :param data: list - information about filtered countries
    :param country: string - user input
    :return: boolean - returns True if it's an actual country
    """
    try:
        for region in data:
            if region.name == country:
                return True
    except:
        print(data)

def country_code(data, name):
    for nation in data:
        if nation.name == name:
            return nation.code

def is_region(region):
    if region == "Sub-Saharan Africa":
        return True
    elif region == "South Asia":
        return True
    elif region == "Europe & Central Asia":
        return True
    elif region == "Latin America & Caribbean":
        return True
    elif region == "Middle East & North Africa":
        return True
    elif region == "North America":
        return True
    elif region == "East Asia & Pacific":
        return True
    else:
        return False

def loop(data):
    """
    This function asks the user to enter country name or code and prints the country name and life expectancy data
    :param data: list - information about filtered countries
    """
    while True:
        print("")
        name = input("Enter name of country or country code (Enter to quit): ")
        if name == "":
            break
        if is_country(data, name) or name in regions:
            print("Data for " + name + ":")
            if len(name) == 3:
                for nation in data:
                    if nation.code == name:
                        le_data = nation.le_data
            else:
                for nation in data:
                    if nation.name == name:
                        le_data = nation.le_data
            for year in le_data.keys():
                if le_data[year] == 0.0:
                    continue
                else:
                    print("Year: " + str(year) + " Life expectancy: " + str(le_data[year]))
        else:
            print("'" + name + "'" + " is not a valid country name or code")

def main():
    """
    Prints general information about countries like number of groupings, number of entities...
    Then it lets the user enter a region name to see which countries are in that region
    And it also lets the user enter an income group to see which countries belong in that income group
    Then it calls the looping function to give user more information such as life expectancy data
    """
    data = read_data("worldbank_life_expectancy")
    (me_na, e_ca, na, la_c, sa, ea_p, ssa) = count_regions(data)
    (lower, upper, high, low) = count_income(data)
    print("Total number of entities:", len(data))
    print("Number of countries/territories:", len(data) - count_groupings(data))
    print("")
    print("Regions and their country count:")
    print("Middle East & North Africa:", me_na)
    print("Europe & Central Asia:", e_ca)
    print("North America:", na)
    print("Latin America & Caribbean:", la_c)
    print("South Asia:", sa)
    print("East Asia & Pacific:", ea_p)
    print("Sub-Saharan Africa:", ssa)
    print("")
    print("Income categories and their country count:")
    print("Lower middle income:", lower)
    print("Upper middle income:", upper)
    print("High income:", high)
    print("Low income", low)
    print("")
    region_name = input("Enter region name: ")
    filtered_region = filter_region(data, region_name)
    print("Countries in the '" + region_name + "' region:")
    print_nations(filtered_region)
    print("")
    income_name = input("Enter income category: ")
    filtered_income = filter_income(filter_region(data, "all"), income_name)
    print("Countries in the '" + income_name + "' income category:")
    print_nations(filtered_income)
    d = filter_region(data, "all")
    loop(d)


if __name__ == '__main__':
    main()